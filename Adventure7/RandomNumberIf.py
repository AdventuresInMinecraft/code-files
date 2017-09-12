# Adventure 7: RandomNumberIf.py

# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program shows how to use random numbers and probability to make
# different things happen.

import random
if random.randint(1,10) == 10:
    print("This happens about 1 time in 10")
else:
    print("This happens about 9 times out of 10")

