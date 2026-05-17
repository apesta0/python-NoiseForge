import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox

from noiseforge.generator import generatenoise
from noiseforge.pngwriter import savepng

from noiseforge.config import (
    DEFAULT_WIDTH,
    DEFAULT_HEIGHT,
    DEFAULT_MIN,
    DEFAULT_MAX,
    DEFAULT_SEED
)


def generateimage():

    try:

        seed = int(seedentry.get())

        width = int(widthentry.get())
        height = int(heightentry.get())

        minval = int(minentry.get())
        maxval = int(maxentry.get())

        repeat = repeatvar.get()

        pixels = generatenoise(
            seed=seed,
            width=width,
            height=height,
            minval=minval,
            maxval=maxval,
            repeat=repeat
        )

        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Files", "*.png")
            ]
        )

        if filepath:

            savepng(
                filepath,
                width,
                height,
                pixels
            )

            messagebox.showinfo(
                "NoiseForge",
                "Image exported successfully."
            )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )


root = tk.Tk()

root.title("NoiseForge")

root.geometry("350x320")

root.resizable(False, False)


tk.Label(root, text="Seed").pack()

seedentry = tk.Entry(root)
seedentry.insert(0, str(DEFAULT_SEED))
seedentry.pack()


tk.Label(root, text="Width").pack()

widthentry = tk.Entry(root)
widthentry.insert(0, str(DEFAULT_WIDTH))
widthentry.pack()


tk.Label(root, text="Height").pack()

heightentry = tk.Entry(root)
heightentry.insert(0, str(DEFAULT_HEIGHT))
heightentry.pack()


tk.Label(
    root,
    text="Lowest Point (White)"
).pack()

minentry = tk.Entry(root)
minentry.insert(0, str(DEFAULT_MIN))
minentry.pack()


tk.Label(
    root,
    text="Highest Point (Black)"
).pack()

maxentry = tk.Entry(root)
maxentry.insert(0, str(DEFAULT_MAX))
maxentry.pack()


repeatvar = tk.BooleanVar()

repeatcheck = tk.Checkbutton(
    root,
    text="Repeatable Pattern",
    variable=repeatvar
)

repeatcheck.pack(pady=10)


generatebutton = tk.Button(
    root,
    text="Generate PNG",
    command=generateimage
)

generatebutton.pack(pady=15)


def run():
    root.mainloop()
