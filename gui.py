import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import shutil

# set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# create a CTk window
window = ctk.CTk()
# Set window size to be 80% of user's monitor size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
width = int(screen_width * 0.6)
height = int(screen_height * 0.6)
x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(False, False)
window.title("Asion")

ctk.FontManager.load_font("gui/fonts/bbcb700.ttf")
bbcb_font = "Burbank Big Condensed"
label = ctk.CTkLabel(window, text="Asion", font=(bbcb_font, 150), text_color="white")
label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# create a function to open an image file
def open_image():
    filename = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.webp *.pfm *.sr *.ras")])
    filetype = filename.split(".")[-1]
    shutil.copy(filename, f"ml/input/input.{filetype}")
    print(filename)

# create a button to open an image file
button = ctk.CTkButton(window, text="Open Image", command=open_image, width=200, height=70, font=(bbcb_font, 30), text_color="white", hover_color="green", corner_radius=80)
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

window.mainloop()