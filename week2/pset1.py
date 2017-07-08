def calculate(balance, annualInterestRate, monthlyPaymentRate):

    #vars
    counter = 0

    #loop
    while counter <= 11:
        montlhyPayment = balance * monthlyPaymentRate
        balance = balance - montlhyPayment
        interest = annualInterestRate / 12 * balance
        balance = balance + interest
        counter += 1

    return "Remaining balance: ".format(round(balance,2))



print(calculate(484,0.2,0.04, 0))