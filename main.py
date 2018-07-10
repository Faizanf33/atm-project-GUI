########################
# GUI-Author: Nauman Afsar, Faizan Ahmad
# Date: 27-03-2018
#########################

#########################
# importing Libraries
#########################
# import tkinter as tk        # Python 3: "t" lower-case

from tkinter import Menu
from tkinter import ttk, messagebox
from tkinter import *
import logging, os
##########################
#importing files
########################
from Data.data import data

try:
    Path = os.path.join('temp', 'info.log')
    logging.basicConfig(format='[ATM]:[%(asctime)s]:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG, filename=Path)

except (IOError or FileNotFoundError):
    os.mkdir('temp')
    Path = os.path.join('temp', 'info.log')
    logging.basicConfig(format='[ATM]:[%(asctime)s]:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG, filename=Path)


root = Tk()

def windows_size():
    root.update()                        # to get runtime size
    logging.info('setting width={} and height={}'.format(root.winfo_width(), root.winfo_height()))

def resize_window():
    w, h = 500, 400

    #to open window in the centre of screen
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x_axis = (ws/2) - (w/2)
    y_axis = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
    # disable resizing the GUI
    root.resizable(0,0)

def quit():
    logging.debug('closing main window')
    root.quit()
    root.destroy()
    exit()

def new_account():
    logging.debug('user selected create new account')
    import Data.new_acc_gui

def login():
    logging.debug('user selected login')
    d = data()
    Username, Pin = username.get(), pin.get()
    if Username in d.keys():
        logging.debug('username match found in data with name : {}'.format(d[Username][2]))
        if Pin == d[Username][5]:
            logging.debug('user entered correct pin')
            username.delete(0, END)
            pin.delete(0, END)
            messagebox.showinfo('Successfull', 'Welcome {} to atm service.'.format((d[Username][2]).upper()))

        else:
            pin.delete(0, END)
            messagebox.showwarning('Unsuccessfull', 'Invalid PIN!')
            logging.warning('user entered incorrect pin')

    else:
        username.delete(0, END)
        pin.delete(0, END)
        logging.warning('no match found with username:{}'.format(Username))
        messagebox.showwarning('Unsuccessfull', 'Invalid Username! No match found')

root.title("ATM Project")

# Menu Bar
menuBar = Menu()
root.config(menu = menuBar)

# Menu Items

filemenu = Menu(menuBar, tearoff = 0)
filemenu.add_command(label = "New", command=new_account)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = quit) #Calling the quit function
menuBar.add_cascade(label = "File", menu = filemenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)
# ---------------------------------------------------------------

# Tab Control / Notebook introduced here ------------------------
tabControl = ttk.Notebook(root)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='My ATM')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Instructions')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible

# ---------------------------------------------------------------
instr = ttk.LabelFrame(tab2, text='This Tab will be containing all the Instruction we are going to have for our program!')

# using the tkinter grid layout manager
instr.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(instr, text="All The Instructions are as follows: \n 1. If you are reading this then it means that you have downloaded this file. \n 2. Install Python3 on your system if you haven't already. \n 3. Install tkinter module in order to run the GUI of this program \n 4. If you are having any issues than please report it so we can fix it!").grid(column=0, row=0, sticky='W')

ttk.Label(tab1,text="Enter Username: ", font='none 12').grid(row=0, sticky="W")
username = Entry(tab1)
username.grid(row=0, column=2)
bullet = "\u2022"
ttk.Label(tab1, text="Enter PIN: ", font='none 12').grid(row=1, sticky="W")
pin = Entry(tab1, show=bullet)
pin.grid(row=1, column=2)
# ---------------------------------------------------------------

#Add buttons---------------------------
Button(root, text='LOGIN', bg='deep sky blue', font='none 12 bold', command=login).pack(side='top', padx=4, pady=4, fill='both')
Button(root, text='CREATE NEW ACCOUNT', bg='pale green', font='none 12 bold', command=new_account).pack(padx=4, pady=4, fill='both')


#Copyright label-----------------------------------------------------
cp = Label(root, text="Copyright {} 2018 \tFaizan Ahmad & Nauman Afsar Joint Project".format(chr(0xa9)), relief=SUNKEN, anchor=W, bg='LightCyan2')
cp.pack(fill=X)
# -------------------------------------------------------------------------------------


#======================
# Start GUI
#======================
# windows_size()
resize_window()
# print()
# windows_size()
root.mainloop()
