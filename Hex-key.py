import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define row and column pins
row_pins = [board.D0, board.D1, board.D2, board.D3, board.D4]
col_pins = [
    board.D10, board.MOSI, board.MISO, board.SCK, 
    board.A0, board.A1, board.A2, board.A3, 
    board.D9, board.D8, board.D7, board.D6, board.D5
]

# Set up rows as outputs
rows = []
for pin in row_pins:
    row = digitalio.DigitalInOut(pin)
    row.direction = digitalio.Direction.OUTPUT
    row.value = False  # Default to low
    rows.append(row)

# Set up columns as inputs with pull-ups
cols = []
for pin in col_pins:
    col = digitalio.DigitalInOut(pin)
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.UP
    cols.append(col)

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)

# Example keymap (Modify this to match your actual key layout)
keymap = [
    [Keycode.Q, Keycode.W, Keycode.E, Keycode.R, Keycode.T, Keycode.Y, Keycode.U, Keycode.I, Keycode.O, Keycode.P, Keycode.A, Keycode.S, Keycode.D],
    [Keycode.F, Keycode.G, Keycode.H, Keycode.J, Keycode.K, Keycode.L, Keycode.Z, Keycode.X, Keycode.C, Keycode.V, Keycode.B, Keycode.N, Keycode.M],
    [Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE, Keycode.SIX, Keycode.SEVEN, Keycode.EIGHT, Keycode.NINE, Keycode.ZERO, Keycode.ENTER, Keycode.SPACE, Keycode.BACKSPACE],
    [Keycode.SHIFT, Keycode.CONTROL, Keycode.ALT, Keycode.GUI, Keycode.TAB, Keycode.ESCAPE, Keycode.DELETE, Keycode.HOME, Keycode.END, Keycode.PAGE_UP, Keycode.PAGE_DOWN, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW],
    [Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.F1, Keycode.F2, Keycode.F3, Keycode.F4, Keycode.F5, Keycode.F6, Keycode.F7, Keycode.F8, Keycode.F9, Keycode.F10, Keycode.F11]
]


def scan_matrix():
    for row_idx, row in enumerate(rows):
        row.value = True  # Activate row
        for col_idx, col in enumerate(cols):
            if not col.value:  # Key pressed (low state)
                kbd.press(keymap[row_idx][col_idx])
            else:
                kbd.release(keymap[row_idx][col_idx])
        row.value = False  # Deactivate row

while True:
    scan_matrix()
    time.sleep(0.01)













