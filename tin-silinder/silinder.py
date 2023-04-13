import tkinter as tk
from PIL import ImageGrab
from tkinter import ttk

window = tk.Tk()
window.title("Sistem Pengiraan Isi Padu Silinder")
style = ttk.Style()
# style.theme_use('clam')
style.configure("Treeview.Heading", font=("Quicksand Medium", 10))

# A function to calculate the volume of a cylinder
def calculate_volume():
    try:
        radius, height = int(radius_entry.get()), int(height_entry.get())
    except ValueError:
        # Create a top level window
        warning = tk.Toplevel()
        warning.title("Ralat")
        warning.geometry("300x100+450+250")
        warning.resizable(False, False)
        warning_label = ttk.Label(warning, text="Sila masukkan nombor dalam kedua-dua ruangan.")
        warning_label.grid(row=0, column=0, padx=10, pady=10)
        ok_button = ttk.Button(warning, text="OK", command=warning.destroy)
        ok_button.grid(row=1, column=0, padx=10, pady=10)
        warning.focus_set()
    
        return
    
    volume = 3.142 * radius ** 2 * height
    volume_label2.config(text=f"{volume:.2f} cm\u00b3")


# Place the wiindow at the center of the screen
x = ImageGrab.grab().size[0] / 2 - 400 * 1.3
y = ImageGrab.grab().size[1] / 2 - 170 * 2
print(x, y)
window_width, window_height = 400, 170
window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
window.resizable(False, False)

# Create the widgets
radius_label = ttk.Label(window, text="Jejari (cm): ")
radius_entry = ttk.Entry(window)
radius_label.grid(row=0, column=0, padx=10, pady=10)
radius_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = ttk.Label(window, text="Ketinggian (cm): ")
height_entry = ttk.Entry(window)
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry.grid(row=1, column=1, padx=10, pady=10)

volume_label1 = ttk.Label(window, text="Isi Padu: ")
volume_label2 = ttk.Label(window, text="0.00 cm\u00b3")
volume_label1.grid(row=2, column=0, padx=10, pady=10)
volume_label2.grid(row=2, column=1, padx=10, pady=10)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

calculate_button = ttk.Button(
    window,
    text="Kira",
    command=lambda: calculate_volume())
calculate_button.grid(row=3, column=0, padx=10, pady=10)

# Make a enter keybind to the calculate button
window.bind("<Return>", lambda event: calculate_volume())

radius_entry.focus_set()
window.mainloop()
