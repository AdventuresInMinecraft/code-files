# Adventure 3: build.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program builds a block at an absolute coordinate

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Build a block
mc.setBlock(1, 2, 3, block.DIAMOND_BLOCK.id)

# END



