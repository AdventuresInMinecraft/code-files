# Adventure 8: house2.py
#
# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program shows how to design a custom house icon for your micro:bit

# Import necessary modules
import microbit
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Create a connection to the Minecraft game
mc = minecraft.Minecraft.create()

# Define a custom image for your house icon
MYHOUSE = microbit.Image("00900:09090:90009:99999:09990")

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
        # Display your custom house image on the micro:bit display
        microbit.display.show(MYHOUSE)
    else:
        # Display a ? so you know your micro:bit is still doing something
        microbit.display.show('?')

# END
