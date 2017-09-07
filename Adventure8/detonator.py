# Adventure 8: detonator.py
#
# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program sets off an explosion when you touch a banana connected to your micro:bit
# NOTE: You can also use an orange, if you don't have a banana handy

# Import necessary modules
import microbit
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Define a custom image that looks a bit like a banana
BANANA = microbit.Image("00090:00090:00990:09900:99000")

# Create a connection to the Minecraft game
mc = minecraft.Minecraft.create()

# Define a function that will set off an explosion at a position in Minecraft
def bomb(x, y, z):
    # TNT goes into the centre of the blast area
    mc.setBlock(x+1, y, z+1, block.TNT.id)

    # Count down 5,4,3,2,1 on the micro:bit display
    for t in range(6):
        microbit.display.show(str(5-t))
        time.sleep(1)

    # The explosion is simulated, by setting a range of blocks to AIR
    mc.postToChat("BANG!")
    mc.setBlocks(x-10, y-5, z-10, x+10, y+10, z+10, block.AIR.id)

# The game loop runs forever
while True:
    # Slow things down a bit so you don't overload your computer
    time.sleep(0.1)
    # Only when you touch the P0 pin
    if microbit.pin0.is_touched():
        # Show your custom banana image on the micro:bit display
        microbit.display.show(BANANA)
        # Get Steve's position and set of an explosion where he is standing
        pos = mc.player.getTilePos()
        bomb(pos.x, pos.y, pos.z)
    else:
        # Put something on the micro:bit display so you know it is still working
        microbit.display.show('?')

# END
