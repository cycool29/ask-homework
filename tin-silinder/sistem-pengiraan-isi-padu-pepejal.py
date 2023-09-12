import tkinter as tk
from PIL import ImageGrab
from tkinter import ttk

window = tk.Tk()
window.title("Sistem Pengiraan Isi Padu Pepejal")
style = ttk.Style()
# style.theme_use('clam')
style.configure("Treeview.Heading", font=("Quicksand Medium", 10))

# A function to calculate the volume of a Silinder
def calculate_volume(shape):
    try:
        if shape == "Silinder":
            radius, height = int(entry_1.get()), int(entry_2.get())
        elif shape == "Kon":
            radius, height = int(entry_1.get()), int(entry_2.get())
        elif shape == "Sfera":
            radius = int(entry_1.get())   
        elif shape == "Kuboid":
            height, width, length = int(entry_1.get()), int(entry_2.get()), int(entry_3.get())
        elif shape == "Piramid":
            height, width, length = int(entry_1.get()), int(entry_2.get()), int(entry_3.get())
        elif shape == "Prisma":
            height, width, length = int(entry_1.get()), int(entry_2.get()), int(entry_3.get())
        elif shape == "Hemisfera":
            radius = int(entry_1.get())
        elif shape == "Semisilinder":
            radius, height = int(entry_1.get()), int(entry_2.get())
    except ValueError:
        # Create a top level window
        warning = tk.Toplevel()
        warning.title("Ralat")
        warning.geometry("300x100+450+250")
        warning.resizable(False, False)
        warning_label = ttk.Label(warning, text="Sila masukkan nombor dalam semua ruangan.")
        warning_label.grid(row=0, column=0, padx=10, pady=10)
        ok_button = ttk.Button(warning, text="OK", command=warning.destroy)
        ok_button.grid(row=1, column=0, padx=10, pady=10)
        warning.focus_set()
    
        return
    
    if shape == "Silinder":
        volume = 3.142 * radius ** 2 * height
    elif shape == "Kon":
        volume = 3.142 * radius ** 2 * height / 3
    elif shape == "Sfera":
        volume = 4 / 3 * 3.142 * radius ** 3
    elif shape == "Kuboid":
        volume = height * width * length
    elif shape == "Piramid":
        volume = height * width * length / 3
    elif shape == "Prisma":
        volume = height * width * length / 2
    elif shape == "Hemisfera":
        volume = 2 / 3 * 3.142 * radius ** 3
    elif shape == "Semisilinder":
        volume = 3.142 * radius ** 2 * height / 2
        
    volume_label2.config(text=f"{volume:.2f} cm\u00b3")


def change_labels(shape):
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    if shape == "Silinder":
        label_1.config(text="Jejari (cm): ")
        label_2.config(text="Ketinggian (cm): ")
        label_3.config(text="")
        entry_1.config(state="normal")
        entry_2.config(state="normal")
        entry_3.config(state="disabled")
    elif shape == "Kon":
        label_1.config(text="Jejari (cm): ")
        label_2.config(text="Ketinggian (cm): ")
        label_3.config(text="")
        entry_1.config(state="normal")
        entry_2.config(state="normal")
        entry_3.config(state="disabled")
    elif shape == "Sfera":
        label_1.config(text="Jejari (cm): ")
        label_2.config(text="")
        label_3.config(text="")
        entry_1.config(state="normal")
        entry_2.config(state="disabled")
        entry_3.config(state="disabled")
    elif shape == "Kuboid":
        label_1.config(text="Ketinggian (cm): ")
        label_2.config(text="Lebar (cm): ")
        label_3.config(text="Panjang (cm): ")
        entry_1.config(state="normal")
        entry_2.config(state="normal")
        entry_3.config(state="normal")
    elif shape == "Piramid":
        label_1.config(text="Panjang (cm): ")
        label_2.config(text="Lebar (cm): ")
        label_3.config(text="Ketinggian (cm): ")
        entry_1.config(state="normal")
        entry_2.config(state="normal")
        entry_3.config(state="normal")
    elif shape == "Prisma":
        label_1.config(text="Panjang (cm): ")
        label_2.config(text="Lebar (cm): ")
        label_3.config(text="Ketinggian (cm): ")
        entry_1.config(state="normal")
        entry_2.config(state="normal")
        entry_3.config(state="normal")
    elif shape == "Hemisfera":
        label_1.config(text="Jejari (cm): ")
        label_2.config(text="")
        label_3.config(text="")
        entry_1.config(state="normal")
        entry_2.config(state="disabled")
        entry_3.config(state="disabled")
    elif shape == "Semisilinder":
        label_1.config(text="Jejari (cm): ")
        label_2.config(text="Ketinggian (cm): ")
        label_3.config(text="")
        entry_1.config(state="normal")
        entry_2.config(state="normal")
        entry_3.config(state="disabled")
        
    
    

# Place the wiindow at the center of the screen
x = ImageGrab.grab().size[0] / 2 - 400 * 1.3
y = ImageGrab.grab().size[1] / 2 - 170 * 2
print(x, y)
window_width, window_height = 400, 270
window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

# Create the widgets
shapes = ["Silinder", "Kon", "Sfera", "Kuboid", "Piramid", "Prisma", "Hemisfera", "Semisilinder"]
shape_choice = tk.StringVar(window)
# Create a dropdown menu to choose the shape
shape_label = ttk.Label(window, text="Pilih bentuk: ")
shape_dropdown = ttk.OptionMenu(
    window, shape_choice, shapes[0], *shapes)
shape_label.grid(row=0, column=0, padx=10, pady=10)
shape_dropdown.grid(row=0, column=1, padx=10, pady=10)

# Bind the choice of the dropdown to change the Labels accordingly
shape_choice.trace("w", lambda *args: change_labels(shape=shape_choice.get()))

label_1 = ttk.Label(window, text="Jejari (cm): ")
entry_1 = ttk.Entry(window)
label_1.grid(row=1, column=0, padx=10, pady=10)
entry_1.grid(row=1, column=1, padx=10, pady=10)

label_2 = ttk.Label(window, text="Ketinggian (cm): ")
entry_2 = ttk.Entry(window)
label_2.grid(row=2, column=0, padx=10, pady=10)
entry_2.grid(row=2, column=1, padx=10, pady=10)

label_3 = ttk.Label(window, text="Ketinggian (cm): ")
entry_3 = ttk.Entry(window)
label_3.grid(row=3, column=0, padx=10, pady=10)
entry_3.grid(row=3, column=1, padx=10, pady=10)

volume_label1 = ttk.Label(window, text="Isi Padu: ")
volume_label2 = ttk.Label(window, text="0.00 cm\u00b3")
volume_label1.grid(row=4, column=0, padx=10, pady=10)
volume_label2.grid(row=4, column=1, padx=10, pady=10)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

calculate_button = ttk.Button(
    window,
    text="Kira",
    command=lambda: calculate_volume(shape=shape_choice.get()))
calculate_button.grid(row=5, column=0, padx=10, pady=10)

# Make a enter keybind to the calculate button
window.bind("<Return>", lambda event: calculate_volume(shape=shape_choice.get()))

entry_1.focus_set()
window.mainloop()
