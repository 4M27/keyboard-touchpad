from pynput import keyboard, mouse
import tkinter as tk

# --- Get screen resolution ---
root = tk.Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.destroy()

m = mouse.Controller()

# --- Keyboard layout (exclude Esc) ---
layout = [
    "1234567890",
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./",
    " "
]

def key_to_position(char):
    char = char.lower()
    for row_index, row in enumerate(layout):
        if char in row:
            col_index = row.index(char)
            cols = len(row)
            x = int((col_index + 0.5) / cols * screen_w)
            y = int((row_index + 0.5) / len(layout) * screen_h)
            return (x, y)
    return None

def on_press(key):
    try:
        k = key.char.lower()
        pos = key_to_position(k)
        if pos:
            m.position = pos  # move real OS cursor
    except AttributeError:
        # ignore Esc + other special keys
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
