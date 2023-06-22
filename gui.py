import tkinter as tk
import beets.library
from tkinter import ttk
import pygame

pygame.mixer.init()

def play_audio(path):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def open_song_screen(song):

    result_frame.destroy()
    header_row1.destroy()
    header_row2.destroy()
    # Create a new window for the song screen
    # Create labels to display song information
    title_label = tk.Label(root, text="Title: {}".format(song.title))
    title_label.pack()

    artist_label = tk.Label(root, text="Artist: {}".format(song.artist))
    artist_label.pack()

    album_label = tk.Label(root, text="Album: {}".format(song.album))
    album_label.pack()



    play_audio(song.path)


# Load the Beets library
library = beets.library.Library('/Users/christian.gioia/Desktop/MP3/musiclibrary.db')

def search():
    search_query = search_entry.get()
    search_type = search_var.get()

    if search_type == "Songs":
        songs = library.items('title:{}'.format(search_query))

        # Clear previous results
        for widget in result_frame.winfo_children():
            widget.destroy()

        # Iterate over the matched items
        for song in songs: 
            play_button = tk.Button(result_frame, text=song.title, command=lambda path=song.path: open_song_screen(song))
            play_button.pack()

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

def update_button_styles():
    current_search_type = search_var.get()

    # Reset button styles
    songs_button.config(relief=tk.RAISED)
    artists_button.config(relief=tk.RAISED)
    albums_button.config(relief=tk.RAISED)

    # Set highlight for the current search type
    if current_search_type == "Songs":
        songs_button.config(relief=tk.SUNKEN)
    elif current_search_type == "Artists":
        artists_button.config(relief=tk.SUNKEN)
    elif current_search_type == "Albums":
        albums_button.config(relief=tk.SUNKEN)

root = tk.Tk()

root.geometry("400x400")

# Header - Row 1
header_row1 = tk.Frame(root)
header_row1.pack()

search_var = tk.StringVar()  # Variable to store the search type

songs_button = tk.Button(header_row1, text="Songs", command=lambda: (search_var.set("Songs"), update_button_styles()))
songs_button.pack(side=tk.LEFT)

artists_button = tk.Button(header_row1, text="Artists", command=lambda: (search_var.set("Artists"), update_button_styles()))
artists_button.pack(side=tk.LEFT)

albums_button = tk.Button(header_row1, text="Albums", command=lambda: (search_var.set("Albums"), update_button_styles()))
albums_button.pack(side=tk.LEFT)

# Header - Row 2
header_row2 = tk.Frame(root)
header_row2.pack()

search_entry = tk.Entry(header_row2)
search_entry.pack(side=tk.LEFT)

search_button = tk.Button(header_row2, text="Search", command=search)
search_button.pack(side=tk.LEFT)

# Result
result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True)


result_text = tk.Text(result_frame)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text.config(yscrollcommand=scrollbar.set)

# Initialize button styles
update_button_styles()

root.mainloop()
