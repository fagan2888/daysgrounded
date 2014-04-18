#!/usr/bin/env python
# -*- coding: latin-1 -*-

"""
blablabla
"""

from datetime import date
import pickle
import sys
from os import path
import Tkinter as tk
import ttk
import tkMessageBox

import config as cfg

def update_file(childs, last_upd):
    """
    blablabla
    """
    with open(cfg.DATA_FILE, 'wb') as f_out:
        pickle.dump(childs, f_out)
        pickle.dump(last_upd, f_out)
    if LOG:
        with open(cfg.LOG_FILE, 'ab') as f_out:
            pickle.dump([childs, last_upd], f_out)

def create_file():
    """
    blablabla
    """
    # use lower case letters or names
    childs = {'t': 0, 's': 0}
    last_upd = date.today()
    update_file(childs, last_upd)
    return childs, last_upd

def read_file():
    """
    blablabla
    """
    with open(cfg.DATA_FILE, 'rb') as f_in:
        childs = pickle.load(f_in)
        last_upd = pickle.load(f_in)
    return childs, last_upd

def print_state(childs, last_upd):
    """
    blablabla
    """
    for child in childs:
        print child, childs[child],
    print str(last_upd)

def usage():
    """
    blablabla
    """
    return """
NOME E OBJETIVO

       days_grounded - gerir dias de castigo da(s) criança(s)

LINHA DE COMANDO

       days_grounded [OPÇÃO | CRIANÇA+/-DIAS...]

       -h, --help
              Esta informação de como usar days_grounded

       -a, --auto
              Atualização automática dos castigo, baseada na data

       -v, --version
              Mostra a versão da aplicação

       -l, --license
              Mostra a licença

       CRIANÇA+/-DIAS
              eg. t+1 s-1
    """

def banner():
    """
    blablabla
    """
    return """
    days_grounded version x.x.x, Copyright (C) 2014 Joao Carlos Roseta Matos
    days_grounded comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions; type 'days_grounded -l' for details.
    """

def show_license():
    """
    blablabla
    """
    with open('LICENSE.txt') as f_in:
        print f_in.read()

def man_upd_days(childs, last_upd):
    """
    blablabla
    """
    # check args
    for arg in sys.argv[1:]:
        if '-' in arg:
            child, days = str.lower(arg).split('-')
        elif '+' in arg:
            child, days = str.lower(arg).split('+')
        else:
            args_ok = False
            break

        try:
            days = int(days)
        except ValueError:
            args_ok = False
            break

        if (child in childs.keys()) and (-MAX_DAYS <= days <= MAX_DAYS):
            args_ok = True
        else:
            args_ok = False
            break

    # process args
    if args_ok:
        print_state(childs, last_upd)

        for arg in sys.argv[1:]:
            child = str.lower(arg[0])
            days = int(arg[1:])

            childs[child] += days
            if childs[child] > 0:
                childs[child] = min(MAX_DAYS, childs[child])
            else:
                childs[child] = max(0, childs[child])

        last_upd = date.today()

        update_file(childs, last_upd)
        print_state(childs, last_upd)
    else:
        print 'Erro: argumento incorreto', arg
        print usage()

def auto_upd_days(childs, last_upd):
    """
    blablabla
    """
    print_state(childs, last_upd)

    right_now = date.today()
    days_to_remove = (right_now - last_upd).days

    for child in childs:
        childs[child] -= days_to_remove
        childs[child] = max(0, childs[child])

    last_upd = right_now

    update_file(childs, last_upd)
    print_state(childs, last_upd)

def plus_btn(*args):
    """
    blablabla
    """
    if int(days_var.get()) < 0:
        days_var.set(0)
    else:
        days_var.set(min(MAX_DAYS, int(days_var.get()) + 1))

def minus_btn(*args):
    """
    blablabla
    """
    if int(days_var.get()) > MAX_DAYS:
        days_var.set(MAX_DAYS)
    else:
        days_var.set(max(0, int(days_var.get()) - 1))

def days_scale_chg(*args):
    """
    blablabla
    """
    days_var.set(int(float(days_var.get()))) # fix increment to integer

def childs_combo_chg(*args):
    """
    blablabla
    """
    global child
    global prev_child

    try:
        int(days_var.get())
    except ValueError:
        days_var.set(0)

    if 0 <= int(days_var.get()) <= MAX_DAYS:
        childs[prev_child] = int(days_var.get())

        child = prev_child = childs_combo.get()
        days_var.set(childs[child])
    else:
        childs_combo.set(prev_child)

        tkMessageBox.showwarning('AVISO',
                                 'O número de dias tem que estar entre 0 e ' +
                                 MAX_DAYS_STR)

def set_upd_btn(upd):
    """
    blablabla
    """
    global last_upd

    try:
        int(days_var.get())
    except ValueError:
        days_var.set(0)

    if 0 <= int(days_var.get()) <= MAX_DAYS:
        childs[childs_combo.get()] = int(days_var.get())

        if upd:
            days_to_remove = (date.today()- last_upd).days

            for child in childs:
                childs[child] -= days_to_remove
                childs[child] = max(0, childs[child])

        last_upd = date.today()
        last_upd_var.set(value=str(last_upd))

        update_file(childs, last_upd)
    else:
        tkMessageBox.showwarning('AVISO',
                                 'O número de dias tem que estar entre 0 e ' +
                                 MAX_DAYS_STR)

def confirm_exit():
    """
    blablabla
    """
    if tkMessageBox.askokcancel("Sair", "Tem a certeza que pretende sair?"):
        root.destroy()

def digits_only(up_down, idx, value, prev_val, char, val_type, source, widget):
    """
    blablabla
    """
    return char in '0123456789' and len(value) <= len(cfg.MAX_DAYS_STR)

