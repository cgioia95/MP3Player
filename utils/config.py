
import tkinter as tk
import beets.library
from tkinter import ttk
import pygame

audio = pygame.mixer.init()
library = beets.library.Library('/Users/christian.gioia/Desktop/MP3/musiclibrary.db')
root = tk.Tk()
