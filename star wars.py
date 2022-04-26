from tkinter import *
from time import *
from random import *
from tkinter import messagebox
from threading import *

def shot(event):
    global bullet, img_bullet, img_ship_1, first, second, bullet_1, img_bullet_1, third, fourth, fifth
    global bullet_2, bullet_3, bullet_4, img_bullet_2, img_bullet_3, img_bullet_4
    global bullet_1_1, bullet_2_2, bullet_3_3, bullet_4_4, bullet_5_5, number_of_enemy, num_of_enemy
    object = c.coords(img_ship_1)
    objx = int(object[0])
    objy = int(object[1])
    print(objx, objy)
    if first == True:
        bullet = PhotoImage(file=images['bullet'])
        img_bullet = c.create_image(objx, objy, image=bullet)
        first = False
        bullet_1_1 = True
        bullet_fly_1()
    elif second == True:
        bullet_1 = PhotoImage(file=images['bullet'])
        img_bullet_1 = c.create_image(objx, objy, image=bullet_1)
        second = False
        bullet_2_2 = True
        bullet_fly_2()
    elif third == True:
        bullet_2 = PhotoImage(file=images['bullet'])
        img_bullet_2 = c.create_image(objx, objy, image=bullet_2)
        third = False
        bullet_3_3 = True
        bullet_fly_3()
    elif fourth == True:
        bullet_3 = PhotoImage(file=images['bullet'])
        img_bullet_3 = c.create_image(objx, objy, image=bullet_3)
        fourth = False
        bullet_4_4 = True
        bullet_fly_4()
    elif fifth == True:
        bullet_4 = PhotoImage(file=images['bullet'])
        img_bullet_4 = c.create_image(objx, objy, image=bullet_4)
        fifth = False
        bullet_5_5 = True
        bullet_fly_5()
    else:
        if num_of_enemy <= 0:
            lab3.config(text='Гра закінчена')
        else:
            lab3.config(text='Почекайте, поки пролетять пулі')

