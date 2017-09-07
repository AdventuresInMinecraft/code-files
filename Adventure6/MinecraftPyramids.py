# Adventure 6: MinecraftPyramids.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html

#import python modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import math

#find point on circle function
def findPointOnCircle(cx, cy, radius, angle):
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    x = int(round(x, 0))
    y = int(round(y, 0))
    return(x,y)

#create connection to minecraft
mc = minecraft.Minecraft.create()

#create minecraft drawing object
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

#pyramid variables
#the midde of the pyramid will be the position of the player
middle = mc.player.getTilePos()

RADIUS = 20
HEIGHT = 10
SIDES = 4

#loop through the number of sides, each side will become a triangle
for side in range(0,SIDES): 
    #find the first point of the triangle
    point1Angle = int(round((360 / SIDES) * side,0))
    point1X, point1Z = findPointOnCircle(middle.x, middle.z,
                                         RADIUS, point1Angle)

    #find the second point of the triangle
    point2Angle = int(round((360 / SIDES) * (side + 1),0))
    point2X, point2Z = findPointOnCircle(middle.x, middle.z,
                                         RADIUS, point2Angle)

    #draw the triangle
    # create the triangle points
    points = minecraftstuff.Points()
    points.add(point1X, middle.y, point1Z)
    points.add(point2X, middle.y, point2Z)
    points.add(middle.x, middle.y + HEIGHT, middle.z)
    
    # draw the triangle
    mcdrawing.drawFace(points, True, block.SANDSTONE.id)

