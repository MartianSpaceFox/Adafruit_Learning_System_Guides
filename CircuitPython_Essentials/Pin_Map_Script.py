"""CircuitPython Essentials Pin Map Script"""

import microcontroller
import board

board_pins = []
for pin in dir(microcontroller.pin):
    if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
        if pins := [
            f"board.{alias}"
            for alias in dir(board)
            if getattr(board, alias) is getattr(microcontroller.pin, pin)
        ]:
            board_pins.append(" ".join(pins))
for pins in sorted(board_pins):
    print(pins)
