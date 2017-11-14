# Adventure 8: ballgame.py
#
# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program is a complete mini-game involving rolling a ball on a table

# Import necessary modules
import microbit
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# CONSTANTS
# Change these to vary the size/difficulty of the game
TABLE_WIDTH = 20
TABLE_DEPTH = 20
TREASURE_COUNT = 25
TABLE = block.STONE.id
BALL = block.CACTUS.id
TREASURE = block.GOLD_BLOCK.id

# Connect to the Minecraft game and
# let the player know that the micro:bit is connected
mc = minecraft.Minecraft.create()
mc.postToChat("BBC micro:bit joined the game")

# VARIABLES

table_x = None
table_y = None
table_z = None
ball_x = None
ball_y = None
ball_z = None
speed_x = 0
speed_z = 0
remaining = 1

# Build a complete game table
def build_table(x, y, z):
    global table_x, table_y, table_z
    # Put a small gap around the edge in case of nearby mountains
    GAP = 10
    mc.setBlocks(x-GAP, y, z-GAP, x+TABLE_WIDTH+GAP, y+GAP, z+TABLE_DEPTH+GAP,
                 block.AIR.id)
    # Build the table as a big block
    mc.setBlocks(x-1, y, z-1, x+TABLE_WIDTH+1, y+1, z+TABLE_DEPTH+1, TABLE)
    # Carve out the middle, this creates the wall around the table
    mc.setBlocks(x, y+1, z, x+TABLE_WIDTH, y+1, z+TABLE_DEPTH, block.AIR.id)
    # Remember where the table was built, for later
    table_x = x
    table_y = y
    table_z = z

# Place random treasure blocks on the table
def place_treasure():
    y = table_y
    for i in range(TREASURE_COUNT):
        # BUGFIX: Prevent block being re-created in same pos
        # which would make it impossible to complete the game
        while True:
            # Choose a random position for the next block
            x = random.randint(0, TABLE_WIDTH) + table_x
            z = random.randint(0, TABLE_DEPTH) + table_z
            # Is it already a treasure block?
            b = mc.getBlock(x,y,z)
            if b == TREASURE: continue # if so, loop round to try again
            # Place treasure at the new random location
            mc.setBlock(x, y, z, TREASURE)
            break # break out of loop to move to next treasure block
        # BUGFIX END

# Move the ball based on the present ball speed
def move_ball():
    new_x = ball_x - speed_x
    new_z = ball_z - speed_z
    if ball_x != new_x or ball_z != new_z: # prevent screen flicker
        # Don't draw the ball if it falls off the table for some reason
        if is_on_table(new_x, new_z):
            move_ball_to(new_x, ball_y, new_z)

# Move the ball to a specific position on the table
def move_ball_to(x, y, z):
    global ball_x, ball_y, ball_z
    # Clear the existing ball if it has already been built
    if ball_x is not None:
        mc.setBlock(ball_x, ball_y, ball_z, block.AIR.id)
    # Update our record of where the ball is now
    ball_x = x
    ball_y = y
    ball_z = z
    # Build a block where the ball needs to be
    mc.setBlock(ball_x, ball_y, ball_z, BALL)

# Calculate a new speed value, given the existing speed and amount of tilt.
# You can change this algorithm to make the acceleration and deceleration of
# the ball more life-like
def new_speed(speed, tilt):
    # Create a dead spot when the micro:bit is flat to slow/stop the ball
    if abs(tilt) < 300: tilt = 0
    # Reduce the range of the tilt to roughly -3..+3
    tilt = tilt / 300
    # Adjust the speed gradually each time, to simulate simple acceleration
    if tilt < speed:
        speed = speed - 1
    elif tilt > speed:
        speed = speed + 1
    return speed

# Sense the amount of tilt of the micro:bit and update the speed variables
def check_tilt():
    global speed_x, speed_z
    speed_x = new_speed(speed_x, microbit.accelerometer.get_x())
    speed_z = new_speed(speed_z, microbit.accelerometer.get_y())
    #print(speed_x, speed_z)

# Work out if a given ball position is on the table or not.
# This can be used to prevent the ball rolling off the table.
# It can also be used to sense if it rolls off the table.
def is_on_table(x, z):
    if x < table_x or x > table_x + TABLE_WIDTH:
        return False
    if z < table_z or z > table_z + TABLE_DEPTH:
        return False
    return True

# Check what is below the ball, and action it accordingly
def check_below():
    global remaining
    # What is below the ball?
    block_below = mc.getBlock(ball_x, ball_y-1, ball_z)
    if block_below == TREASURE:
        # It's treasure, so collect it and update the count of remaining items
        mc.setBlock(ball_x, ball_y-1, ball_z, block.AIR.id)
        remaining = remaining - 1
        microbit.display.show(remaining)
    elif block_below == block.AIR.id:
        # It's a hole, so introduce a time-penalty
        move_ball_to(ball_x, ball_y-1, ball_z)
        while not microbit.button_b.was_pressed():
            time.sleep(0.1)
        # Bounce the ball out to a random new position
        move_ball_to(table_x + random.randint(0, TABLE_WIDTH), table_y+1,
                     table_z + random.randint(0, TABLE_DEPTH))

# Wait for the user to start the game
def wait_for_start():
    # A helpful message so that the user knows what to do
    mc.postToChat("press B to start")
    microbit.display.show("?")
    # Wait for the B button to be pressed on the micro:bit
    while not microbit.button_b.was_pressed():
        time.sleep(0.1)

    # Countdown 5,4,3,2,1
    for t in range(6):
        microbit.display.show(str(5-t))
        time.sleep(0.5)

# Build the complete game with table and treasure
def build_game():
    global speed_x, speed_z, remaining

    # Get Steve's position, so the table can be built nearby
    pos = mc.player.getTilePos()
    # Build the table close by
    build_table(pos.x, pos.y-2, pos.z)
    # Start the ball at a random position
    move_ball_to(table_x + random.randint(0, TABLE_WIDTH), table_y+1,
                 table_z + random.randint(0, TABLE_DEPTH))
    # Place all the treasure at random locations
    place_treasure()
    # Place Steve at a good viewing point
    mc.player.setTilePos(table_x + TABLE_WIDTH/2, table_y+1, table_z)
    # Start off the game variables at sensible values
    remaining = TREASURE_COUNT
    speed_x = 0
    speed_z = 0

# Play one complete game from start to end
def play_game():
    # Remember what time the game was started
    start_time = time.time()
    # Loop around a game loop until all treasure is collected
    while remaining > 0:
        # Slow things down a bit, this loop runs 10 times per second
        time.sleep(0.1)
        # Find out how much the user is tilting the micro:bit
        check_tilt()
        # Move the ball based on the tilt
        move_ball()
        # Process treasure or air blocks below the ball
        check_below()
    # Remember what time the game finished
    end_time = time.time()
    # Display the total game time taken to collect all treasure
    mc.postToChat("game time=" + str(int(end_time-start_time)))

# The main program.
# Loops forever, until you press CTRL-C
while True:
    wait_for_start()
    build_game()
    play_game()

# END
