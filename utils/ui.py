import tkinter as tk
from utils.config import root

def displaySongScreen(result_frame, header_row1, header_row2, song):
    result_frame.destroy()
    header_row1.destroy()
    header_row2.destroy()

    title_label = tk.Label(root, text="Title: {}".format(song.title))
    title_label.pack()

    artist_label = tk.Label(root, text="Artist: {}".format(song.artist))
    artist_label.pack()

    album_label = tk.Label(root, text="Album: {}".format(song.album))
    album_label.pack()