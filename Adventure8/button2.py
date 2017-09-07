# Adventure 8: button2.py
#
# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html
#
# This program shows how to write to your micro:bit display when you press a button

# Import necessary modules
import time
import microbit

# Display a message in the Python shell window
print("press button A to test")

# Loop forever
while True:
    # Sense when the A button has been pressed on the micro:bit
    if microbit.button_a.was_pressed():
        # Display message in Python shell window
        print("Button A pressed")
        # Also display letter A on micro:bit display for half a second
        microbit.display.show("A")
        time.sleep(0.5)
        microbit.display.clear()

# END
