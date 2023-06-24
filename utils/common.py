from utils.ui.displaySongFrame import displaySongFrame
from utils.audio import playSong
from utils.config import library
import tkinter as tk

def open_song_frame(song):
    displaySongFrame(song)
    print(song.title)
    playSong(song.path)

def truncate_text(text, length):
    if len(text) <= length:
        return text
    else:
        return text[:length] + "..."


def search_songs(search_query, inner_frame):
    songs = library.items('title:{}'.format(search_query))

    # Iterate over the matched items
    for song in songs:
        play_button = tk.Button(inner_frame, text=truncate_text(song.title, 40), command=lambda s=song: open_song_frame(s))
        play_button.pack()

def search(search_entry, search_var, inner_frame):
    search_query = search_entry.get()
    search_query = "time"
    search_type = search_var.get()

    if search_type == "Songs":
        search_songs(search_query, inner_frame)

    elif search_type == "Artists":
        items = library.items('artist:{}'.format(search_query))

        # Clear previous results
        for widget in inner_frame.winfo_children():
            widget.destroy()

        # Iterate over the matched items
        for item in items:
            title = item.title
            button = tk.Button(inner_frame, text=title)
            button.pack()

    elif search_type == "Albums":
        albums = library.albums(search_query)

        # Clear previous results
        for widget in inner_frame.winfo_children():
            widget.destroy()

        # Iterate over the matched items
        for album in albums:
            title = album.album
            button = tk.Button(inner_frame, text=title)
            button.pack()
     