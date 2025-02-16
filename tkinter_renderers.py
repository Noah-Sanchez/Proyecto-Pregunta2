import tkinter as tk
from str_src import wd
import random
from tkinter import ttk
from lorddanlib import parse_string_to_list as p_str

btbgcol = "#6BC08E"
bgcol = "#7BD09E"
bord = False
full = False
it = 1
correctas = 0


def window_mode(win, key):
    global bord
    global full
    if key == 1:
        bord = not bord
        win.overrideredirect(bord)
    elif key == 2:
        full = not full
        win.attributes("-fullscreen", full)


class Respuesta:
    def change_value(self, hola):
        self.value = hola

    def __init__(self, win):
        self.button = tk.Button(win)
        self.value = True


def do_check(win, pgrs, nextbut, botones, value):
    for i in botones:
        if i.value:
            i.button.config(bg="#00BF00", command='')
            print("c_corr")
        else:
            i.button.config(bg="#BF0000", command='')
            print("c_incorr")
        print("Unlock")
    if value:
        pgrs.bar.step(100/15)
        global correctas
        correctas += 1
    nextbut.config(command=lambda: pgrs.do_it(win), bg=btbgcol)


class Progreso:
    def __init__(self, win):
        self.bar = ttk.Progressbar(
            win, orient="horizontal", mode="determinate")
        self.countt = 1

    def do_it(self, win):
        self.countt = self.countt + 1
        print("upt")
        game_upt(win, self)


def frame_call(frame_index, win):
    ele_list = win.winfo_children()
    for x in range(len(ele_list)):
        ele_list[x].grid_forget()

    if frame_index == 0:
        do_menu(win)
    elif frame_index == 1:
        do_game(win)
    elif frame_index == 2:
        do_credits(win)
    elif frame_index == 3:
        do_config(win)
    elif frame_index == 4:
        do_lesgo(win)


def game_upt(win, pgrs):

    print(pgrs.countt)
    ele_list = win.winfo_children()
    for x in range(len(ele_list)):
        ele_list[x].grid_forget()

    dict_str = "Pregunta " + str(pgrs.countt)
    if(dict_str == 'Pregunta 16'):
        frame_call(4, win)
    else:
        dict_src = p_str(wd[dict_str], "&")
        preglbl = tk.Label(win, text=dict_src[0], font=(
            'Helvetica bold', 30), bg=bgcol)
        preglbl.grid(column=0, row=0, columnspan=3)
        del dict_src[0:1]
        random.shuffle(dict_src)

        but_next = tk.Button(win, text="Siguiente", font=('Helvetica bold', 20),
                             fg="#FF0000", bg=bgcol)
        but_next.grid(column=0, row=6)

        but_sal = tk.Button(win, text="Salir", font=('Helvetica bold', 20),
                            fg="#FF0000", command=lambda: win.destroy(), bg=btbgcol)
        but_sal.grid(column=2, row=6)

        botones = []
        boton1 = Respuesta(win)
        boton1.button.config(text=dict_src[0], font=(
            'Helvetica bold', 20), bg=btbgcol, command=lambda: do_check(win, pgrs, but_next, botones, boton1.value))
        boton2 = Respuesta(win)
        boton2.button.config(text=dict_src[1], font=(
            'Helvetica bold', 20), bg=btbgcol, command=lambda: do_check(win, pgrs, but_next, botones, boton2.value))
        boton3 = Respuesta(win)
        boton3.button.config(text=dict_src[2], font=(
            'Helvetica bold', 20), bg=btbgcol, command=lambda: do_check(win, pgrs, but_next, botones, boton3.value))
        boton4 = Respuesta(win)
        boton4.button.config(text=dict_src[3], font=(
            'Helvetica bold', 20), bg=btbgcol, command=lambda: do_check(win, pgrs, but_next, botones, boton4.value))
        botones = [boton1, boton2, boton3, boton4]

        pgrs.bar.grid(column=0, row=1, columnspan=3)

        for i in range(4):
            if "*" in dict_src[i]:
                botones[i].change_value(True)
                botones[i].button.config(
                    text=dict_src[i].replace("*", " ").strip())
                botones[i].button.grid(column=0, row=i + 2, columnspan=3)
            else:
                botones[i].change_value(False)
                botones[i].button.grid(column=0, row=i + 2, columnspan=3)


