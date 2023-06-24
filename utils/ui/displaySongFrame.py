import tkinter as tk
from tkinter import ttk
from utils.config import songFrame, updateCurrentFrame, searchFrame
from utils.audio import togglePlay, getSongProgress, teardown

def pause_handler(event):
    togglePlay()

def searchHandler(event):
    teardown()
    updateCurrentFrame(searchFrame)

def convert_seconds_to_mp3_time(seconds):
    minutes = round(seconds) // 60
    seconds = round(seconds) % 60
    return f"{minutes}:{seconds:02d}"

def update_progress(progress_bar, label_text):
    # Get the current progress of the song

    current_position, songLength, progress = getSongProgress()

    curr = convert_seconds_to_mp3_time(current_position)
    length = convert_seconds_to_mp3_time(songLength)

    if(songLength > 0):
        label_text.set(curr + " / " + length)

    # Update the progress bar value
    progress_bar["value"] = progress

    # Schedule the next update after 100 milliseconds
    progress_bar.after(1000, lambda: update_progress(progress_bar, label_text))

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

    label_text = tk.StringVar()

    progress_label = ttk.Label(songFrame, textvariable=label_text)
    progress_label.pack()

    # Bind the key handler to the space bar
    songFrame.bind("<space>", pause_handler)
    songFrame.bind("<BackSpace>", searchHandler)
    songFrame.focus_set()  # Set focus to the frame to receive key events

    updateCurrentFrame(songFrame)

    update_progress(progress_bar, label_text)

