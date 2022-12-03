import tkinter as tk
try:
    from PIL import ImageGrab
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'Pillow'])
    from PIL import ImageGrab
import datetime
from items import *
from tkinter import ttk
from discounts import *

window = tk.Tk()
window.title("Sistem Kiraan Wang Kedai Buku Chung Ling")
style = ttk.Style()
# style.theme_use('clam')
style.configure("Treeview.Heading", font=('Comic Sans MS', 10))

screen_width, screen_height = ImageGrab.grab().size

default_quantity = 1
quantity_var = tk.StringVar(value=default_quantity)

total_price = 0
total_discount = 0

def update_time():
    global time_label
    global order_quantity
    time_label.config(
        text="Masa: " + str(datetime.datetime.now().strftime("%H:%M:%S") + '\n'), font=("Comic Sans MS", 10))
    date_label.config(
        text="\nTarikh: " + str(datetime.datetime.now().strftime("%d/%m/%Y")), font=("Comic Sans MS", 10))
    # order_quantity.configure(selectforeground="red")
    time_label.after(1000, update_time)


def count_all(event):
    global total_price
    total = 0
    for i in order_list.get_children():
        total = total + int(order_list.item(i)['values'][2])
    print(total)
    if total_discount > 0:
        total -= total_discount
    order_total_price.config(text="Jumlah: RM " +
                             str(total), font=("Comic Sans MS", 15))
    total_price = total
    order_total_paid_input.focus_set()


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
            order_list.insert('', 'end', text="1",
                              values=(name, quantity, price))
        elif on_the_list:
            order_list.item(list_item, values=(name, order_list.item(list_item)[
                            'values'][1] + quantity, (order_list.item(list_item)['values'][1] + quantity) * price))
    else:
        order_list.insert('', 'end', text="1", values=(name, quantity, price))


def delete_order(event):
    order_list.delete(order_list.selection()[0])


def clear_order(event):
    order_list.delete(*order_list.get_children())
    order_total_paid_input.delete(0, 'end')
    order_total_change.config(text="Baki: RM 0", font=("Comic Sans MS", 15))
    order_total_price.config(text="Jumlah: RM 0", font=("Comic Sans MS", 15))
    order_total_discount.config(text="Diskaun: RM 0", font=("Comic Sans MS", 15))
    order.delete(0, 'end')
    order.focus_set()


def count_change(event):
    paid = int(order_total_paid_input.get())
    if paid >= total_price:
        change = paid - total_price
        order_total_change.config(text="Baki: RM " + str(change),
                                  font=("Comic Sans MS", 15))
    else:
        # Create toplevel remind user to pay more
        warning = tk.Toplevel()
        not_enough = tk.Label(
            warning, text="Bayaran tidak mencukupi.", font=("Comic Sans MS", 15))
        top_level_button = tk.Button(warning, text="OK", font=(
            "Comic Sans MS", 15), command=warning.destroy)
        not_enough.pack()
        top_level_button.pack()
        warning.focus_set()


def add_discount(event):
    global total_price
    global total_discount
    discount = discount_code_entry.get()
    total_discount += check_discount(discount)
    order_total_discount.config(
        text="Diskaun: RM " + str(total_discount), font=("Comic Sans MS", 15))
    if total_price > 0:
        total_price -= total_discount
        order_total_price.config(text="Jumlah: RM " +
                             str(total_price), font=("Comic Sans MS", 15))


window.state('zoomed')
title = tk.Label(text="\nKedai Buku Chung Ling", font=("Comic Sans MS", 20, "bold"))
sub_title = tk.Label(text="Sistem Kiraan Wang\n", font=("Comic Sans MS", 13))
time_label = tk.Label(
    text="Masa: " + str(datetime.datetime.now().strftime("%H:%M") + '\n'), font=("Comic Sans MS", 10))
date_label = tk.Label(
    text="\nTarikh: " + str(datetime.datetime.now().strftime("%d/%m/%Y")), font=("Comic Sans MS", 10))
order_label = tk.Label(text="      Pesanan: ", font=("Comic Sans MS", 15))
order = tk.Entry(window, width=20, font=("Comic Sans MS", 13))
order_quantity = tk.Spinbox(master=window, from_=1, to=100,
                            textvariable=quantity_var, font=("Comic Sans MS", 13), width=3)
order_enter = tk.Button(text="Masuk", font=("Comic Sans MS", 13))
order_delete = tk.Button(text="Padam", font=("Comic Sans MS", 13))
order_finish = tk.Button(text="Selesai", font=("Comic Sans MS", 13))
order_next_order = tk.Button(text="Pesanan Baharu", font=("Comic Sans MS", 13))
order_total_price = tk.Label(text="Jumlah: RM 0", font=("Comic Sans MS", 15))
order_total_paid_label = tk.Label(text="Bayar:", font=("Comic Sans MS", 15))
order_total_paid_input = tk.Entry(window, width=10, font=("Comic Sans MS", 13))
order_total_change = tk.Label(text="Baki: RM 0", font=("Comic Sans MS", 15))
order_total_discount = tk.Label(text="Diskaun: RM 0", font=("Comic Sans MS", 15))
# window.bind('<Return>', add_order)

discount_code_label = tk.Label(text="Kod Diskaun: ", font=("Comic Sans MS", 15))
discount_code_entry = tk.Entry(window, font=("Comic Sans MS", 13))
# separator = ttk.Separator(window, orient=tk.VERTICAL,)


order_enter.bind('<Button-1>', add_order)
order.bind('<Return>', add_order)
order_finish.bind('<Button-1>', count_all)
order.bind('<Control-Return>', count_all)
order_total_paid_input.bind('<Return>', count_change)
order_delete.bind('<Button-1>', delete_order)
order_next_order.bind('<Button-1>', clear_order)
window.bind('<Control-BackSpace>', clear_order)
discount_code_entry.bind('<Return>', add_discount)

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
order_next_order.pack(side=tk.BOTTOM, pady=5)
order_finish.pack(side=tk.BOTTOM)

# order_list_frame.grid_rowconfigure(0, weight=1)
# order_list_frame.grid_columnconfigure(0, weight=1)


order_list.grid(row=0, column=0, sticky=tk.E, padx=50)
order_list_frame.pack(side=tk.RIGHT, padx=0, pady=10)
order_total_change.pack(side=tk.BOTTOM)
order_total_paid_input.pack(side=tk.BOTTOM)
order_total_paid_label.pack(side=tk.BOTTOM)
order_total_discount.pack(side=tk.BOTTOM)
order_total_price.pack(side=tk.BOTTOM)


discount_code_label.pack(side=tk.TOP, anchor=tk.SW, padx=30)

discount_code_entry.pack(side=tk.TOP, anchor=tk.SW, padx=30)
order_label.pack(side=tk.LEFT)
order.pack(side=tk.LEFT)
order_quantity.pack(side=tk.LEFT, padx=10)
order_enter.pack(side=tk.LEFT, padx=20)
order_delete.pack(side=tk.LEFT, padx=20)


order_quantity.configure(state='readonly', selectbackground="#f0f0f0",
                         selectforeground="black")


# separator.pack(fill=tk.Y, side=tk.LEFT, padx=10)

order.focus_set()


update_time()
window.mainloop()
