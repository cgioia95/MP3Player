from utils.ui import displaySongScreen
from utils.audio import playSong
from utils.config import library
import tkinter as tk



def openDisplayScreen( result_frame, header_row1, header_row2, song):
    displaySongScreen(result_frame, header_row1, header_row2, song)
    playSong(song.path)

def searchSongs(search_query, result_frame, header_row1, header_row2):
    songs = library.items('title:{}'.format(search_query))

    for widget in result_frame.winfo_children():
        widget.destroy()

    # Iterate over the matched items
    for song in songs: 
        play_button = tk.Button(result_frame, text=song.title, command=lambda path=song.path: openDisplayScreen(result_frame, header_row1, header_row2, song))
        play_button.pack()


def search(search_entry, search_var, result_frame, library, header_row1, header_row2):
    search_query = search_entry.get()
    search_type = search_var.get()

    if search_type == "Songs":
        searchSongs(search_query, result_frame, header_row1, header_row2)


    elif search_type == "Artists":
        items = library.items('artist:{}'.format(search_query))

        # Clear previous results
        for widget in result_frame.winfo_children():
            widget.destroy()

        # Iterate over the matched items
        for item in items:
            title = item.title
            button = tk.Button(result_frame, text=title)
            button.pack()

    elif search_type == "Albums":
        albums = library.albums(search_query)

        # Clear previous results
        for widget in result_frame.winfo_children():
            widget.destroy()

        # Iterate over the matched items
        for album in albums:
            title = album.album
            button = tk.Button(result_frame, text=title)
            button.pack()
     