
import tkinter as tk
import beets.library
import pygame

audio = pygame.mixer.init()
library = beets.library.Library('/Users/christian.gioia/Desktop/MP3/musiclibrary.db')

root = tk.Tk()
root.geometry("400x400")

searchFrame = tk.Frame(root)
songFrame = tk.Frame(root)

currentFrame = searchFrame

def updateCurrentFrame(newFrame):
    global currentFrame
    currentFrame.pack_forget()
    currentFrame = newFrame
    currentFrame.pack()
