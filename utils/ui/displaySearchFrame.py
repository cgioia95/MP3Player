import tkinter as tk
from tkinter import ttk
from utils.config import updateCurrentFrame, searchFrame, library
from utils.common import search



def displaySearchFrame():
    # Header - Row 1 - Song | Artist | Album buttons
    header_row1 = tk.Frame(searchFrame)
    header_row1.pack()

    search_var = tk.StringVar()

    songs_button = tk.Button(header_row1, text="Songs", command=lambda: (search_var.set("Songs")))
    songs_button.pack(side=tk.LEFT)

    artists_button = tk.Button(header_row1, text="Artists", command=lambda: (search_var.set("Artists")))
    artists_button.pack(side=tk.LEFT)

    albums_button = tk.Button(header_row1, text="Albums", command=lambda: (search_var.set("Albums")))
    albums_button.pack(side=tk.LEFT)

    # Header - Row 2 - Search Bar
    header_row2 = tk.Frame(searchFrame)
    header_row2.pack()

    search_entry = tk.Entry(header_row2)
    search_entry.pack(side=tk.LEFT)

    result_frame = tk.Frame(searchFrame)


    # Results
    result_frame.pack(fill=tk.BOTH, expand=True)
    canvas=tk.Canvas(result_frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,50,500))
    canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    bar = tk.Scrollbar(result_frame, orient=tk.VERTICAL, command=canvas.yview)
    bar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=bar.set)
    frame_inner = tk.Frame(canvas)

    def configure_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_inner.bind("<Configure>", configure_scrollregion)

    canvas.create_window(0, 0, anchor='nw', window=frame_inner)

    search_button = tk.Button(header_row2, text="Search", command=lambda: search(search_entry, search_var, frame_inner))

    search_button.pack(side=tk.LEFT)

    updateCurrentFrame(searchFrame)
