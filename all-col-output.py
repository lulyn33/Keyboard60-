
import board
import digitalio
import time

# 🛠 Define row and column pins (Modify based on your PCB wiring)
row_pins = [board.D0, board.D1, board.D2, board.D3, board.D4]  # Update as needed
col_pins = [
    board.D10, board.MOSI, board.MISO, board.SCK, 
    board.A0, board.A1, board.A2, board.A3, 
    board.D9, board.D8, board.D7, board.D6, board.D5
]  # Update as needed

# 🔵 Set up rows as OUTPUTS (default LOW)
rows = []
for pin in row_pins:
    row = digitalio.DigitalInOut(pin)
    row.direction = digitalio.Direction.OUTPUT
    row.value = False  # Default LOW
    rows.append(row)

# 🟢 Set up columns as INPUTS with PULL-UP resistors (default HIGH)
cols = []
for pin in col_pins:
    col = digitalio.DigitalInOut(pin)
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.UP  # Default HIGH
    cols.append(col)

# 🗝 Define the keymap with characters (Modify this keymap according to your layout)
keymap = [
    ['Esc', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],  # Row 0: Esc, 1-0, -, =, Backspace
    ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],        # Row 1: Tab, Q-P, [, ], \
    ['CapsLock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],     # Row 2: CapsLock, A-L, ;, ', Enter
    ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],              # Row 3: Shift, Z-/, Shift
    ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Win', 'Menu', 'Ctrl']                      # Row 4: Ctrl, Win, Alt, Space, Alt, Win, Menu, Ctrl
]

# Variable to store the last pressed key state (for debouncing)
last_key_state = {}

while True:
    for row_idx, row in enumerate(rows):
        row.value = True  # Activate current row
        
        for col_idx, col in enumerate(cols):
            if not col.value:  # If column goes LOW, key is pressed
                key = keymap[row_idx][col_idx]  # Get the character from the keymap
                
                # Check if the key was previously released (key press event)
                if (row_idx, col_idx) not in last_key_state or last_key_state[(row_idx, col_idx)] == 'released':
                    print(f"Key Pressed: Row {row_idx}, Col {col_idx}, Key {key}")
                    last_key_state[(row_idx, col_idx)] = 'pressed'  # Mark key as pressed
                
            else:
                # If key is released, update the state
                if (row_idx, col_idx) in last_key_state and last_key_state[(row_idx, col_idx)] == 'pressed':
                    last_key_state[(row_idx, col_idx)] = 'released'  # Mark key as released
                
        row.value = False  # Deactivate row
    
    time.sleep(0.01)  # Small delay to reduce output spam