def bullet_fly_1():
    global bullet, img_bullet, bullet_1_1, first, img_enemy_1, img_enemy_2, img_enemy_3, number_of_enemy, img_enemy_4, img_enemy_5, speed_of_bullet, kill, num_of_enemy
    c.move(img_bullet, speed_of_bullet, 0)
    x1y1 = c.coords(img_bullet)
    place_y = randint(50, 450)
    if -20 < c.coords(img_enemy_1)[0] - x1y1[0] < 40:
        if -20 < c.coords(img_enemy_1)[1] - x1y1[1] < 40:
            explosing(coo=c.coords(img_bullet))
            print(c.coords(img_enemy_1)[1] - x1y1[1])
            bullet_1_1 = False
            first = True
            lab3.config(text='')
            c.move(img_bullet, -1000, 0)
            c.coords(img_enemy_1, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_2)[0] - x1y1[0] < 40:
        if -20 < c.coords(img_enemy_2)[1] - x1y1[1] < 40:
            explosing(coo=c.coords(img_bullet))
            print(c.coords(img_enemy_2)[1] - x1y1[1])
            bullet_1_1 = False
            first = True
            lab3.config(text='')
            c.move(img_bullet, -1000, 0)
            c.coords(img_enemy_2, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_3)[0] - x1y1[0] < 40:
        if -20 < c.coords(img_enemy_3)[1] - x1y1[1] < 40:
            explosing(coo=c.coords(img_bullet))
            print(c.coords(img_enemy_3)[1] - x1y1[1])
            bullet_1_1 = False
            first = True
            lab3.config(text='')
            c.move(img_bullet, -1000, 0)
            c.coords(img_enemy_3, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_4)[0] - x1y1[0] < 40:
        if -20 < c.coords(img_enemy_4)[1] - x1y1[1] < 40:
            explosing(coo=c.coords(img_bullet))
            print(c.coords(img_enemy_4)[1] - x1y1[1])
            bullet_1_1 = False
            first = True
            lab3.config(text='')
            c.move(img_bullet, -1000, 0)
            c.coords(img_enemy_4, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if x1y1[0] > 800:
        bullet_1_1 = False
        if num_of_enemy != 0:
            first = True
        lab3.config(text='')
    if bullet_1_1 == True:
        win.after(50, bullet_fly_1)

def explosing(coo):
    global img_explos, explos
    explos = PhotoImage(file=images['explosion'])
    img_explos = c.create_image(coo[0], coo[1], image=explos)
    win.after(10, move_exp)

def move_exp():
    global img_explos, explos, number_exp
    if number_exp > 0:
        c.move(img_explos, 0, -5)
        number_exp = number_exp - 1
        win.after(100, move_exp)
    else:
        win.after(300, clear)

def clear():
    global img_explos, number_exp
    c.coords(img_explos, 1000, 40)
    number_exp = 5

def bullet_fly_2():
    global bullet_1, img_bullet_1, bullet_2_2, second, img_enemy_1, img_enemy_2, img_enemy_3, number_of_enemy, speed_of_bullet, kill, num_of_enemy
    c.move(img_bullet_1, speed_of_bullet, 0)
    x2y2 = c.coords(img_bullet_1)
    place_y = randint(50, 450)
    if -20 < c.coords(img_enemy_1)[0] - x2y2[0] < 40:
        if -20 < c.coords(img_enemy_1)[1] - x2y2[1] < 40:
            explosing(coo=c.coords(img_bullet_1))
            print('sefwar')
            bullet_2_2 = False
            second = True
            lab3.config(text='')
            c.move(img_bullet_1, -1000, 0)
            c.coords(img_enemy_1, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_2)[0] - x2y2[0] < 40:
        if -20 < c.coords(img_enemy_2)[1] - x2y2[1] < 40:
            explosing(coo=c.coords(img_bullet_1))
            print(c.coords(img_enemy_2)[1] - x2y2[1])
            bullet_2_2 = False
            second = True
            lab3.config(text='')
            c.move(img_bullet_1, -1000, 0)
            c.coords(img_enemy_2, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_3)[0] - x2y2[0] < 40:
        if -20 < c.coords(img_enemy_3)[1] - x2y2[1] < 40:
            explosing(coo=c.coords(img_bullet_1))
            print(c.coords(img_enemy_3)[1] - x2y2[1])
            bullet_2_2 = False
            second = True
            lab3.config(text='')
            c.move(img_bullet_1, -1000, 0)
            c.coords(img_enemy_3, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_4)[0] - x2y2[0] < 40:
        if -20 < c.coords(img_enemy_4)[1] - x2y2[1] < 40:
            explosing(coo=c.coords(img_bullet_1))
            print(c.coords(img_enemy_4)[1] - x2y2[1])
            bullet_2_2 = False
            second = True
            lab3.config(text='')
            c.move(img_bullet_1, -1000, 0)
            c.coords(img_enemy_4, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if x2y2[0] > 800:
        bullet_2_2 = False
        if num_of_enemy != 0:
            second = True
        lab3.config(text='')
    if bullet_2_2 == True:
        win.after(50, bullet_fly_2)

def bullet_fly_3():
    global bullet_2, img_bullet_2, bullet_3_3, third, img_enemy_1, img_enemy_2, img_enemy_3, number_of_enemy, speed_of_bullet, kill, num_of_enemy
    c.move(img_bullet_2, speed_of_bullet, 0)
    x3y3 = c.coords(img_bullet_2)
    place_y = randint(50, 450)
    if -20 < c.coords(img_enemy_1)[0] - x3y3[0] < 40:
        if -20 < c.coords(img_enemy_1)[1] - x3y3[1] < 40:
            explosing(coo=c.coords(img_bullet_2))
            print('sefwar')
            bullet_3_3 = False
            third = True
            lab3.config(text='')
            c.move(img_bullet_2, -1000, 0)
            c.coords(img_enemy_1, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_2)[0] - x3y3[0] < 40:
        if -20 < c.coords(img_enemy_2)[1] - x3y3[1] < 40:
            explosing(coo=c.coords(img_bullet_2))
            print('sefwar')
            bullet_3_3 = False
            third = True
            lab3.config(text='')
            c.move(img_bullet_2, -1000, 0)
            c.coords(img_enemy_2, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_3)[0] - x3y3[0] < 40:
        if -20 < c.coords(img_enemy_3)[1] - x3y3[1] < 40:
            explosing(coo=c.coords(img_bullet_2))
            print('sefwar')
            bullet_3_3 = False
            third = True
            lab3.config(text='')
            c.move(img_bullet_2, -1000, 0)
            c.coords(img_enemy_3, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_4)[0] - x3y3[0] < 40:
        if -20 < c.coords(img_enemy_4)[1] - x3y3[1] < 40:
            explosing(coo=c.coords(img_bullet_2))
            print('sefwar')
            bullet_3_3 = False
            third = True
            lab3.config(text='')
            c.move(img_bullet_2, -1000, 0)
            c.coords(img_enemy_4, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if x3y3[0] > 800:
        bullet_3_3 = False
        if num_of_enemy != 0:
            third = True
        lab3.config(text='')
    if bullet_3_3 == True:
        win.after(50, bullet_fly_3)

def bullet_fly_4():
    global bullet_3, img_bullet_3, bullet_4_4, fourth, img_enemy_1, img_enemy_2, img_enemy_3, number_of_enemy, speed_of_bullet, kill, num_of_enemy
    c.move(img_bullet_3, speed_of_bullet, 0)
    x4y4 = c.coords(img_bullet_3)
    place_y = randint(50, 450)
    if -20 < c.coords(img_enemy_1)[0] - x4y4[0] < 40:
        if -20 < c.coords(img_enemy_1)[1] - x4y4[1] < 40:
            explosing(coo=c.coords(img_bullet_3))
            print('sefwar')
            bullet_4_4 = False
            fourth = True
            lab3.config(text='')
            c.move(img_bullet_3, -1000, 0)
            c.coords(img_enemy_1, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_2)[0] - x4y4[0] < 40:
        if -20 < c.coords(img_enemy_2)[1] - x4y4[1] < 40:
            explosing(coo=c.coords(img_bullet_3))
            print('sefwar')
            bullet_4_4 = False
            fourth = True
            lab3.config(text='')
            c.move(img_bullet_3, -1000, 0)
            c.coords(img_enemy_2, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_3)[0] - x4y4[0] < 40:
        if -20 < c.coords(img_enemy_3)[1] - x4y4[1] < 40:
            explosing(coo=c.coords(img_bullet_3))
            print('sefwar')
            bullet_4_4 = False
            fourth = True
            lab3.config(text='')
            c.move(img_bullet_3, -1000, 0)
            c.coords(img_enemy_3, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_4)[0] - x4y4[0] < 40:
        if -20 < c.coords(img_enemy_4)[1] - x4y4[1] < 40:
            explosing(coo=c.coords(img_bullet_3))
            print('sefwar')
            bullet_4_4 = False
            fourth = True
            lab3.config(text='')
            c.move(img_bullet_3, -1000, 0)
            c.coords(img_enemy_4, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if x4y4[0] > 800:
        bullet_4_4 = False
        if num_of_enemy != 0:
            fourth = True
        lab3.config(text='')
    if bullet_4_4 == True:
        win.after(50, bullet_fly_4)

def bullet_fly_5():
    global bullet_4, img_bullet_4, bullet_5_5, fifth, img_enemy_1, img_enemy_2, img_enemy_3, number_of_enemy, speed_of_bullet, kill, num_of_enemy
    c.move(img_bullet_4, speed_of_bullet, 0)
    x5y5 = c.coords(img_bullet_4)
    place_y = randint(50, 450)
    if -20 < c.coords(img_enemy_1)[0] - x5y5[0] < 40:
        if -20 < c.coords(img_enemy_1)[1] - x5y5[1] < 40:
            explosing(coo=c.coords(img_bullet_4))
            print('sefwar')
            bullet_5_5 = False
            fifth = True
            lab3.config(text='')
            c.move(img_bullet_4, -1000, 0)
            c.coords(img_enemy_1, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_2)[0] - x5y5[0] < 40:
        if -20 < c.coords(img_enemy_2)[1] - x5y5[1] < 40:
            explosing(coo=c.coords(img_bullet_4))
            print('sefwar')
            bullet_5_5 = False
            fifth = True
            lab3.config(text='')
            c.move(img_bullet_4, -1000, 0)
            c.coords(img_enemy_2, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_3)[0] - x5y5[0] < 40:
        if -20 < c.coords(img_enemy_3)[1] - x5y5[1] < 40:
            explosing(coo=c.coords(img_bullet_4))
            print('sefwar')
            bullet_5_5 = False
            fifth = True
            lab3.config(text='')
            c.move(img_bullet_4, -1000, 0)
            c.coords(img_enemy_3, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if -20 < c.coords(img_enemy_4)[0] - x5y5[0] < 40:
        if -20 < c.coords(img_enemy_4)[1] - x5y5[1] < 40:
            explosing(coo=c.coords(img_bullet_4))
            print('sefwar')
            bullet_5_5 = False
            fifth = True
            lab3.config(text='')
            c.move(img_bullet_4, -1000, 0)
            c.coords(img_enemy_4, 800, place_y)
            num_of_enemy -= 1
            kill = kill + 1
            lab1.config(text=f'Кількість вбивств -- {kill}')

    if x5y5[0] > 800:
        bullet_5_5 = False
        if num_of_enemy != 0:
            fifth = True
        lab3.config(text='')
    if bullet_5_5 == True:
        win.after(50, bullet_fly_5)

def check_place_ship():
    global img_ship_1
    x_y_ship = c.coords(img_ship_1)
    if x_y_ship[1] < 50:
        c.move(img_ship_1, 0, 3)
    if x_y_ship[1] > 450:
        c.move(img_ship_1, 0, -3)
    win.after(10, check_place_ship)

def restart_game():
    global first, second, third, fourth, fifth, img_ship_1, ship_1, hp, kill, number_of_enemy, num_of_enemy
    btn13.config(state='normal')
    lab4.config(text='.....................')
    lab3.config(text='')
    btn14.config(state='disabled')
    first = True
    second = True
    third = True
    fourth = True
    fifth = True
    ship_1 = PhotoImage(file=fon_ship)
    img_ship_1 = c.create_image(70, 300, image=ship_1)
    hp = 10
    kill = 0
    num_of_enemy = number_of_enemy
    lab2.config(text=f'Кількість життя -- {hp}')
    lab1.config(text=f'Кількість вбивств -- {kill}')
    enemys()
# ............................................................................................................................................
def back_game_to_set():
    global id_1, id_2, id_3, id_4
    win.after_cancel(id_1)
    win.after_cancel(id_2)
    win.after_cancel(id_3)
    win.after_cancel(id_4)
    c.forget()
    lab1.forget()
    lab2.forget()
    btn13.forget()
    btn14.forget()
    lab4.forget()
    lab3.forget()
    win.geometry('700x500')
    canvas_set.pack()

def get_ship_1():
    global fon_ship
    fon_ship = images['ship_1']
    print(fon_ship)
    canvas_ship_set.forget()
    canvas_set.pack()

def get_ship_2():
    global fon_ship
    fon_ship = images['ship_2']
    print(fon_ship)
    canvas_ship_set.forget()
    canvas_set.pack()

def get_ship_3():
    global fon_ship
    fon_ship = images['ship_3']
    print(fon_ship)
    canvas_ship_set.forget()
    canvas_set.pack()

def back_ship_to_win():
    canvas_ship_set.forget()
    canvas_set.pack()

def get_sky_1():
    global fon_game
    fon_game = images['sky_1']
    print(fon_game)
    canvas_game_set.forget()
    canvas_set.pack()

def get_sky_2():
    global fon_game
    fon_game = images['sky_2']
    print(fon_game)
    canvas_game_set.forget()
    canvas_set.pack()

def get_sky_3():
    global fon_game
    fon_game = images['sky_3']
    print(fon_game)
    canvas_game_set.forget()
    canvas_set.pack()

def back_game_to_win():
    canvas_game_set.forget()
    canvas_set.pack()

def ship_fon():
    canvas_set.forget()
    canvas_ship_set.pack()

def game_fon():
    canvas_set.forget()
    canvas_game_set.pack()

def settings():
    canv.forget()
    canvas_set.pack()

def back_to_win():
    canvas_set.forget()
    canv.pack()

def enemy_enemy():
    canvas_different_set.forget()
    canvas_speed_enemy.pack()

def from_speed_enemy_to_set():
    canvas_speed_enemy.forget()
    canvas_different_set.pack()

def start_game():
    global fon_game, sky4, fon_ship, ship_1, img_ship_1, img_sky_4
    global first, second, third, fourth, fifth
    canv.forget()
    c.pack()
    c1.place(x=0, y=500)
    sky4 = PhotoImage(file=fon_game)
    img_sky_4 = c.create_image(350, 250, image=sky4)
    ship_1 = PhotoImage(file=fon_ship)
    img_ship_1 = c.create_image(70, 300, image=ship_1)
    win.geometry('700x600')
    lab1.place(x=3, y=510)
    lab2.place(x=3, y=560)
    btn13.place(x=240, y=550)
    btn14.place(x=420, y=550)
    lab4.place(x=530, y=550)
    lab3.place(x=240, y=505)
    first = True
    second = True
    third = True
    fourth = True
    fifth = True
    enemys()

def enemys():
    enemy_1_1()
    enemy_2_2()
    enemy_3_3()
    enemy_4_4()

def enemy_1_1():
    global enemy_1, img_enemy_1, start, id_1
    place_y = randint(50, 450)
    enemy_1 = PhotoImage(file=images['ship_enemy'])
    img_enemy_1 = c.create_image(700, place_y, image=enemy_1)

    id_1 = enemy_move_1()

def enemy_move_1():
    global enemy_1, img_enemy_1, hp, number_of_enemy, img_bullet, img_bullet_1, img_bullet_2, img_bullet_3, img_bullet_4
    global first, second, third, fourth, fifth, img_enemy_1, img_enemy_2, img_enemy_3, img_enemy_4, start, num_of_enemy, id_1, speed_enemy
    place_y = randint(50, 450)
    c.move(img_enemy_1, -speed_enemy, 0)
    x_y = c.coords(img_enemy_1)
    if num_of_enemy > 0:
        if x_y[0] > -50:
            id_1 = win.after(20, enemy_move_1)
        else:
            hp = hp - 1
            if hp <= 0:
                lab2.config(text=f'Кількість життя -- 0')
            lab2.config(text=f'Кількість життя -- {hp}')
            c.coords(img_enemy_1, 1000, place_y)
            id_1 = win.after(20, enemy_move_1)
    else:
        lab4.config(text='Ти виграв')
        btn14.config(state='normal')
        btn13.config(state='disabled')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)
    if hp <= 0:
        lab4.config(text='Ти програв')
        btn14.config(state='normal')
        btn13.config(state='disabled')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)

def enemy_2_2():
    global enemy_2, img_enemy_2, id_2
    place_y = randint(50, 450)
    enemy_2 = PhotoImage(file=images['ship_enemy'])
    img_enemy_2 = c.create_image(800, place_y, image=enemy_2)

    id_2 = win.after(1000, enemy_move_2)

def enemy_move_2():
    global enemy_2, img_enemy_2, hp, number_of_enemy, img_bullet, img_bullet_1, img_bullet_2, img_bullet_3, img_bullet_4
    global first, second, third, fourth, fifth, img_enemy_1, img_enemy_2, img_enemy_3, img_enemy_4, start, num_of_enemy, id_2, speed_enemy
    place_y = randint(50, 450)
    c.move(img_enemy_2, -speed_enemy, 0)
    x_y = c.coords(img_enemy_2)
    if num_of_enemy > 0:
        if x_y[0] > -50:
            id_2 = win.after(20, enemy_move_2)
        else:
            hp = hp - 1
            if hp <= 0:
                lab2.config(text=f'Кількість життя -- 0')
            lab2.config(text=f'Кількість життя -- {hp}')
            c.coords(img_enemy_2, 1000, place_y)
            id_2 = win.after(20, enemy_move_2)

    else:
        lab4.config(text='Ти виграв')
        btn14.config(state='normal')
        btn13.config(state='disabled')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)
    if hp <= 0:
        lab4.config(text='Ти програв')
        btn14.config(state='normal')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)
        btn13.config(state='disabled')

def enemy_3_3():
    global enemy_3, img_enemy_3, id_3
    place_y = randint(50, 450)
    enemy_3 = PhotoImage(file=images['ship_enemy'])
    img_enemy_3 = c.create_image(800, place_y, image=enemy_3)

    id_3 = win.after(2000, enemy_move_3)

def enemy_move_3():
    global enemy_3, img_enemy_3, hp, number_of_enemy, img_bullet, img_bullet_1, img_bullet_2, img_bullet_3, img_bullet_4
    global first, second, third, fourth, fifth, img_enemy_1, img_enemy_2, img_enemy_3, img_enemy_4, start, num_of_enemy, id_3, speed_enemy
    place_y = randint(50, 450)
    c.move(img_enemy_3, -speed_enemy, 0)
    x_y = c.coords(img_enemy_3)
    if num_of_enemy > 0:
        if x_y[0] > -50:
            id_3 = win.after(20, enemy_move_3)
        else:
            hp = hp - 1
            if hp <= 0:
                lab2.config(text=f'Кількість життя -- 0')
            lab2.config(text=f'Кількість життя -- {hp}')
            c.coords(img_enemy_3, 1000, place_y)
            id_3 = win.after(20, enemy_move_3)
    else:
        lab4.config(text='Ти виграв')
        btn14.config(state='normal')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)
        btn13.config(state='disabled')
    if hp <= 0:
        lab4.config(text='Ти програв')
        btn14.config(state='normal')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)
        btn13.config(state='disabled')

