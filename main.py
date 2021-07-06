import time
from tkinter import *
from tkinter import messagebox
import random

tk = Tk()
app_running = True

size_canvas_x = 500
size_canvas_y = 500
s_x = s_y = 10  # размер игрового поля
step_x = size_canvas_x // s_x  # шаг по горизонтали
step_y = size_canvas_y // s_y  # шаг по вертикали
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y
menu_x = 250
ships = s_x // 2  # определяем максимальное количество кораблей
ship_len1 = s_x // 5  # длина первого типа корабля
ship_len2 = s_x // 3  # длина второго типа корабля
ship_len3 = s_x // 2  # длина третьего типа корабля
enemy_ships = [[0 for i in range(s_x)] for i in range(s_x)]
#print(enemy_ships)


def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Игра морской бой")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=size_canvas_x + menu_x, height=size_canvas_y)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.pack()
tk.update()


def draw_table():
    for i in range(0, s_x + 1):
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)


draw_table()


def button_show_enemy():
    pass


def button_begin_again():
    pass


b0 = Button(tk, text="Показать корабли противника", command=button_show_enemy)
b0.place(x=size_canvas_x + 20, y=30)

b1 = Button(tk, text="Начать заново", command=button_begin_again)
b1.place(x=size_canvas_x + 20, y=70)


def add_to_all(event):
    _type = 0  # левая кнопка мыши
    if event.num == 3:
        _type = 1  # правая кнопка мыши
    # print(_type)
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    # print(mouse_x, mouse_y)
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y

    print(ip_x, ip_y, "_type", _type)


canvas.bind_all("<Button-1>", add_to_all)  # левая кнопка мыши
canvas.bind_all("<Button-3>", add_to_all)  # правая кнопка мыши


# def generate_enemy_ships():
#     global enemy_ships
#     ships_list = []
#     # генерируем список случайных длин кораблей
#     for i in range(0, ships):
#         ships_list.append(random.choice([ship_len1,ship_len2,ship_len3]))
#         print(ships_list)
#
#
#         sum_1_all_ships = sum(ships_list)
#         sum_1_enemy = 0
#         while sum_1_enemy !=sum_1_all_ships:
#
# generate_enemy_ships()


while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()

    time.sleep(0.005)
