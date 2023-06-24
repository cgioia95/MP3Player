import tkinter as tk
from utils.config import songFrame, updateCurrentFrame
from utils.audio import togglePlay

def key_handler(event):
    if event.keysym == 'space':
        togglePlay()

def displaySongFrame(song):
    title_label = tk.Label(songFrame, text="Title: {}".format(song.title))
    title_label.pack()

    artist_label = tk.Label(songFrame, text="Artist: {}".format(song.artist))
    artist_label.pack()

    album_label = tk.Label(songFrame, text="Album: {}".format(song.album))
    album_label.pack()

    # Bind the key handler to the space bar
    songFrame.bind("<space>", key_handler)
    songFrame.focus_set()  # Set focus to the frame to receive key events

    updateCurrentFrame(songFrame)
