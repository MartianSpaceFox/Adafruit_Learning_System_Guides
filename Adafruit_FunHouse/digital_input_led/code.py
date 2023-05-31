"""CircuitPython Digital Input Example for FunHouse"""

import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.BUTTON_UP)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    led.value = bool(button.value)