def enemy_4_4():
    global enemy_4, img_enemy_4, id_4
    place_y = randint(50, 450)
    enemy_4 = PhotoImage(file=images['ship_enemy'])
    img_enemy_4 = c.create_image(800, place_y, image=enemy_4)

    id_4 = win.after(3000, enemy_move_4)

def enemy_move_4():
    global enemy_4, img_enemy_4, hp, number_of_enemy, img_bullet, img_bullet_1, img_bullet_2, img_bullet_3, img_bullet_4
    global first, second, third, fourth, fifth, img_enemy_1, img_enemy_2, img_enemy_3, img_enemy_4, num_of_enemy, id_4, speed_enemy
    place_y = randint(50, 450)
    c.move(img_enemy_4, -speed_enemy, 0)
    x_y = c.coords(img_enemy_4)
    if num_of_enemy > 0:
        if x_y[0] > -50:
            id_4 = win.after(20, enemy_move_4)
        else:
            hp = hp - 1
            if hp <= 0:
                lab2.config(text=f'Кількість життя -- 0')
            lab2.config(text=f'Кількість життя -- {hp}')
            c.coords(img_enemy_4, 1000, place_y)
            id_4 = win.after(20, enemy_move_4)
    else:
        lab4.config(text='Ти виграв')
        btn14.config(state='normal')
        btn13.config(state='disabled')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)
    if hp <= 0:
        lab4.config(text='Ти програв')
        btn14.config(state='normal')
        btn13.config(state='disabled')
        first = False
        second = False
        third = False
        fourth = False
        fifth = False
        c.coords(img_enemy_1, 800, 0)
        c.coords(img_enemy_2, 800, 0)
        c.coords(img_enemy_3, 800, 0)
        c.coords(img_enemy_4, 800, 0)
        c.coords(img_bullet_1, 1000, 0)
        c.coords(img_bullet_2, 1000, 0)
        c.coords(img_bullet_3, 1000, 0)
        c.coords(img_bullet_4, 1000, 0)
        c.coords(img_bullet, 1000, 0)

