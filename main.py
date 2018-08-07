########################
# GUI-Author: Nauman Afsar, Faizan Ahmad
# Date: 27-03-2018
#########################

#########################
# importing Libraries
#########################
# import tkinter as tk        # Python 3: "t" lower-case
from tkinter import *
from tkinter import ttk,messagebox
import tkinter, logging, os, csv
from Data.data import data
from Data.new_acc_class import NewAccount
from Data.encrypt import rot13

##########################
#importing files
########################

def exit():
    msg = messagebox.askquestion("CONFIRM","ARE YOU SURE YOU WANT TO EXIT?", icon='warning')
    if msg == "yes":
        root.deiconify()   #makes the root window visible again
        window.destroy()
        logging.info('exiting window')

    else:
        logging.info('window still running')

def new_account(event=None):

    def limitSize(*args):
        value = limit.get()
        if len(value) > 13: limit.set(value[:13])



    def data_entry(Pin):
        filename = os.path.join('Data', 'userdata.csv')
        with open(filename, 'a') as data_file:
            fathername, name = rot13(user.father_name.lower()), rot13(user.fullname.lower())
            new = [user.username, user.account_no, user.acc_type, name, fathername, user.cnic, Pin,  user.balance, 'NEW']
            csv.writer(data_file).writerow(new)
            logging.debug('writing data in file')
            data_file.close()
            logging.info('data written successfully in file : {}'.format('userdata.csv'))



    def next_window():
        window.title("PIN BOX")

        def finish():
            Pin, V_Pin = pin.get(), v_pin.get()
            if (Pin == V_Pin) and (len(Pin) == 4):
                logging.info('pin matched successfully')
                window.bell()
                logging.info('account no generated successfully')
                messagebox.showinfo('Confirmation', "Dear {}! Your account is created successfully. Your account number is {}.".format(user.fullname, user.account_no))
                data_entry(Pin)
                window.destroy()
                root.deiconify()
                return

            else:
                window.bell()
                logging.warning('pin did not match')
                messagebox.showwarning('Failed' ,"Your PIN did not match!, Try again!")

        #----First Frame------

        Frame_2 = Frame(window)
        Frame_2.grid()
        #------empty label----------
        Label(Frame_2, text='CREATE NEW PIN', font=("Microsoft Himalaya", 12, "bold")).grid(row=0, rowspan=2, column=1, columnspan=2, sticky=EW)
        Label(Frame_2).grid(row=2, sticky=EW)
        Label(Frame_2).grid(row=3, sticky=EW)
        Label(Frame_2).grid(row=4, sticky=EW)


        #------label for PIN-------
        Label(Frame_2, text="4-Digit PIN : ", font="none 12 bold").grid(row=5, column=0, sticky=W)
        Label(Frame_2, text="Verify PIN : ", font="none 12 bold").grid(row=6, column=0, sticky=W)






        def limitPin(*args):
            value = pinLimit.get()
            if len(value) > 4: pinLimit.set(value[:4])


        pinLimit = StringVar()
        pinLimit.trace('w', limitPin)

        def limitVerPin(*arg):
            value = verPinLimit.get()
            if len(value) > 4: verPinLimit.set(value[:4])

        verPinLimit = StringVar()
        verPinLimit.trace('w', limitVerPin)

        #------entry for PIN------
        logging.debug('creating entries...')
        bullet = "\u2022"
        pin = Entry(Frame_2, bg="white", width=20, font="12", show=bullet, textvariable=pinLimit)
        pin.grid(row=5, column=2, sticky=W)
        v_pin = Entry(Frame_2, bg="white", width=20, font="12", show=bullet, textvariable=verPinLimit)
        v_pin.grid(row=6, column=2, sticky=W)

        #------empty label----------
        Label(Frame_2).grid(row=7, sticky=EW)
        Label(Frame_2).grid(row=8, sticky=EW)
        Label(Frame_2).grid(row=9, sticky=EW)
        Label(Frame_2).grid(row=10, sticky=EW)
        Label(Frame_2).grid(row=11, sticky=EW)
        Label(Frame_2).grid(row=12, sticky=EW)
        Label(Frame_2).grid(row=13, sticky=EW)
        Label(Frame_2).grid(row=14, sticky=EW)

        logging.debug('creating buttons....')
        #----button for exit-----
        finish_bt = Button(Frame_2, text="FINISH", bg="pale green", fg="black", font="Jokerman 12", relief=GROOVE, padx=12, bd=2, command=finish)
        finish_bt.grid(row=15, column=3, sticky=W+S)

    def click(event=None):
        first, last, middle, father, CNIC = f_name.get(), l_name.get(), m_name.get(), ft_name.get(), cnic.get()
        global user

        Username, Acc_type = username.get(), acc_type.get()

        if Acc_type == 1:
            logging.info('user selected account type as Gold')
            Acc_type =  'Gold'

        else:
            logging.info('user selected account type as Silver')
            Acc_type = 'Silver'

        #sending data to NewAccount class
        user = NewAccount(first, last, father, CNIC, Username, Acc_type, middle)
        Full_name, CNIC = user.full_name(), user.cnic_check()

        if not Full_name:
            window.bell()
            logging.warn('user entered invalid name')
            messagebox.showwarning('Failed', "Invalid Name!")

        elif not CNIC:
            window.bell()
            logging.warn('user entered invalid CNIC : {}'.format(CNIC))
            messagebox.showwarning('Failed', "Invalid CNIC Number!")

        elif (Username == " ") or (Username.lower() == first.lower()) or (Username.lower() == last.lower()) or (Username.lower() == father.lower()):
            window.bell()
            logging.warn('user entered invalid username : {}'.format(Username))
            messagebox.showwarning('Failed', "Invalid username : {}. Please enter a unique username.".format(Username))

        else:
            user.get_account_no()
            logging.info('user entered correct information and now prompting user for pin...')

            Frame_1.destroy()
            next_window()



    global window
    window = Toplevel(root)
    root.withdraw()
    window.title("NEW ACCOUNT")

    w = 450
    h = 400
    window.protocol('WM_DELETE_WINDOW',exit) # if windows default cross button is pressed
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x_axis = (ws/2) - (w/2)
    y_axis = (hs/2) - (h/2)

    window.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
    window.resizable(width=False, height=False)
    icon = os.path.join('Data', 'icon.ico')
    try:

        window.iconbitmap(icon)
        imgicon = PhotoImage(file=icon)
        window.tk.call('wm', 'iconphoto', window._w, imgicon)

    except Exception as err:
        logging.warning(err)
        icon = os.path.join('Data', 'icon.gif')
        imgicon = PhotoImage(file=icon)
        window.tk.call('wm', 'iconphoto', window._w, imgicon)

    finally:
        pass

    #-----creating menus-----
    my_menu = Menu(window)
    window.config(menu=my_menu)

    subMenu = Menu(my_menu)
    my_menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label='Exit', command=window.destroy)

    helpMenu = Menu(my_menu)
    my_menu.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label='About ATM')
    helpMenu.add_separator()
    helpMenu.add_command(label='help create account')



    #----First Frame------
    Frame_1 = Frame(window)
    Frame_1.grid()

    #------empty label----------
    Label(Frame_1, text='CREATE NEW ACCOUNT', font=("Microsoft Himalaya", 12, "bold")).grid(row=0, column=2, sticky=EW)

    #----label for name------
    Label(Frame_1, text="First Name : ", font="none 12 bold").grid(row=1, column=0, sticky=W)
    Label(Frame_1, text="Middle Name : ", font="none 12 bold").grid(row=2, column=0, sticky=W)
    Label(Frame_1, text="(optional)", font="none 12 bold").grid(row=2, column=3, sticky=W)
    Label(Frame_1, text="Last Name : ", font="none 12 bold").grid(row=3, column=0, sticky=W)

    #------empty label----------
    Label(Frame_1).grid(row=4, sticky=EW)

    #---label for father name-----
    Label(Frame_1, text="Father's Name : ", font="none 12 bold").grid(row=5, column=0, sticky=W)

    #------empty label----------
    Label(Frame_1).grid(row=6, sticky=EW)

    #---label for cnic-----
    l_cnic = Label(Frame_1, text="13-Digit CNIC : ", font="none 12 bold").grid(row=7, column=0, sticky=W)
    Label(Frame_1, text="without (-)", font="none 12 bold").grid(row=7, column=3, sticky=W)

    #------empty label----------
    Label(Frame_1).grid(row=8, sticky=EW)

    #-----label for username------
    Label(Frame_1, text="Username : ", font="none 12 bold").grid(row=9, column=0, sticky=W)

    #------empty label----------
    Label(Frame_1).grid(row=10, sticky=EW)

    #-----label for account type------
    Label(Frame_1, text="Account Type : ", font="none 12 bold").grid(row=11, column=0, sticky=W)

    #-----entries for name-----
    logging.debug('creating entries....')
    f_name = Entry(Frame_1, bg="white", width=20, font="none 12")
    f_name.grid(row=1, column=2, sticky=W)
    m_name = Entry(Frame_1, bg="white", width=20, font="none 12")
    m_name.grid(row=2, column=2, sticky=W)
    l_name = Entry(Frame_1, bg="white", width=20, font="none 12")
    l_name.grid(row=3, column=2, sticky=W)
    ft_name = Entry(Frame_1, bg="white", width=20, font="none 12")
    ft_name.grid(row=5, column=2, sticky=W)



    limit = StringVar()
    limit.trace('w', limitSize)

    #---entry for cnic----
    cnic = Entry(Frame_1, validate="key", bg="white", width=16, font="12", textvariable=limit)
    cnic.grid(row=7, column=2, sticky=W)

    #-----entry for username-----
    username = Entry(Frame_1, bg="white", width=20, font="none 12")
    username.grid(row=9, column=2, sticky=W)


    #-----Radiobutton for account type-------
    logging.debug('creating buttons ....')
    acc_type = IntVar()
    Radiobutton(Frame_1, text="GOLD", variable=acc_type, value=1, font="none 10 bold", bg="gold").grid(row=11, column=2, sticky=W)
    Radiobutton(Frame_1, text="SILVER", variable=acc_type, value=2, font="none 10 bold", bg="silver").grid(row=11, column=2, sticky=E)


    #------empty label----------
    Label(Frame_1).grid(row=12, sticky=EW)
    Label(Frame_1).grid(row=13, sticky=EW)

    #----button for next-----
    next_bt = Button(Frame_1, text="NEXT", bg="pale green", fg="black", font="Jokerman 12", relief=GROOVE, padx=12, bd=2, command=click)
    next_bt.grid(row=14, column=2,sticky=E)

    #----button for exit-----
    exit_bt = Button(Frame_1, text="EXIT", bg='light grey', fg='black', font="Jokerman 12", relief=GROOVE, padx=12, bd=2, command=exit)
    exit_bt.grid(row=14, column=3, sticky=W)

    #------empty label----------
    Label(Frame_1).grid(row=15, sticky=EW)