def do_lesgo(win):

    win.columnconfigure((0, 2), weight=1)
    win.columnconfigure(1, weight=3)
    win.rowconfigure((0, 2, 3), weight=1)
    win.rowconfigure(1, weight=3)
    if(correctas == 15):
        namelbl = tk.Label(win, text='Puntuacion perfecta, \n ¡Felicidades!' + str(correctas),
                           font=("Copperplate", 30), bg=bgcol)
        namelbl.grid(row=1, column=1)
    else:
        namelbl = tk.Label(win, text='Puntuacion: ' + str(correctas),
                           font=("Copperplate", 30), bg=bgcol)
        namelbl.grid(row=1, column=1)

    ret_but = tk.Button(win, text="Creditos", font=('Helvetica bold', 20),
                        bg=btbgcol, command=lambda: frame_call(2, win))
    ret_but.grid(row=2, column=1)


def do_game(win):
    global correctas
    correctas = 0
    win.columnconfigure((0, 1, 2), weight=1)
    win.rowconfigure(0, weight=2)
    win.rowconfigure((1, 2, 3, 4, 5, 6), weight=1)

    pgrss = Progreso(win)
    game_upt(win, pgrss)


def do_credits(win):

    win.columnconfigure((0, 2), weight=1)
    win.columnconfigure(1, weight=3)
    win.rowconfigure((0, 2, 3), weight=1)
    win.rowconfigure(1, weight=3)

    namelbl = tk.Label(win, text=wd["nombres"],
                       font=("Copperplate", 15), bg=bgcol)
    namelbl.grid(row=1, column=1)

    ret_but = tk.Button(win, text="Regresar al menu", font=('Helvetica bold', 20),
                        bg=btbgcol, command=lambda: frame_call(0, win))
    ret_but.grid(row=2, column=1)


def do_menu(win):

    win.columnconfigure((0, 1, 2), weight=1)
    win.rowconfigure(1, weight=2)
    win.rowconfigure((0, 2, 3, 4), weight=1)

    tit = tk.Label(win, text="Pregunta2\nTec",
                   font=('Copperplate', 30), bg=bgcol)
    tit.grid(column=0, row=1, columnspan=3)

    game_but = tk.Button(win, text="Iniciar juego", font=('Helvetica bold', 20),
                         bg=btbgcol, command=lambda: frame_call(1, win))
    game_but.grid(column=0, row=2, columnspan=3)

    cred_but = tk.Button(win, text="Créditos", font=('Helvetica bold', 20),
                         bg=btbgcol, command=lambda: frame_call(2, win))
    cred_but.grid(column=0, row=3, sticky=tk.N, columnspan=3)

    but_end = tk.Button(win, text="Salir", font=('Helvetica bold', 20),
                        fg="#FF0000", command=lambda: win.destroy(), bg=btbgcol)
    but_end.grid(column=2, row=4)

    but_conf = tk.Button(win, text="Config", font=('Helvetica bold', 20),
                         command=lambda: frame_call(3, win), bg=btbgcol)
    but_conf.grid(column=0, row=4)


def do_config(win):

    win.columnconfigure((0, 2), weight=1)
    win.columnconfigure(1, weight=1)
    win.rowconfigure((0, 2, 3), weight=1)
    win.rowconfigure(1, weight=1)

    bord_but = tk.Button(win, text="Ventana sin bordes", font=("Copperplate", 15), bg=btbgcol,
                         command=lambda: window_mode(win, 1))
    bord_but.grid(row=1, column=1)

    # full_but = tk.Button(win, text="Pantalla completa", font=("Copperplate", 15), bg=btbgcol,
    # command=lambda: window_mode(win, 2))
    #full_but.grid(row=2, column=1)

    ret_but = tk.Button(win, text="Regresar al menu", font=('Helvetica bold', 20),
                        bg=btbgcol, command=lambda: frame_call(0, win))
    ret_but.grid(row=4, column=1)