def finish_game():
    if messagebox.askokcancel('Вихід з програми', 'Ви точно хочете вийти з програми?'):
        exit()

def from_set_to_2set():
    canvas_set.forget()
    canvas_different_set.pack()

def from_dif_to_set():
    canvas_different_set.forget()
    canvas_set.pack()

def ship_speed():
    canvas_different_set.forget()
    canvas_speed_ship.pack()

def count_of_enemy():
    canvas_different_set.forget()
    canvas_count_enemy.pack()

def bullet_speed():
    canvas_different_set.forget()
    canvas_speed_bullet.pack()

def from_speed_ship_to_set():
    canvas_speed_ship.forget()
    canvas_different_set.pack()

def from_count_of_enemy_to_set():
    canvas_count_enemy.forget()
    canvas_different_set.pack()

def from_speed_bullet_to_set():
    canvas_speed_bullet.forget()
    canvas_different_set.pack()

def speed_ship_1():
    global speed_of_ship
    speed_of_ship = 2
    canvas_speed_ship.forget()
    canvas_different_set.pack()

def speed_ship_2():
    global speed_of_ship
    speed_of_ship = 3
    canvas_speed_ship.forget()
    canvas_different_set.pack()

def speed_ship_3():
    global speed_of_ship
    speed_of_ship = 4
    canvas_speed_ship.forget()
    canvas_different_set.pack()

