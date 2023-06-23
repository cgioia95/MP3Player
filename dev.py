from tkinter import *

def configure_scrollregion(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
frame = Frame(root, width=50, height=300)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg='#FFFFFF', width=300, height=300)
canvas.pack(side=LEFT, expand=True, fill=BOTH)

bar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
bar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=bar.set)

frame_inner = Frame(canvas)
frame_inner.bind("<Configure>", configure_scrollregion)

for _ in range(10):
    Button(frame_inner, text=str(_)).grid(row=_)

canvas.create_window(0, 0, anchor='nw', window=frame_inner)

root.mainloop()
