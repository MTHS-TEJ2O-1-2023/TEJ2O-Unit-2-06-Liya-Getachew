"""
Created by: Liya Getachew
Created on: Sep 2023
This module is a Micro:bit MicroPython program that turns an LED on and off.
"""

from microbit import *

"setup"
display.clear
display.show(Image.HAPPY)

while True:
    "LED on"
    if button_a.is_pressed():
        pin16.write_digital(1)
        display.show(Image.YES)
    "LED off"
    if button_b.is_pressed():
        pin16.write_digital(0)
        display.show(Image.NO)
