import tkinter as tk
from utils.config import songFrame, updateCurrentFrame

def displaySongFrame(song):
    title_label = tk.Label(songFrame, text="Title: {}".format(song.title))
    title_label.pack()

    artist_label = tk.Label(songFrame, text="Artist: {}".format(song.artist))
    artist_label.pack()

    album_label = tk.Label(songFrame, text="Album: {}".format(song.album))
    album_label.pack()

    updateCurrentFrame(songFrame)
