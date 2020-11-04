import tkinter as tk

# - Window
window = tk.Tk()
window.title('Image Resizing')
window.config(bg='white')
window.minsize(width=900, height=640)
window.rowconfigure(index=0, weight=1)
window.columnconfigure(index=0, weight=1)
window.columnconfigure(index=1, minsize=300)

# - Left Frame
frame_left = tk.Frame(master=window, bg='#4F4F4F')
frame_left.grid(row=0, column=0, sticky=tk.NSEW)
frame_left.rowconfigure(index=1, minsize=500, weight=1)
frame_left.columnconfigure(index=0, weight=1)

# --- Label
label_title = tk.Label(master=frame_left, text='Original image', fg='white', bg='#363636')
label_title.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10, ipady=10)

# --- Image
label_image = tk.Label(master=frame_left, bg='#4F4F4F')
label_image.grid(row=1, column=0)

# --- Button
button = tk.Button(master=frame_left, text='Choose image')
button.grid(row=2, column=0, padx=10, pady=15, ipadx=10, ipady=5)

# - Right Frame
frame_right = tk.Frame(master=window, bg='#FFFFFF')
frame_right.grid(row=0, column=1, sticky=tk.NSEW)
frame_right.rowconfigure(index=1, minsize=300, weight=1)
frame_right.columnconfigure(index=0, weight=1)

# --- Label
label_title = tk.Label(master=frame_right, text='Resizing images', bg='#E6E6E6')
label_title.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10, ipady=10)

# --- Fields
frame_fields = tk.Frame(master=frame_right, bg='#FFFFFF')
frame_fields.grid(row=1, column=0, sticky=tk.N+tk.E+tk.W, padx=10, pady=20)
frame_fields.columnconfigure(index=1, weight=1)
for i, value in enumerate((128, 256, 512)):
    label_width = tk.Label(master=frame_fields, text='Width {}'.format(i + 1), bg='#FFFFFF')
    label_width.grid(row=i, column=0, pady=(0, 20))

    entry_width = tk.Entry(master=frame_fields)
    entry_width.insert(0, str(value))
    entry_width.grid(row=i, column=1, padx=5, pady=(0, 20), sticky=tk.NSEW)

    label_px = tk.Label(master=frame_fields, text='px', bg='#FFFFFF')
    label_px.grid(row=i, column=2, pady=(0, 20))

# --- Button
button = tk.Button(master=frame_right, text='Export images')
button.grid(row=2, column=0, padx=10, pady=15, ipadx=10, ipady=5)

# - Run
window.mainloop()