try:
    Path = os.path.join('temp', 'info.log')
    logging.basicConfig(format='[ATM]:[%(asctime)s]:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG, filename=Path)

except (IOError or FileNotFoundError):
    os.mkdir('temp')
    Path = os.path.join('temp', 'info.log')
    logging.basicConfig(format='[ATM]:[%(asctime)s]:%(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG, filename=Path)



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


def windows_size():
    root.update()                        # to get runtime size
    logging.info('setting width={} and height={}'.format(root.winfo_width(), root.winfo_height()))

root = Tk()
root.title("ATM Project")

icon = os.path.join('Data', 'icon.ico')

w, h = 500, 400
#to open window in the centre of screen
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x_axis = (ws/2) - (w/2)
y_axis = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
# disable resizing the GUI
root.resizable(0,0)

try:
    root.iconbitmap(icon)
    imgicon = PhotoImage(file=icon)
    root.tk.call('wm', 'iconphoto', root._w, imgicon)

except Exception as err:
    logging.warning(err)
    icon = os.path.join('Data', 'icon.gif')
    imgicon = PhotoImage(file=icon)
    root.tk.call('wm', 'iconphoto', root._w, imgicon)

finally:
    pass

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

ttk.Label(tab1,text="Enter Username: ", font=("Palatino Linotype", 12, "bold")).grid(row=0, sticky="W")
username = Entry(tab1, font='none')
username.grid(row=0, column=2, padx=1, pady=2, ipadx=2, ipady=2)
bullet = "\u2022"
ttk.Label(tab1, text="Enter PIN: ", font=("Palatino Linotype", 12, "bold")).grid(row=1, sticky="W")

def LimitPin(*arg):
    value = PinLimit.get()
    if len(value) > 4: PinLimit.set(value[:4])

PinLimit = StringVar()
PinLimit.trace('w', LimitPin)

pin = Entry(tab1, show=bullet, font='none', textvariable=PinLimit)
pin.grid(row=1, column=2, padx=1, pady=2, ipadx=2, ipady=2)
# ---------------------------------------------------------------

#Add buttons---------------------------
Button(root, text='LOGIN', bg='deep sky blue', font='Jokerman 12', command=login).pack(side='top', padx=4, pady=4, fill='both')
Button(root, text='CREATE NEW ACCOUNT', bg='pale green', font='Jokerman 12', command=new_account).pack(padx=4, pady=4, fill='both')


#Copyright label-----------------------------------------------------
cp = Label(root, text=" Faizan Ahmad & Nauman Afsar Joint Project {} 2018".format(chr(0xa9)), relief=SUNKEN, anchor=W, bg='LightCyan2')
cp.pack(fill=X)

root.mainloop()
