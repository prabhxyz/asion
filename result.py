from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
import ml.process as process
import constellation_recognition as cr

threshold = 125
min_area = 25
blur = 5

def create_window():
    win = ctk.CTk()
    win._set_appearance_mode("dark")
    win.title("Asion - Constellation Recognition")
    win.resizable(False, False)
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    width = int(screen_width * 0.6)
    height = int(screen_height * 0.6)
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    win.geometry(f"{width}x{height}+{x-100}+{y}")

    # load fonts
    ctk.FontManager.load_font("gui/fonts/ksb.otf")
    ks = "Kayak Sans Bold"
    ctk.FontManager.load_font("gui/fonts/ksr.otf")
    ksr = "Kayak Sans Regular"
    ctk.FontManager.load_font("gui/fonts/ksl.otf")
    ksl = "Kayak Sans Light"

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

    def slider_th(value):
        global threshold
        threshold = round(value)
        txt_th.configure(text="Threshold: {}".format(threshold))
    def slider_ma(value):
        global min_area
        min_area = round(value)
        txt_ma.configure(text="Minimum Area: {}".format(min_area))
    def slider_blur(value):
        global blur
        blur = round(value)
        txt_bl.configure(text="Blur: {}".format(blur))

    # Threshold Slider
    txt_th = ctk.CTkLabel(win, text="Threshold: 125", font=(ksr, 25), text_color="white", bg_color="#2b2c30")
    txt_th.place(x=330, y=355, anchor="w")
    slider_1 = ctk.CTkSlider(master=win,command=slider_th, from_=-1, to=250, bg_color="#2b2c30")
    slider_1.pack(pady=5, padx=5)
    slider_1.place(relx=0.575, rely=0.75, anchor="e")
    slider_1.set(125)

    # Min Area Slider
    txt_ma = ctk.CTkLabel(win, text="Minimum Area: 25", font=(ksr, 25), text_color="white", bg_color="#2b2c30")
    txt_ma.place(x=610, y=355, anchor="w")
    slider_2 = ctk.CTkSlider(master=win,command=slider_ma, from_=-1, to=50, bg_color="#2b2c30")
    slider_2.pack(pady=5, padx=5)
    slider_2.place(relx=0.875, rely=0.75, anchor="e")
    slider_2.set(25)

    # Blur Slider
    txt_bl = ctk.CTkLabel(win, text="Blur: 5", font=(ksr, 25), text_color="white", bg_color="#2b2c30")
    txt_bl.place(x=335, y=435, anchor="w")
    slider_1 = ctk.CTkSlider(master=win,command=slider_blur, from_=0, to=10, bg_color="#2b2c30")
    slider_1.pack(pady=5, padx=5)
    slider_1.place(relx=0.575, rely=0.9, anchor="e")
    slider_1.set(5)

    # Constellation Section
    pre_const = ctk.CTkLabel(win, text="Prediction:", font=(ksr, 25), text_color="white", bg_color="#2b2c30")
    pre_const.place(x=330, y=88, anchor="w")
    pre = ctk.CTkLabel(win, text="-/-", font=(ksl, 25), text_color="white", bg_color="#2b2c30")
    pre.place(x=330, y=120, anchor="w")

    st_no = ctk.CTkLabel(win, text="No. of Stars:", font=(ksr, 25), text_color="white", bg_color="#2b2c30")
    st_no.place(x=630, y=88, anchor="w")
    st = ctk.CTkLabel(win, text="-/-", font=(ksl, 25), text_color="white", bg_color="#2b2c30")
    st.place(x=630, y=120, anchor="w")

    pre_const_l = ctk.CTkLabel(win, text="Other Predictions:", font=(ksr, 25), text_color="white", bg_color="#2b2c30")
    pre_const_l.place(x=330, y=170, anchor="w")
    other_l = ctk.CTkLabel(win, text="-/-", font=(ksl, 25), text_color="white", bg_color="#2b2c30", wraplength=500)
    other_l.place(x=330, y=202, anchor="nw")

    # Process Button
    img2 = None
    def button_callback():
        global img2
        new_parameters = f"threshold = {threshold}\nmin_area = {min_area}\nblur = {blur}"
        with open('data/parameters.py', 'w') as f:
            f.write(new_parameters)
        win.config(cursor="wait")
        process.process(threshold, min_area, blur)
        img2 = ImageTk.PhotoImage(Image.open("ml/input/temp/processed.jpg").resize((300, 300)))
        label2.configure(image=img2)
        data = cr.predict(threshold, min_area, blur)
        pre.configure(text=f"{data[0]}: {data[1]}%")
        other_l.configure(text=f"{data[3]}")
        st.configure(text=f"{data[2]}")
        win.config(cursor="")

    process_btn = ctk.CTkButton(master=win, command=button_callback, bg_color="#2b2c30", height=50, width=150, text="Process", font=(ks, 25), text_color="white", hover_color="green")
    process_btn.pack(pady=10, padx=10)
    process_btn.place(x=635, y=450, anchor="w")

    # Reset The Image to Placeholder Image
    img2 = ImageTk.PhotoImage(Image.open("gui/imgs/placeholder.jpg").resize((300, 300)))
    label2.configure(image=img2)

    win.mainloop()

if __name__ == '__main__':
    create_window()