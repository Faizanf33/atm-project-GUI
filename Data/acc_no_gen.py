from random import randint, randrange
from Data.data import data

def account_no_gen(user_name):
    d = data()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    acc_no = ''
    acc_no += str(len(d.keys()) + 10)
    for alpha in user_name:
        if (len(acc_no) < 12):
            if alpha in alphabets:
                index = alphabets.rfind(alpha)
                acc_no += str(index + 1)

            else:
                acc_no += '0'

        else:
            break

    if len(acc_no) > 12:
        final_acc_no = ''
        for index in acc_no:
            if len(final_acc_no) < 12:
                final_acc_no += index

        acc_no = final_acc_no
        return acc_no

    if len(acc_no) < 12:
        remain_index = 12 - len(acc_no)
        for index in range(remain_index):
            acc_no += str(randint(0,9))

        return acc_no

    else:
        return acc_no

def code():
    a = 'qwertyuiopasdfghjklzxcvbnm'
    conf_code = ''
    for i in range(3):
        conf_code += str(a[randrange(9)])+str(randrange(9))
    return conf_code
