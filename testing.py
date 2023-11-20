
import tkinter as tk
from tkinter import *
from tkinter import font

root = tk.Tk()
available_fonts = list(font.families())
for font_name in available_fonts:
    print(font_name)
root.destroy()