
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

while True:
    for row in rows:
        row.value = True  # Activate current row
        
        for col in cols:
            if not col.value:  # If column goes LOW, a switch is pressed
                print("1")  # Output 1
                
        row.value = False  # Deactivate row
    
    time.sleep(0.01)  # Small delay to prevent excessive output

