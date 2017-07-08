def calculate(balance, annualInterestRate):

    #vars
    new_balance = balance
    monthlypayment = 0.01


    while new_balance > 0:


        for i in range(12):
            new_balance = new_balance - monthlypayment
            interest = annualInterestRate / 12 * new_balance
            new_balance = new_balance + interest

        if new_balance <= 0:
            break
        else:

            lower_bound = new_balance / 12
            interest = (annualInterestRate * new_balance) / 12
            upper_bound = interest + new_balance
            middle = ((lower_bound + upper_bound) / 2) / 12
            if middle < new_balance:
                monthlypayment += middle + 0.01
            else:
                monthlypayment += middle - 0.01
            print(new_balance, middle, monthlypayment)

            new_balance = balance

    print("Lowest Payments: {}".format(round(monthlypayment, 2)))

calculate(320000, 0.2)
