import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox

from noiseforge.generator import generatenoise
from noiseforge.preview import previewimage
from noiseforge.pngwriter import savepng


currentpixels = None
currentwidth = 0
currentheight = 0


root = tk.Tk()

root.title("NoiseForge Alpha 0.0.2")

root.geometry("700x520")

root.resizable(False, False)


mainframe = tk.Frame(root)

mainframe.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


controlframe = tk.Frame(mainframe)

controlframe.pack(
    side="left",
    fill="y",
    padx=15,
    pady=15
)


previewframe = tk.Frame(mainframe)

previewframe.pack(
    side="right",
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


previewcanvas = tk.Canvas(
    previewframe,
    bg="black",
    width=512,
    height=512,
    highlightthickness=0
)

previewcanvas.pack(
    fill="both",
    expand=True
)


# Seed

seedlabel = tk.Label(
    controlframe,
    text="Seed"
)

seedlabel.pack(anchor="w")

seedentry = tk.Entry(controlframe)

seedentry.insert(0, "1234")

seedentry.pack(fill="x", pady=4)


# Width

widthlabel = tk.Label(
    controlframe,
    text="Width"
)

widthlabel.pack(anchor="w")

widthentry = tk.Entry(controlframe)

widthentry.insert(0, "512")

widthentry.pack(fill="x", pady=4)


# Height

heightlabel = tk.Label(
    controlframe,
    text="Height"
)

heightlabel.pack(anchor="w")

heightentry = tk.Entry(controlframe)

heightentry.insert(0, "512")

heightentry.pack(fill="x", pady=4)


# Lowest Point

minlabel = tk.Label(
    controlframe,
    text="Lowest Point"
)

minlabel.pack(anchor="w")

minentry = tk.Entry(controlframe)

minentry.insert(0, "0")

minentry.pack(fill="x", pady=4)


# Highest Point

maxlabel = tk.Label(
    controlframe,
    text="Highest Point"
)

maxlabel.pack(anchor="w")

maxentry = tk.Entry(controlframe)

maxentry.insert(0, "255")

maxentry.pack(fill="x", pady=4)


# Repeatable

repeatvar = tk.BooleanVar()

repeatcheck = tk.Checkbutton(
    controlframe,
    text="Repeatable Pattern",
    variable=repeatvar
)

repeatcheck.pack(anchor="w", pady=10)


# Noise Mode

modelabel = tk.Label(
    controlframe,
    text="Noise Mode"
)

modelabel.pack(anchor="w")

modevar = tk.StringVar(value="static")

modemenu = tk.OptionMenu(
    controlframe,
    modevar,
    "static",
    "smooth",
    "grid",
    "cloud"
)

modemenu.pack(fill="x", pady=4)


def generateimage():

    global currentpixels
    global currentwidth
    global currentheight

    try:

        seed = int(seedentry.get())

        width = int(widthentry.get())
        height = int(heightentry.get())

        minval = int(minentry.get())
        maxval = int(maxentry.get())

        repeat = repeatvar.get()

        mode = modevar.get()

        pixels = generatenoise(
            seed=seed,
            width=width,
            height=height,
            minval=minval,
            maxval=maxval,
            repeat=repeat,
            mode=mode
        )

        currentpixels = pixels
        currentwidth = width
        currentheight = height

        image = previewimage(
            width,
            height,
            pixels
        )

        previewcanvas.delete("all")
        
        previewcanvas.create_image(
            256,
            256,
            image=image,
            anchor="center"
        )
        
        previewcanvas.image = image

    except Exception as error:

        messagebox.showerror(
            "NoiseForge",
            str(error)
        )


def saveimage():

    global currentpixels

    if currentpixels is None:

        messagebox.showwarning(
            "NoiseForge",
            "Generate an image first."
        )

        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG Files", "*.png")
        ]
    )

    if filepath:

        savepng(
            filepath,
            currentwidth,
            currentheight,
            currentpixels
        )

        messagebox.showinfo(
            "NoiseForge",
            "PNG exported successfully."
        )


generatebutton = tk.Button(
    controlframe,
    text="Generate Preview",
    command=generateimage,
    height=2
)

generatebutton.pack(
    fill="x",
    pady=10
)


savebutton = tk.Button(
    controlframe,
    text="Export PNG",
    command=saveimage,
    height=2
)

savebutton.pack(
    fill="x",
    pady=4
)


def run():
    root.mainloop()
