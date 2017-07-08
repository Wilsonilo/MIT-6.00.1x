low = 0
high = 100
mid = int(high / 2)
c = False
print("Please think of a number between 0 and 100!")
while c == False:
    print("Is your secret number {}?".format(mid))
    responseUser = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if str(responseUser) == 'c' or str(responseUser) == 'l' or str(responseUser) == 'h':

        if str(responseUser) == 'c':
            print("Game over. Your secret number was: {}".format(mid))
            c = True
            break
        elif str(responseUser) == 'h':
            high = mid

        elif str(responseUser) == 'l':
            low = mid

        mid = int((low + high) / 2)

    else:
        print("Sorry, I did not understand your input.")