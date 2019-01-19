#!usr/bin/env python

import tkinter as tk


def motion(event):
    print(f'({event.x}, {event.y})')


root = tk.Tk()

what_ever_you_do = "What ever you do will insegnificant, but is important that you do it.\n(Mahatam Gandhi)"

msg = tk.Message(
    root,
    text=what_ever_you_do
)
msg.config(
    bg='lightgreen',
    font=('times', 24, 'italic')
)
msg.bind('<Key>', motion)

msg.pack()

root.mainloop()
