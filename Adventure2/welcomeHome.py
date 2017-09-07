# Adventure 2: welcomeHome.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program creates a magic doormat that says "welcome home"
# when you stand on it.

# Import necessary modules
import mcpi.minecraft as minecraft
import time

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()

# The main game loop
while True:
    # Short delay to prevent chat filling up too quickly
    time.sleep(1)
  
    # Get player position
    pos = mc.player.getTilePos()
  
    # Check whether your player is standing on the mat
    if pos.x == 10 and pos.z == 12:
        mc.postToChat("welcome home")
        
# END
