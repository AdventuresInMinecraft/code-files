# Adventure 2: whereAmI2.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program works out where you are in the Minecraft world.
# It uses a game loop to repeatedly display your position
# on the Minecraft chat.

# The Minecraft API has to be imported before it can be used
import mcpi.minecraft as minecraft

# The time module allows you to insert time delays
import time

# To communicate with a running Minecraft game, 
# you need a connection to that game.
mc = minecraft.Minecraft.create()

# A game loop will make sure your game runs forever
while True:
    # delay, to prevent the Minecraft chat filling up too quickly
    time.sleep(1)
    
    # Ask the Minecraft game for the position of your player
    pos = mc.player.getTilePos()
    
    # Display the coordinates of the players position
    mc.postToChat("x="+str(pos.x) + " y="+str(pos.y) +" z="+str(pos.z))

# END