def speed_ship_4():
    global speed_of_ship
    speed_of_ship = 5
    canvas_speed_ship.forget()
    canvas_different_set.pack()

def count_enemy_1():
    global number_of_enemy, num_of_enemy
    number_of_enemy = 30
    num_of_enemy = number_of_enemy
    canvas_count_enemy.forget()
    canvas_different_set.pack()

def count_enemy_2():
    global number_of_enemy, num_of_enemy
    number_of_enemy = 40
    num_of_enemy = number_of_enemy
    canvas_count_enemy.forget()
    canvas_different_set.pack()

def count_enemy_3():
    global number_of_enemy, num_of_enemy
    number_of_enemy = 60
    num_of_enemy = number_of_enemy
    canvas_count_enemy.forget()
    canvas_different_set.pack()

def count_enemy_4():
    global number_of_enemy, num_of_enemy
    number_of_enemy = 100
    num_of_enemy = number_of_enemy
    canvas_count_enemy.forget()
    canvas_different_set.pack()

def speed_bullet_1():
    global speed_of_bullet
    speed_of_bullet = 3
    canvas_speed_bullet.forget()
    canvas_different_set.pack()

def speed_bullet_2():
    global speed_of_bullet
    speed_of_bullet = 5
    canvas_speed_bullet.forget()
    canvas_different_set.pack()

