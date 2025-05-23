import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.D10,
    board.MOSI,
    board.MISO,
    board.SCK,
    board.A0,
    board.A1,
    board.A2,
    board.A3,
    board.D9,
    board.D8,
    board.D7,
    board.D6,
    board.D5,
)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.GRAVE,
        KC.N1,
        KC.N2,
        KC.N3,
        KC.N4,
        KC.N5,
        KC.N6,
        KC.N7,
        KC.N8,
        KC.N9,
        KC.N0,
        KC.MINUS,
        KC.EQUAL,
        KC.TAB,
        KC.Q,
        KC.W,
        KC.E,
        KC.R,
        KC.T,
        KC.Y,
        KC.U,
        KC.I,
        KC.O,
        KC.P,
        KC.LBRC,
        KC.BACKSPACE,
        KC.CAPS,
        KC.A,
        KC.S,
        KC.D,
        KC.F,
        KC.G,
        KC.H,
        KC.J,
        KC.K,
        KC.L,
        KC.SCLN,
        KC.QUOT,
        KC.RBRC,
        KC.LSFT,
        KC.Z,
        KC.X,
        KC.C,
        KC.V,
        KC.B,
        KC.N,
        KC.M,
        KC.COMM,
        KC.DOT,
        KC.SLSH,
        KC.RSFT,
        KC.BSLS,
        KC.LCTL,
        KC.LGUI,
        KC.LALT,
        KC.SPC,
        KC.RALT,
        KC.RGUI,
        KC.NO,
        KC.RCTL,
        KC.NO,
        KC.NO,
        KC.ENTER,
        KC.ENTER,
    ],
]

if __name__ == "__main__":
    keyboard.go()














