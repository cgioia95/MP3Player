import tkinter as tk

print ("Booting up GUI")

def search():
    search_query = search_entry.get()

root = tk.Tk()

# Header - Row 1
header_row1 = tk.Frame(root)
header_row1.pack()

songs_button = tk.Button(header_row1, text="Songs")
songs_button.pack(side=tk.LEFT)

artists_button = tk.Button(header_row1, text="Artists")
artists_button.pack(side=tk.LEFT)

albums_button = tk.Button(header_row1, text="Albums")
albums_button.pack(side=tk.LEFT)

# Header - Row 2
header_row2 = tk.Frame(root)
header_row2.pack()

search_entry = tk.Entry(header_row2)
search_entry.pack(side=tk.LEFT)

search_button = tk.Button(header_row2, text="Search", command=search)
search_button.pack(side=tk.LEFT)


root.mainloop()