import ast
from datetime import datetime

def process_transaction(sent_data):
    try:
        amount = sent_data['amount']
        if  valid_transaction(sent_data):
            try:
                amount = float(amount)
            except:
                return "The request is invalid: 400 bad request"
            if amount > 0:
                if amount <= 20:
                    return CheapPaymentGateway(sent_data)
                elif amount > 20 and amount <= 500:
                    return ExpensivePaymentGateway(sent_data)
                elif amount > 500:
                    return PremiumPaymentGateway(sent_data)
        else:
            return "The request is invalid: 400 bad request"
    except Exception as e:
        print(e)
        return str(e)

def valid_credit_card_number(number):
    return len(number) == 16 and type(number) is str

def valid_card_holder(name):
    return name.isalpha()

def valid_expiration_date(date):
    exp_month, exp_year = map(int, date.split("/"))
    exp_year  = int("20" + str(exp_year))
    curr_month = datetime.today().month
    curr_year = datetime.today().year

    if curr_year > exp_year:
        return False
    elif curr_year < exp_year:
        return True
    elif curr_year == exp_year:
        return curr_month == exp_month
    else:
        return False


def valid_security_code(code):
    if code != "":
        return code.isnumeric() and len(code) == 3
    return True

def valid_transaction(sent_data):
    print(sent_data)
    if valid_credit_card_number(sent_data["ccnumber"]):
        print("Passed ccnumber")
        if valid_card_holder(sent_data["holder"]):
            print("Passed holder")
            if valid_expiration_date(sent_data["expirationdate"]):
                print("Passed expirationdate")
                if valid_security_code(sent_data["securitycode"]):
                    print("Passed securitycode")
                    return True
    return False

def PremiumPaymentGateway(data_to_be_processed):
    print("PremiumPaymentGateway")

    for i in range(3):
        print("Attempt Number : ", i)
        if True:
            return True
    return False

def ExpensivePaymentGateway(data_to_be_processed):
    print("ExpensivePaymentGateway")
    if True:
        return True
    return CheapPaymentGateway()

def CheapPaymentGateway(data_to_be_processed):
    print("CheapPaymentGateway")
    if True:
        return True
    return False