def speed_bullet_3():
    global speed_of_bullet
    speed_of_bullet = 7
    canvas_speed_bullet.forget()
    canvas_different_set.pack()

def speed_bullet_4():
    global speed_of_bullet
    speed_of_bullet = 9
    canvas_speed_bullet.forget()
    canvas_different_set.pack()

def speed_enemy_1():
    global speed_enemy
    speed_enemy = 1
    canvas_speed_enemy.forget()
    canvas_different_set.pack()

def speed_enemy_2():
    global speed_enemy
    speed_enemy = 2
    canvas_speed_enemy.forget()
    canvas_different_set.pack()

def speed_enemy_3():
    global speed_enemy
    speed_enemy = 3
    canvas_speed_enemy.forget()
    canvas_different_set.pack()

def speed_enemy_4():
    global speed_enemy
    speed_enemy = 4
    canvas_speed_enemy.forget()
    canvas_different_set.pack()

win = Tk()
win.title('Start')
win.geometry('700x500+400+100')
win.resizable(0, 0)
win.protocol('WM_DELETE_WINDOW', finish_game)

# Усі картинки
images = {
    'sky_main': 'sky_png_2.png',
    'sky_1': 'stars_fon.png',
    'sky_2': 'stars_fon_2.png',
    'sky_3': 'stars_fon_3.png',
    'ship_enemy': 'enemy_ship.png',
    'ship_1': 'ship_1.png',
    'ship_2': 'ship_2.png',
    'ship_3': 'ship_3.png',
    'bullet': 'bullet_1.png',
    'explosion': 'explosion.png'
}

fon_game = images['sky_main']
fon_ship = images['ship_1']

kill = 0
hp = 10
number_exp = 5

speed_enemy = 1
speed_of_ship = 3
number_of_enemy = 2
num_of_enemy = number_of_enemy
speed_of_bullet = 5

first = True
second = True
third = True
fourth = True
fifth = True

bullet_1_1 = True
bullet_2_2 = True
bullet_3_3 = True
bullet_4_4 = True
bullet_5_5 = True

# Головне полотно для зображення налаштування, старт і вийти
canv = Canvas(win, height=500, width=700, highlightthickness=0)
canv.pack()

# Початковий фон
sky = PhotoImage(file=images['sky_main'])
canv.create_image(400, 250, image=sky)

# Створення кнопок для налаштування
btn1 = Button(canv, text='Вийти', font=('Freestyle Script', 30), fg='orange', height=1,  width=30, bg='darkblue', command=finish_game)
btn1.place(x=140, y=300)

btn2 = Button(canv, text='Налаштування', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=settings)
btn2.place(x=140, y=200)

btn3 = Button(canv, text='Почати', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=start_game)
btn3.place(x=140, y=100)

# Полотно для налаштування фону гри, виду корабля і гри
canvas_set = Canvas(win, height=500, width=700, highlightthickness=0)

# Фон налаштувань
sky1 = PhotoImage(file=images['sky_main'])
canvas_set.create_image(400, 250, image=sky1)

# Створення кнопок для налаштування фону гри, виду корабля і кпопки назад
btn4 = Button(canvas_set, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=back_to_win)
btn4.place(x=140, y=100)

btn5 = Button(canvas_set, text='Змінити фон гри', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=game_fon)
btn5.place(x=140, y=200)

btn6 = Button(canvas_set, text='Змінити вид корабля', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=ship_fon)
btn6.place(x=140, y=300)

btn16 = Button(canvas_set, text='Інші налаштування', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=from_set_to_2set)
btn16.place(x=140, y=400)

# Полотно для налаштувань фону гри
canvas_game_set = Canvas(win, height=500, width=700, highlightthickness=0)

# Фон налаштувань
sky2 = PhotoImage(file=images['sky_main'])
canvas_game_set.create_image(400, 250, image=sky2)

# Картинки для кнопок
sky_fon_1 = PhotoImage(file=images['sky_1'])
sky_fon_2 = PhotoImage(file=images['sky_2'])
sky_fon_3 = PhotoImage(file=images['sky_3'])

