def calculate(balance, annualInterestRate):
    new_balance = balance
    monthlypayment = 0

    # loop to make the calculations for the year
    while new_balance > 0:

        for i in range(12):
            new_balance = new_balance - monthlypayment
            interest = annualInterestRate / 12 * new_balance
            new_balance = new_balance + interest
        if new_balance <= 0:
            break
        else:
            new_balance = balance
            monthlypayment += 10

    print("Lowest Payment: ", monthlypayment)

calculate(4773, 0.2)
