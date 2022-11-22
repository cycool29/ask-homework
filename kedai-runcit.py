import tkinter as tk
from PIL import ImageGrab
import datetime
from items import *
from tkinter import ttk

window = tk.Tk()
window.title("Sistem Kiraan Wang Kedai Buku Chung Ling")
style = ttk.Style()
# style.theme_use('clam')
style.configure("Treeview.Heading", font=('Quicksand Medium', 10))

screen_width, screen_height = ImageGrab.grab().size

default_quantity = 1
quantity_var = tk.StringVar(value=default_quantity)


def update_time():
    global time_label
    global order_quantity
    time_label.config(
        text="Masa: " + str(datetime.datetime.now().strftime("%H:%M:%S") + '\n'), font=("Quicksand", 10))
    date_label.config(
        text="\nTarikh: " + str(datetime.datetime.now().strftime("%d/%m/%Y")), font=("Quicksand", 10))
    # order_quantity.configure(selectforeground="red")
    time_label.after(1000, update_time)


def count_all(event):
    total = 0
    for i in order_list.get_children():
        total = total + int(order_list.item(i)['values'][2])
    print(total)
    # discount_toplevel = tk.Toplevel()
    # discount_toplevel.geometry("300x100+" + str(int(window.winfo_screenwidth() // 2 - 300 // 2)) +
    #                            "+" + str(int(window.winfo_screenheight() // 2 - 100 // 2)))
    # discount_toplevel.title("Diskaun")
    # discount_label = tk.Label(
    #     discount_toplevel, text="Kod Diskaun: ", font=("Quicksand", 10))
    # discount_entry = tk.Entry(discount_toplevel, font=("Quicksand", 10))
    # discount_label.pack(side=tk.LEFT, padx=10)
    # discount_entry.pack(side=tk.LEFT)
    # discount_entry.focus_set()
    # discount_toplevel.mainloop()


def add_order(event):
    on_the_list = False
    price, name = check_item(int(order.get()))
    quantity = int(quantity_var.get())
    price *= quantity
    # if order is not in list, add it
    # if name.lower() not in order_list.get_children():
    #     order_list.insert('', 'end', text='1', values=(name, quantity, price))
    if order_list.get_children():
        for child in order_list.get_children():
            if name in order_list.item(child)['values']:
                on_the_list = True
                list_item = child
                print(child)
        if not on_the_list:
            order_list.insert('', 'end', text="1", values=(name, quantity, price))
        elif on_the_list:
            order_list.item(list_item, values=(name, order_list.item(list_item)['values'][1] + quantity, (order_list.item(list_item)['values'][1] + quantity) * price))
    else:
        order_list.insert('', 'end', text="1", values=(name, quantity, price))

# window.geometry("600x570+" + str(int(screen_width / 2 - 610)) +
#                 "+" + str(int(screen_height / 2 - 510)))
window.state('zoomed')
title = tk.Label(text="Kedai Buku Chung Ling", font=("Quicksand Medium", 20))
sub_title = tk.Label(text="Sistem Kiraan Wang\n", font=("Quicksand", 13))
time_label = tk.Label(
    text="Masa: " + str(datetime.datetime.now().strftime("%H:%M") + '\n'), font=("Quicksand", 10))
date_label = tk.Label(
    text="\nTarikh: " + str(datetime.datetime.now().strftime("%d/%m/%Y")), font=("Quicksand", 10))
order_label = tk.Label(text="      Pesanan: ", font=("Quicksand", 15))
order = tk.Entry(window, width=30, font=("Quicksand", 13))
order_quantity = tk.Spinbox(master=window, from_=1, to=100,
                            textvariable=quantity_var, font=("Quicksand", 13), width=3)
order_enter = tk.Button(text="Enter", font=("Quicksand", 13))
order_finish = tk.Button(text="Selesai", font=("Quicksand", 13))
order_total_price = tk.Label(text="Jumlah: RM0", font=("Quicksand", 15))
# window.bind('<Return>', add_order)

discount_code_label = tk.Label(text="Kod Diskaun: ", font=("Quicksand", 15))
discount_code_entry = tk.Entry(window, font=("Quicksand", 13))
# separator = ttk.Separator(window, orient=tk.VERTICAL,)

total_amount_label = tk.Label(text="Jumlah: RM0", font=("Quicksand", 15))

order_enter.bind('<Button-1>', add_order)
window.bind('<Return>', add_order)
order_finish.bind('<Button-1>', count_all)
window.bind('<Control-Return>', count_all)

order_list_frame = tk.Frame(window)
order_list = ttk.Treeview(order_list_frame, column=(
    "c1", "c2", "c3"), show='headings', height=14)
order_list.column("# 1", anchor=tk.CENTER, width=250)
order_list.heading("# 1", text="Name Barang")
order_list.column("# 2", anchor=tk.CENTER, width=100)
order_list.heading("# 2", text="Kuantiti")
order_list.column("# 3", anchor=tk.CENTER, width=200)
order_list.heading("# 3", text="Harga")


title.pack()
sub_title.pack()
time_label.pack(side=tk.BOTTOM, padx=50)
date_label.pack(side=tk.BOTTOM, padx=50)
order_finish.pack(side=tk.BOTTOM)

# order_list_frame.grid_rowconfigure(0, weight=1)
# order_list_frame.grid_columnconfigure(0, weight=1)


order_list.grid(row=0, column=0, sticky=tk.E, padx=50)
order_list_frame.pack(side=tk.RIGHT, padx=0, pady=10)
total_amount_label.pack(side=tk.BOTTOM, pady=70)



discount_code_label.pack(side=tk.TOP, anchor=tk.SW, padx=30)

discount_code_entry.pack(side=tk.TOP, anchor=tk.SW, padx=30)
order_label.pack(side=tk.LEFT)
order.pack(side=tk.LEFT)
order_quantity.pack(side=tk.LEFT, padx=10)
order_enter.pack(side=tk.LEFT, padx=20)


order_quantity.configure(state='readonly', selectbackground="#f0f0f0",
                             selectforeground="black")


# separator.pack(fill=tk.Y, side=tk.LEFT, padx=10)

order.focus_set()


update_time()
window.mainloop()