# Зміна розміру картинок
sky_fon_1 = sky_fon_1.subsample(4, 6)
sky_fon_2 = sky_fon_2.subsample(3, 6)
sky_fon_3 = sky_fon_3.subsample(3, 6)

# Створення кнопок для зміни фону гри
btn8 = Button(canvas_game_set, image=sky_fon_1, height=70, width=200, command=get_sky_1, highlightthickness=0)
btn8.place(x=250, y=200)

btn9 = Button(canvas_game_set, image=sky_fon_2, height=70, width=200, command=get_sky_2, highlightthickness=0)
btn9.place(x=250, y=300)

btn10 = Button(canvas_game_set, image=sky_fon_3, height=70, width=200, command=get_sky_3, highlightthickness=0)
btn10.place(x=250, y=400)

btn7 = Button(canvas_game_set, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=back_game_to_win)
btn7.place(x=140, y=100)

# Полотно для налаштувань виду корабля
canvas_ship_set = Canvas(win, height=500, width=700, highlightthickness=0)

# Фон налаштувань
sky3 = PhotoImage(file=images['sky_main'])
canvas_ship_set.create_image(400, 250, image=sky3)

# Картинки для кнопок
ship_fon_1 = PhotoImage(file='ship_1.png')
ship_fon_2 = PhotoImage(file='ship_2.png')
ship_fon_3 = PhotoImage(file='ship_3.png')

# Зміна розміру картинок
ship_fon_1 = ship_fon_1.subsample(2, 2)
ship_fon_2 = ship_fon_2.subsample(2, 2)
ship_fon_3 = ship_fon_3.subsample(2, 2)

# Створення кнопок для зміни виду корабля
btn11 = Button(canvas_ship_set, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=back_ship_to_win)
btn11.place(x=140, y=100)

btn12 = Button(canvas_ship_set, image=ship_fon_1, height=70, width=200, highlightthickness=0, bg='darkblue', command=get_ship_1)
btn12.place(x=250, y=200)

btn13 = Button(canvas_ship_set, image=ship_fon_2, height=70, width=200, highlightthickness=0, bg='darkblue', command=get_ship_2)
btn13.place(x=250, y=300)

btn14 = Button(canvas_ship_set, image=ship_fon_3, height=70, width=200, highlightthickness=0, bg='darkblue', command=get_ship_3)
btn14.place(x=250, y=400)

# Створення головного полотна
c = Canvas(win, height=500, width=700, highlightthickness=0)

# Фон налаштувань
sky4 = PhotoImage(file=fon_game)
img_sky_4 = c.create_image(400, 250, image=sky4)

# Створення полотна на панелі налаштувань
c1 = Canvas(win, height=100, width=700, highlightthickness=0, bg='purple')

lab1 = Label(win, text=f'Кількість вбивств -- {kill}', bg='purple', fg='orange', font=15)
lab2 = Label(win, text=f'Кількість життя -- {hp}', bg='purple', fg='orange', font=15)

btn13 = Button(win, text='Налаштування', bg='purple', fg='orange', font=('Verdana', 15), command=back_game_to_set)
btn14 = Button(win, text='Рестарт', bg='purple', fg='orange', font=('Verdana', 15), state='disabled', command=restart_game)
lab4 = Label(win, text='.....................', bg='purple', fg='orange', font=('Verdana', 15))

ship_1 = PhotoImage(file=fon_ship)
img_ship_1 = c.create_image(70, 300, image=ship_1)

c.focus_set()

c.bind('w', lambda event: c.move(img_ship_1, 0, -speed_of_ship))
c.bind('s', lambda event: c.move(img_ship_1, 0, speed_of_ship))

check_place_ship()

c.bind('g', shot)

bullet = PhotoImage(file=images['bullet'])
img_bullet = c.create_image(90, 300, image=bullet)

bullet_1 = PhotoImage(file=images['bullet'])
img_bullet_1 = c.create_image(90, 300, image=bullet_1)

bullet_2 = PhotoImage(file=images['bullet'])
img_bullet_2 = c.create_image(90, 300, image=bullet_2)

bullet_3 = PhotoImage(file=images['bullet'])
img_bullet_3 = c.create_image(90, 300, image=bullet_3)

bullet_4 = PhotoImage(file=images['bullet'])
img_bullet_4 = c.create_image(90, 300, image=bullet_4)

lab3 = Label(win, text='', bg='purple', fg='orange', font=15)

enemy_1 = PhotoImage(file=images['ship_enemy'])
img_enemy_1 = c.create_image(700, 300, image=enemy_1)

enemy_2 = PhotoImage(file=images['ship_enemy'])
img_enemy_2 = c.create_image(700, 300, image=enemy_2)

enemy_3 = PhotoImage(file=images['ship_enemy'])
img_enemy_3 = c.create_image(700, 300, image=enemy_3)

enemy_4 = PhotoImage(file=images['ship_enemy'])
img_enemy_4 = c.create_image(700, 300, image=enemy_4)

explos = PhotoImage(file=images['explosion'])
img_explos = c.create_image(20, 200, image=explos)

canvas_different_set = Canvas(win, height=500, width=700, highlightthickness=0, bg='purple')

sky5 = PhotoImage(file=images['sky_main'])
canvas_different_set.create_image(400, 250, image=sky5)

