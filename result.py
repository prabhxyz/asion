from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
import ml.process as process
from data.parameters import *

def create_window():
    process.process(threshold, min_area)
    win = ctk.CTk()
    win._set_appearance_mode("dark")
    win.title("Asion - Input Analysis")
    win.resizable(False, False)
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    width = int(screen_width * 0.6)
    height = int(screen_height * 0.6)
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

    # load font - Kayak Sans Bold
    ctk.FontManager.load_font("gui/fonts/ksb.otf")
    ks = "Kayak Sans Bold"

    # Images - Input and Processed
    frame = Frame(win, width=400, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.18, rely=0.265)
    frame2 = Frame(win, width=400, height=400)
    frame2.pack()
    frame2.place(anchor='center', relx=0.18, rely=0.73)

    img = ImageTk.PhotoImage(Image.open("ml/input/image.png").resize((300, 300)))
    img2 = ImageTk.PhotoImage(Image.open("gui/imgs/placeholder.jpg").resize((300, 300)))
    label = Label(frame, image=img)
    label2 = Label(frame2, image=img2)
    label.pack()
    label2.pack()

    # Window UI Components
    canvas = ctk.CTkCanvas(master=win, width=750, height=800, background="#2b2c30", highlightthickness=0)
    canvas.pack(side="right")

    txt_output = ctk.CTkLabel(win, text="Observation Summary", font=(ks, 35), text_color="white", bg_color="#2b2c30")
    txt_output.place(relx=0.71, rely=0.07, anchor="e")

    txt_process = ctk.CTkLabel(win, text="Processing Parameters", font=(ks, 35), text_color="white", bg_color="#2b2c30")
    txt_process.place(relx=0.72, rely=0.58, anchor="e")

    win.mainloop()

if __name__ == '__main__':
    create_window()
