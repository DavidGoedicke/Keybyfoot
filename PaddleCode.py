# Write your code here :-)
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
 
kbd = Keyboard()
 
while True:
    if cpx.button_a:
        kbd.send(Keycode.SHIFT, Keycode.F1)  # Type capital 'A'
        while cpx.button_a: # Wait for button to be released
          pass
 
    if cpx.button_b:
        kbd.send(Keycode.CONTROL, Keycode.F2)  # control-X key
        while cpx.button_b: # Wait for button to be released
          pass