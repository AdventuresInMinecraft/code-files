# Adventure 3: tower.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program builds a tall tower inside Minecraft, using a for loop.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position
pos = mc.player.getTilePos()

# Build a tower 50 blocks high
for a in range(50):
    # Each block is at height: y+a
    mc.setBlock(pos.x+3, pos.y+a, pos.z, block.STONE.id)

# END