def center(window):
    """
    blablabla
    """
    window.update_idletasks()
    width = window.winfo_width()
    frm_width = window.winfo_rootx() - window.winfo_x()
    win_width = width + 2 * frm_width
    height = window.winfo_height()
    titlebar_height = window.winfo_rooty() - window.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = window.winfo_screenwidth() // 2 - win_width // 2
    y = window.winfo_screenheight() // 2 - win_height // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    if window.attributes('-alpha') == 0:
        window.attributes('-alpha', 1.0)
    window.deiconify()

def show_help(*args):
    """
    blablabla
    """
    tkMessageBox.showinfo('Ajuda', usage())

if __name__ == '__main__':
    print banner()

    if path.isfile(cfg.DATA_FILE): # if file exists
        childs, last_upd = read_file()
    else:
        childs, last_upd = create_file()

    if len(sys.argv) > 1:
        arg1 = str.lower(sys.argv[1])
        if arg1 in ['-h', '--help']:
            usage()
        elif arg1 in ['-a', '--auto']:
            auto_upd_days(childs, last_upd)
        elif arg1 in ['-v', '--version']:
            print __version__
        elif arg1 in ['-l', '--license']:
            show_license()
        else:
            man_upd_days(childs, last_upd)
    else:
        root = tk.Tk()
        root.withdraw()
        win = tk.Toplevel(root)

        # for exit confirmation
        win.protocol("WM_DELETE_WINDOW", confirm_exit)

        win.title('Dias de castigo')

        # not resizable
        win.resizable(False, False)

        # resizable (limits)
        #win.minsize(250, 125)
        #win.maxsize(500, 250)

        # needed by center function?
        #win.attributes('-alpha', 0.0)

        win.bind("<F1>", show_help)
        win.bind("+", plus_btn)
        win.bind("-", minus_btn)

        # menu
        win.option_add('*tearOff', False)
        menubar = tk.Menu(win)
        win.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        helpmenu = tk.Menu(menubar)

        menubar.add_cascade(label="Ficheiro", menu=filemenu, underline=0)
        menubar.add_cascade(label="Ajuda", menu=helpmenu, underline=0)

        filemenu.add_command(label="Sair", underline=0, command=confirm_exit)

        helpmenu.add_command(label="Ajuda", underline=0, command=show_help,
                                                         accelerator='F1')
        helpmenu.add_separator()
        helpmenu.add_command(label="Sobre", underline=0, state='disabled')

        # ToDo: log menu item
##        filemenu.add_separator()
##        check = StringVar(value=1)
##        filemenu.add_checkbutton(label='Log', variable=check, onvalue=1,
##                                 offvalue=0)

        frame = ttk.Frame(win, padding='3 3 3 3')
        frame.grid(column=0, row=0, sticky='WNES')

        # if the main window is resized, the frame should expand
        #frame.columnconfigure(0, weight=1)
        #frame.rowconfigure(0, weight=1)

        prev_child = child = childs.keys()[0]

        child_lbl = tk.StringVar(value='Criança:')
        last_upd_lbl = tk.StringVar(value='Última atualização:')

        days_var = tk.StringVar(value=childs[child])
        last_upd_var = tk.StringVar(value=str(last_upd))

        # 1st row
        ttk.Button(frame, text='+', command=plus_btn).grid(column=3, row=1)

        days_scale = ttk.Scale(frame, orient=tk.VERTICAL, length=100,
                               from_=cfg.MAX_DAYS, to=0, command=days_scale_chg,
                               variable=days_var)
        days_scale.grid(column=4, row=1, rowspan=3)

        # 2nd row
        ttk.Label(frame, textvariable=child_lbl).grid(column=1, row=2)

        childs_combo = ttk.Combobox(frame, state='readonly', #width=10,
                                    values=childs.keys())
        childs_combo.grid(column=2, row=2)
        childs_combo.set(child)
        childs_combo.bind('<<ComboboxSelected>>', childs_combo_chg)

        # validate command, used below by some widgets
        vcmd = (win.register(digits_only),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        days_entry = ttk.Entry(frame, width=len(cfg.MAX_DAYS_STR) + 1,
                               justify=tk.RIGHT, textvariable=days_var,
                               validate='key', validatecommand=vcmd)
        days_entry.grid(column=3, row=2) #, sticky='WE') for expanding

        tk.Spinbox(frame, from_=0, to=cfg.MAX_DAYS,
                   width=len(cfg.MAX_DAYS_STR) + 1, justify=tk.RIGHT,
                   textvariable=days_var, validate='key',
                   validatecommand=vcmd).grid(column=5, row=2)

        # 3rd row
        ttk.Button(frame, text='-', command=minus_btn).grid(column=3, row=3)

        # 4th row
        # lambda is necessary so that the function is called on button creation
        ttk.Button(frame, text='Atualizar',
                   command=lambda: set_upd_btn(upd=True)).grid(column=1, row=4)

        ttk.Label(frame, textvariable=last_upd_lbl).grid(column=2, row=4,
                                                         sticky='E')

        ttk.Label(frame, textvariable=last_upd_var).grid(column=3, row=4,
                                                         sticky='W')

        ttk.Button(frame, text='Atribuir',
                   command=lambda: set_upd_btn(upd=False)).grid(column=4, row=4,
                                                                columnspan=2)

        # remove if windows is non resizable
        #ttk.Sizegrip(frame).grid(column=999, row=999, sticky=(E,S))

        # padding around all widgets
        for widget in frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        days_entry.focus()

        # center window
        center(win)

        root.mainloop()

# show widget options
# print info_lbl.configure()

#texto['state'] = 'disabled'
