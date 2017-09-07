# Adventure 8: button.py
#
# From the book: "Adventures in Minecraft", 2nd Edition
# written by David Whale and Martin O'Hanlon, Wiley, 2017
# http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1119439582.html

# Import necessary modules
import time
import microbit

# Display a message in the Python shell window
print("press button A to test")

# Loop forever waiting for the A button to be pressed
while True:
    # Check if the A buton has been pressed
    if microbit.button_a.was_pressed():
        # Display a message and delay a while to prevent flood of messages
        print("Button A pressed")
        time.sleep(0.5)

# END
