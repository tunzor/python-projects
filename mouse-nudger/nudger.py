import pyautogui as pag
import time
import random

current_mouse_x, current_mouse_y = pag.position()

# Time to wait between nudging the mouse (in seconds)
time_to_wait = 1

# Lower and upper thresholds (in pixels) used to randomize movement
lower_threshold = -20
upper_threshold = 20

print(f"Mouse is at position {current_mouse_x}, {current_mouse_y}.")

while True:
    time.sleep(time_to_wait)
    move_x = random.randrange(lower_threshold, upper_threshold)
    move_y = random.randrange(lower_threshold, upper_threshold)
    pag.move(move_x, move_y)
    print(f"Moved mouse {move_x} units horizontally and {move_y} units vertically.")