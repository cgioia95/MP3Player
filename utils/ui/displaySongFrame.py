import tkinter as tk
from tkinter import ttk
from utils.config import songFrame, updateCurrentFrame
from utils.audio import togglePlay, getSongProgress

def key_handler(event):
    if event.keysym == 'space':
        togglePlay()

def update_progress(progress_bar):
    # Get the current progress of the song
    progress = getSongProgress()

    # Update the progress bar value
    progress_bar["value"] = progress

    # Schedule the next update after 100 milliseconds
    progress_bar.after(100, lambda: update_progress(progress_bar))


def displaySongFrame(song):
    title_label = tk.Label(songFrame, text="Title: {}".format(song.title))
    title_label.pack()

    artist_label = tk.Label(songFrame, text="Artist: {}".format(song.artist))
    artist_label.pack()

    album_label = tk.Label(songFrame, text="Album: {}".format(song.album))
    album_label.pack()

    # Create a progress bar
    progress_bar = ttk.Progressbar(songFrame, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack()

    # Bind the key handler to the space bar
    songFrame.bind("<space>", key_handler)
    songFrame.focus_set()  # Set focus to the frame to receive key events

    updateCurrentFrame(songFrame)

        # Update the progress bar periodically
    update_progress(progress_bar)

