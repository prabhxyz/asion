import tkinter as tk
import customtkinter as ctk
import precise_time_constellation as ptc
import time_constellation as tc
from tkinter import messagebox
import threading

def create_window():
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
    win.geometry(f"{width}x{height}+{x+100}+{y}")

    # load fonts
    ctk.FontManager.load_font("gui/fonts/ksb.otf")
    ks = "Kayak Sans Bold"
    ctk.FontManager.load_font("gui/fonts/ksr.otf")
    ksr = "Kayak Sans Regular"
    ctk.FontManager.load_font("gui/fonts/ksl.otf")
    ksl = "Kayak Sans Light"

    # Window UI Components
    canvas = ctk.CTkCanvas(master=win, width=800, height=800, background="#2b2c30", highlightthickness=0)
    canvas.pack(anchor="center")

    # Input
    txt_output = ctk.CTkLabel(win, text="Input", font=(ks, 80), text_color="white", bg_color="#2b2c30")
    txt_output.place(relx=0.5, rely=0.10, anchor="center")

    # Text boxes
    con_label = tk.Label(win, text="Constellation:", font=(ksr, 18), fg="white", bg="#2b2c30")
    con_label.place(x=440, y=150, anchor="e")
    con = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#5e6069", borderwidth=0)
    con.place(relx=0.5, y=150, anchor="center")

    date_label = tk.Label(win, text="Date (MM/DD/YY):", font=(ksr, 18), fg="white", bg="#2b2c30")
    date_label.place(x=440, y=200, anchor="e")
    date = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#5e6069", borderwidth=0)
    date.place(relx=0.5, y=200, anchor="center")

    time_label = tk.Label(win, text="Time (HH:MM:SS):", font=(ksr, 18), fg="white", bg="#2b2c30")
    time_label.place(x=440, y=250, anchor="e")
    time_txt = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#5e6069", borderwidth=0)
    time_txt.place(relx=0.5, y=250, anchor="center")

    accuracy_label = tk.Label(win, text="Accuracy (1-10):", font=(ksr, 18), fg="white", bg="#2b2c30")
    accuracy_label.place(x=440, y=300, anchor="e")
    accuracy = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#5e6069", borderwidth=0)
    accuracy.place(relx=0.5, y=300, anchor="center")

    min_al = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#3e3f45", borderwidth=0)
    min_al.place(relx=0.5, y=350, anchor="center")

    max_al = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#3e3f45", borderwidth=0)
    max_al.place(relx=0.5, y=400, anchor="center")

    min_az = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#3e3f45", borderwidth=0)
    min_az.place(relx=0.5, y=450, anchor="center")

    max_az = tk.Text(win, height=1, width=20, wrap="none", font=(ksr, 18), fg="white", bg="#3e3f45", borderwidth=0)
    max_az.place(relx=0.5, y=500, anchor="center")

    min_al_label = tk.Label(win, text="Min Altitude (0-90):", font=(ksr, 18), fg="white", bg="#2b2c30")
    min_al_label.place(x=440, y=350, anchor="e")

    max_al_label = tk.Label(win, text="Max Altitude (0-90):", font=(ksr, 18), fg="white", bg="#2b2c30")
    max_al_label.place(x=440, y=400, anchor="e")

    min_az_label = tk.Label(win, text="Min Azimuth (0-360):", font=(ksr, 18), fg="white", bg="#2b2c30")
    min_az_label.place(x=440, y=450, anchor="e")

    max_az_label = tk.Label(win, text="Max Azimuth (0-360):", font=(ksr, 18), fg="white", bg="#2b2c30")
    max_az_label.place(x=440, y=500, anchor="e")

    def open_first():
        open_html(con.get("1.0", "end-1c"), date.get("1.0", "end-1c"), time_txt.get("1.0", "end-1c"),
                accuracy.get("1.0", "end-1c"), min_al.get("1.0", "end-1c"), max_al.get("1.0", "end-1c"),
                min_az.get("1.0", "end-1c"), max_az.get("1.0", "end-1c"))
    def open_html(t_constellation, t_date, t_time, t_accuracy, t_min_al, t_max_al, t_min_az, t_max_az):
        open_btn.configure(state="disabled", text="Please wait...")
        if t_constellation == "" or t_date == "" or t_time == "" or t_accuracy == "":
            messagebox.showerror("Error", "Please fill out all required fields.")
        else:
            if t_min_al == "" or t_max_al == "" or t_min_az == "" or t_max_az == "":
                def run_function():
                    tc.t_constellation(t_constellation, t_accuracy, t_date, t_time)
                t = threading.Thread(target=run_function)
                t.start()
            elif min_al != "" and max_al != "" and min_az != "" and max_az != "":
                def run_function():
                    ptc.p_constellation(t_constellation, t_accuracy, t_max_al, t_min_al, t_max_az, t_min_az, t_date, t_time)
                t = threading.Thread(target=run_function)
                t.start()
        open_btn.configure(state="normal", text="Open Map")

    open_btn = ctk.CTkButton(win, text="Open Map", command=open_first, width=100, height=35, font=(ks, 20),
                                 text_color="white", hover_color="green", corner_radius=40, bg_color="#2b2c30")
    open_btn.place(relx=0.5, y=450, anchor="center")

    win.mainloop()

if __name__ == "__main__":
    create_window()