btn17 = Button(canvas_different_set, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue',  command=from_dif_to_set)
btn17.place(x=140, y=100)

btn18 = Button(canvas_different_set, text='Змінити швидкість корабля', font=('Freestyle Script', 22), fg='orange', width=42, bg='darkblue',  command=ship_speed)
btn18.place(x=140, y=190)

btn19 = Button(canvas_different_set, text='Змінити кількість ворогів', font=('Freestyle Script', 22), fg='orange', width=42, bg='darkblue',  command=count_of_enemy)
btn19.place(x=140, y=260)

btn20 = Button(canvas_different_set, text='Змінити швидкість ракети', font=('Freestyle Script', 22), fg='orange', width=42, bg='darkblue', command=bullet_speed)
btn20.place(x=140, y=330)

btn36 = Button(canvas_different_set, text='Змінити швидкість ворога', font=('Freestyle Script', 22), fg='orange', width=42, bg='darkblue', command=enemy_enemy)
btn36.place(x=140, y=400)

canvas_speed_ship = Canvas(win, height=500, width=700, highlightthickness=0, bg='purple')

sky6 = PhotoImage(file=images['sky_main'])
canvas_speed_ship.create_image(400, 250, image=sky6)

btn21 = Button(canvas_speed_ship, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=from_speed_ship_to_set)
btn21.place(x=140, y=10)

btn24 = Button(canvas_speed_ship, text='3', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=speed_ship_2)
btn24.place(x=140, y=210)

btn25 = Button(canvas_speed_ship, text='2', font=('Freestyle Script', 30), fg='red', width=30, bg='darkblue', command=speed_ship_1)
btn25.place(x=140, y=110)

btn26 = Button(canvas_speed_ship, text='4', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=speed_ship_3)
btn26.place(x=140, y=310)

btn27 = Button(canvas_speed_ship, text='5', font=('Freestyle Script', 30), fg='lightgreen', width=30, bg='darkblue', command=speed_ship_4)
btn27.place(x=140, y=410)

canvas_count_enemy = Canvas(win, height=500, width=700, highlightthickness=0, bg='purple')

sky7 = PhotoImage(file=images['sky_main'])
canvas_count_enemy.create_image(400, 250, image=sky7)

btn22 = Button(canvas_count_enemy, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=from_count_of_enemy_to_set)
btn22.place(x=140, y=10)

btn28 = Button(canvas_count_enemy, text='30', font=('Freestyle Script', 30), fg='lightgreen', width=30, bg='darkblue', command=count_enemy_1)
btn28.place(x=140, y=110)

btn29 = Button(canvas_count_enemy, text='40', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=count_enemy_2)
btn29.place(x=140, y=210)

btn30 = Button(canvas_count_enemy, text='60', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=count_enemy_3)
btn30.place(x=140, y=310)

btn31 = Button(canvas_count_enemy, text='100', font=('Freestyle Script', 30), fg='red', width=30, bg='darkblue', command=count_enemy_4)
btn31.place(x=140, y=410)

canvas_speed_bullet = Canvas(win, height=500, width=700, highlightthickness=0, bg='purple')

sky8 = PhotoImage(file=images['sky_main'])
canvas_speed_bullet.create_image(400, 250, image=sky8)

btn23 = Button(canvas_speed_bullet, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=from_speed_bullet_to_set)
btn23.place(x=140, y=10)

btn32 = Button(canvas_speed_bullet, text='3', font=('Freestyle Script', 30), fg='red', width=30, bg='darkblue', command=speed_bullet_1)
btn32.place(x=140, y=110)

btn33 = Button(canvas_speed_bullet, text='5', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=speed_bullet_2)
btn33.place(x=140, y=210)

btn34 = Button(canvas_speed_bullet, text='7', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=speed_bullet_3)
btn34.place(x=140, y=310)

btn35 = Button(canvas_speed_bullet, text='9', font=('Freestyle Script', 30), fg='lightgreen', width=30, bg='darkblue', command=speed_bullet_4)
btn35.place(x=140, y=410)

canvas_speed_enemy = Canvas(win, height=500, width=700, highlightthickness=0, bg='purple')

sky9 = PhotoImage(file=images['sky_main'])
canvas_speed_enemy.create_image(400, 250, image=sky9)

btn37 = Button(canvas_speed_enemy, text='Назад', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=from_speed_enemy_to_set)
btn37.place(x=140, y=10)

btn38 = Button(canvas_speed_enemy, text='1', font=('Freestyle Script', 30), fg='lightgreen', width=30, bg='darkblue', command=speed_enemy_1)
btn38.place(x=140, y=110)

btn39 = Button(canvas_speed_enemy, text='2', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=speed_enemy_2)
btn39.place(x=140, y=210)

btn40 = Button(canvas_speed_enemy, text='3', font=('Freestyle Script', 30), fg='orange', width=30, bg='darkblue', command=speed_enemy_3)
btn40.place(x=140, y=310)

btn41 = Button(canvas_speed_enemy, text='4', font=('Freestyle Script', 30), fg='red', width=30, bg='darkblue', command=speed_enemy_4)
btn41.place(x=140, y=410)

win.mainloop()
