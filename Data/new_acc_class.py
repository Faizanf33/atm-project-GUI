import logging
from Data.acc_no_gen import account_no_gen


class NewAccount:
    balance = 0.00

    def __init__(self, first_name, last_name, father_name, cnic, username, acc_type, middle_name = None):
        logging.debug("creating a new account")
        self.first_name = first_name
        self.last_name = last_name
        self.cnic = cnic
        self.father_name = father_name
        self.username = username
        self.acc_type = acc_type
        self.middle_name = middle_name

    def full_name(self):
        logging.info("checking first name...")
        if self.first_name.isalpha():
            logging.info("checking last name...")

            if self.last_name.isalpha():
                if self.middle_name:
                    logging.debug("checking middle name {}".format(self.middle_name))

                    if self.middle_name.isalpha():
                        logging.debug("name is cheked, returning full name")
                        self.fullname = self.first_name+" "+self.middle_name+" "+self.last_name
                        return True

                    else:
                        logging.warning("middle name invalid : '{}'".format(self.middle_name))
                        return False

                else:
                    logging.info("return full name with no middle name")
                    self.fullname = self.first_name+" "+self.last_name
                    return True

            else:
                logging.warning("last name invalid : '{}'".format(self.last_name))
                return False

        else:
            logging.warning("first name invalid : '{}'".format(self.first_name))
            return False

    def get_account_no(self):
        name = self.fullname
        if name:
            logging.info("creating account number using name :{}".format(name))
            self.account_no = account_no_gen(name)
            return True

        else:
            logging.info('account number could not be created...')
            return False


    def cnic_check(self):
        logging.debug("checking CNIC : {}".format(self.cnic))
        if (len(self.cnic) == 13) and (self.cnic.isdigit()):
            logging.info('CNIC checked...')
            return ("{}-{}-{}".format(self.cnic[0:5], self.cnic[5:12], self.cnic[12]))

        else:
            logging.warning("invalid CNIC : {}".format(self.cnic))
            return False
