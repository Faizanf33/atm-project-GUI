from tkinter import *
from tkinter import messagebox, ttk
import logging, os, csv

from Data.encrypt import rot13
from Data.new_acc_class import NewAccount




def data_entry(Pin):
    filename = os.path.join('Data', 'userdata.csv')
    with open(filename, 'a') as data_file:
        fathername, name = rot13(user.father_name.lower()), rot13(user.full_name().lower())
        new = [user.username, user.get_account_no(), user.acc_type, name, fathername, user.cnic, Pin,  user.balance, 'NEW']
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
            messagebox.showinfo('Confirmation', "Dear {}! Your account is created successfully. Your account number is {}.".format(user.full_name(), user.get_account_no()))
            data_entry(Pin)
            window.quit()
            window.destroy()
            return

        else:
            window.bell()
            logging.warn('pin did not match')
            messagebox.showwarning('Failed' ,"Your PIN did not match!, Try again!")

    #----First Frame------
    Frame_2 = Frame(window)
    Frame_2.grid()


    #------empty label----------
    Label(Frame_2, text='CREATE NEW PIN', font="none 12 bold").grid(row=0, rowspan=2, column=1, columnspan=2, sticky=EW)
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
    finish_bt = Button(Frame_2, text="FINISH", bg="pale green", fg="black", font="none 12", relief=GROOVE, padx=15, bd=5, command=finish)
    finish_bt.grid(row=15, column=3, sticky=W+S)


    window.mainloop()


#-------MAIN WINDOW------------------------------
window = Tk()
window.title("Create New Account")
w = 400
h = 400

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x_axis = (ws/2) - (w/2)
y_axis = (hs/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x_axis, y_axis))
window.resizable(width=False, height=False)

def close():
    window.quit()
    window.destroy()
    return


def click(event=None):
    first, last, middle, father, CNIC = f_name.get(), l_name.get(), m_name.get(), ft_name.get(), cnic.get()
    global user

    Username, Acc_type = username.get(), acc_type.get()

    if Acc_type == 0:
        logging.info('user selected account type as Gold')
        Acc_type =  'Gold'

    else:
        logging.info('user selected account type as Silver')
        Acc_type = 'Silver'

    #sending data to NewAccount class
    user = NewAccount(first, last, father, CNIC, Username, Acc_type, middle)
    Full_name, CNIC = user.full_name(), user.cnic_check()

    if (Username == " ") or (Username.lower() == first.lower()) or (Username.lower() == last.lower()) or (Username.lower() == father.lower()):
        window.bell()
        logging.warn('user entered invalid username : {}'.format(Username))
        messagebox.showwarning('Failed', "Invalid username : {}. Please enter a unique username.".format(Username))


    elif not Full_name:
        window.bell()
        logging.warn('user entered invalid name')
        messagebox.showwarning('Failed', "Invalid Name!")

    elif not CNIC:
        window.bell()
        logging.warn('user entered invalid CNIC : {}'.format(CNIC))
        messagebox.showwarning('Failed', "Invalid CNIC Number!")

    else:
        logging.info('user entered correct information and now prompting user for pin...')
        window.quit()
        Frame_1.destroy()
        next_window()

#-----creating menus-----
my_menu = Menu(window)
window.config(menu=my_menu)

subMenu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label='Exit', command=close)

helpMenu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label='About ATM')
helpMenu.add_separator()
helpMenu.add_command(label='help create account')



#----First Frame------
Frame_1 = Frame(window)
Frame_1.grid()

#------empty label----------
Label(Frame_1, text='CREATE NEW ACCOUNT').grid(row=0, column=2, sticky=EW)

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

def limitSize(*args):
    value = limit.get()
    if len(value) > 13: limit.set(value[:13])


limit = StringVar()
limit.trace('w', limitSize)

#---entry for cnic----
cnic = Entry(Frame_1, bg="white", width=16, font="12", textvariable=limit)
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
next_bt = Button(Frame_1, text="NEXT", bg="pale green", fg="black", font="none 12", relief=GROOVE, padx=12, bd=5, command=click)
next_bt.grid(row=14, column=2,sticky=E)

#----button for exit-----
exit_bt = Button(Frame_1, text="EXIT", bg='light grey', fg='black', font="none 12", relief=GROOVE, padx=12, bd=5, command=close)
exit_bt.grid(row=14, column=3, sticky=W)

#------empty label---------
Label(Frame_1).grid(row=15, sticky=EW)

window.mainloop()
