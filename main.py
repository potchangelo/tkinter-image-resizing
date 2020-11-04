import tkinter as tk
from tkinter import filedialog as fd
import image as im

class App:
    def __init__(self):
        # - Properties
        self.window = None
        self.image_original = None
        self.image_tk = None
        self.label_image = None
        self.entry_width_list = []

        # - Create app
        self.create_window()
        self.create_left_frame()
        self.create_right_frame()
        self.run()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title('Image Resizing')
        self.window.config(bg='white')
        self.window.minsize(width=900, height=640)
        self.window.rowconfigure(index=0, weight=1)
        self.window.columnconfigure(index=0, weight=1)
        self.window.columnconfigure(index=1, minsize=300)

    def create_left_frame(self):
        # - Frame
        frame_left = tk.Frame(master=self.window, bg='#4F4F4F')
        frame_left.grid(row=0, column=0, sticky=tk.NSEW)
        frame_left.rowconfigure(index=1, minsize=500, weight=1)
        frame_left.columnconfigure(index=0, weight=1)

        # - Label
        label_title = tk.Label(master=frame_left, text='Original image', fg='white', bg='#363636')
        label_title.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10, ipady=10)

        # - Image
        self.label_image = tk.Label(master=frame_left, bg='#4F4F4F')
        self.label_image.grid(row=1, column=0)

        # - Button
        button = tk.Button(master=frame_left, text='Choose image', command=self.open_image)
        button.grid(row=2, column=0, padx=10, pady=15, ipadx=10, ipady=5)

    def create_right_frame(self):
        # - Frame
        frame_right = tk.Frame(master=self.window, bg='#FFFFFF')
        frame_right.grid(row=0, column=1, sticky=tk.NSEW)
        frame_right.rowconfigure(index=1, minsize=300, weight=1)
        frame_right.columnconfigure(index=0, weight=1)

        # - Label
        label_title = tk.Label(master=frame_right, text='Resizing images', bg='#E6E6E6')
        label_title.grid(row=0, column=0, sticky=tk.NSEW, ipadx=10, ipady=10)

        # - Fields
        frame_fields = tk.Frame(master=frame_right, bg='#FFFFFF')
        frame_fields.grid(row=1, column=0, sticky=tk.N + tk.E + tk.W, padx=10, pady=20)
        frame_fields.columnconfigure(index=1, weight=1)
        for i, value in enumerate((128, 256, 512)):
            label_width = tk.Label(master=frame_fields, text='Width {}'.format(i + 1), bg='#FFFFFF')
            label_width.grid(row=i, column=0, pady=(0, 20))

            entry_width = tk.Entry(master=frame_fields)
            entry_width.insert(0, str(value))
            entry_width.grid(row=i, column=1, padx=5, pady=(0, 20), sticky=tk.NSEW)
            self.entry_width_list.append(entry_width)

            label_px = tk.Label(master=frame_fields, text='px', bg='#FFFFFF')
            label_px.grid(row=i, column=2, pady=(0, 20))

        # - Button
        button = tk.Button(master=frame_right, text='Export images', command=self.save_image)
        button.grid(row=2, column=0, padx=10, pady=15, ipadx=10, ipady=5)

    def open_image(self):
        filename = fd.askopenfilename(filetypes=(('image files', '*.png *.jpg'),))
        if len(filename) == 0:
            return

        self.image_original, self.image_tk = im.image_open(filename)
        self.label_image.config(image=self.image_tk)
        self.label_image.image = self.image_tk

    def save_image(self):
        if self.image_original is None:
            return

        directory = fd.askdirectory()
        if len(directory) == 0:
            return

        width_list = (entry.get() for entry in self.entry_width_list)
        im.image_save(self.image_original, directory, width_list)

    def run(self):
        self.window.mainloop()

App()