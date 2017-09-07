# Adventure 8: banana.py
#
# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html

import microbit
import time

BANANA = microbit.Image("00090:00090:00990:09900:99000")

while True:
    time.sleep(0.25)
    if microbit.pin0.is_touched():
        microbit.display.show(BANANA)
    else:
        microbit.display.show('?')

# END

