import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# set up window - 60% of monitor size
window = ctk.CTk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = int(screen_width * 0.6)
height = int(screen_height * 0.6)
x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(False, False)
window.title("Asion - Input Image")

# load font - Kayak Sans Bold
ctk.FontManager.load_font("gui/fonts/ksb.otf")
ks = "Kayak Sans Bold"
label = ctk.CTkLabel(window, text="Asion", font=(ks, 150), text_color="white")
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# function to convert to jpg
def convert_to_jpg(file_path):
    window.config(cursor="wait")
    with Image.open(file_path) as im:
        im = im.convert("RGB")
        new_file_path = file_path.split(".")[0] + ".jpg"
        im.save("ml/input/input.png", "PNG", quality=20)
    return new_file_path

# create a function to open an image file
def open_image():
    filename = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.webp *.pfm *.sr *.ras")])
    if filename != "":
        convert_to_jpg(filename)
        if True:
            import result
            window.destroy()
            result.create_window()

open_button = ctk.CTkButton(window, text="Open Image", command=open_image, width=200, height=70, font=(ks, 35), text_color="white", hover_color="green", corner_radius=80)
open_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
continue_btn = ctk.CTkButton(window, text="Continue Without Image", command=open_image, width=100, height=35, font=(ks, 20), text_color="white", hover_color="green", corner_radius=40)
continue_btn.place(relx=0.5, rely=0.83, anchor=tk.CENTER)

window.mainloop()
