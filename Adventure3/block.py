# Adventure 3: block.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program builds a block next to your player.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position
pos = mc.player.getTilePos()

# Create a block in front of the player
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)

# END
