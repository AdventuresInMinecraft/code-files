# Adventure 6: Polygon.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program shows you how to create polygons using the MinecraftDrawing
# functions in minecraftstuff.

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

#create connection to minecraft
mc = minecraft.Minecraft.create()

#create minecraftstuff drawing object
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#get the players position
pos = mc.player.getTilePos()

#draw 2d shapes
# draw a triangle
points = minecraftstuff.Points()
points.add(pos.x, pos.y, pos.z)
points.add(pos.x + 20, pos.y, pos.z)
points.add(pos.x + 10, pos.y + 20, pos.z)
mcdrawing.drawFace(points, True, block.WOOL.id, 6)

#move the position on a bit
pos.x = pos.x + 25

#draw a square
points = minecraftstuff.Points()
points.add(pos.x, pos.y, pos.z)
points.add(pos.x + 20, pos.y, pos.z)
points.add(pos.x + 20, pos.y + 20, pos.z)
points.add(pos.x, pos.y + 20, pos.z)
mcdrawing.drawFace(points, False, block.WOOL.id, 7)

#move the position on a bit
pos.x = pos.x + 25

#4 sided odd shape
points = minecraftstuff.Points()
points.add(pos.x, pos.y, pos.z)
points.add(pos.x + 15, pos.y, pos.z)
points.add(pos.x + 20, pos.y + 15, pos.z)
points.add(pos.x, pos.y + 20, pos.z)
mcdrawing.drawFace(points, True, block.WOOL.id, 8)

#move the position on a bit
pos.x = pos.x + 25

#5 sided odd shape
points = minecraftstuff.Points()
points.add(pos.x, pos.y, pos.z)
points.add(pos.x + 20, pos.y + 5, pos.z)
points.add(pos.x + 15, pos.y + 20, pos.z)
points.add(pos.x + 5, pos.y + 15, pos.z)
points.add(pos.x, pos.y + 5, pos.z)
mcdrawing.drawFace(points, False, block.WOOL.id, 9)
