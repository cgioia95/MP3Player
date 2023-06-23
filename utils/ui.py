import tkinter as tk
from utils.config import songFrame, updateCurrentFrame

def displaySongScreen(song):

    updateCurrentFrame(songFrame)

    title_label = tk.Label(songFrame, text="Title: {}".format(song.title))
    title_label.pack()

    artist_label = tk.Label(songFrame, text="Artist: {}".format(song.artist))
    artist_label.pack()

    album_label = tk.Label(songFrame, text="Album: {}".format(song.album))
    album_label.pack()
