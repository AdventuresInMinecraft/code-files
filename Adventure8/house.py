# Adventure 8: house.py
#
# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program displays a house icon on your micro:bit display
# when you arrive home

# Import necesssary modules
import microbit
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Create a connection to Minecraft
mc = minecraft.Minecraft.create()

# Set the location of your home.
# NOTE: Set these to sensible coordinates before running this code
HOME_X = 0
HOME_Y = 0
HOME_Z = 0

# Build a woollen carpet here so you know where to build your house
mc.setBlock(HOME_X, HOME_Y, HOME_Z, block.WOOL.id, 15)

# The game loop runs forever
while True:
    # Slow things down a bit, so you don't overload your computer
    time.sleep(1)
    # Work out where Steve is standing
    pos = mc.player.getTilePos()
    # If Steve is standing on the doormat
    if pos.x == HOME_X and pos.z == HOME_Z:
        # Display a standard house image from the micro:bit image library
        microbit.display.show(microbit.Image.HOUSE)
    else:
        # Display a ? so you know your micro:bit is still doing something
        microbit.display.show('?')

# END
