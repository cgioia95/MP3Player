import tkinter as tk
from tkinter import ttk
from utils.common import search
from utils.config import library, root, audio

root.geometry("400x400")

header_row1 = tk.Frame(root)
header_row1.pack()

search_var = tk.StringVar()

songs_button = tk.Button(header_row1, text="Songs", command=lambda: (search_var.set("Songs")))
songs_button.pack(side=tk.LEFT)

artists_button = tk.Button(header_row1, text="Artists", command=lambda: (search_var.set("Artists")))
artists_button.pack(side=tk.LEFT)

albums_button = tk.Button(header_row1, text="Albums", command=lambda: (search_var.set("Albums")))
albums_button.pack(side=tk.LEFT)

# Header - Row 2
header_row2 = tk.Frame(root)
header_row2.pack()

search_entry = tk.Entry(header_row2)
search_entry.pack(side=tk.LEFT)

result_frame = tk.Frame(root)


search_button = tk.Button(header_row2, text="Search", command=lambda: search(search_entry, search_var, result_frame, library, header_row1, header_row2))
search_button.pack(side=tk.LEFT)

# Result
result_frame.pack(fill=tk.BOTH, expand=True)


result_text = tk.Text(result_frame)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
