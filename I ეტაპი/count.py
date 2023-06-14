import tkinter as tk

def on_change(event):
    user_input = entry.get()
    length_label.config(text="Length: " + str(len(user_input)))

window = tk.Tk()

label = tk.Label(window, text="Enter your input:")
label.pack()

entry = tk.Entry(window)
entry.pack()
entry.bind("<KeyRelease>", on_change)

length_label = tk.Label(window, text="Length: 0")
length_label.pack()

window.mainloop()