#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5


def main():

    stringElement = input("give me a text to work on: ")
    counter = 0

    if len(stringElement) > 0:

        for char in stringElement:

            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                counter += 1

        print("Number of vowels: ", counter)
        return

    else:
        print("Don't have text")
        return


if __name__ == '__main__':
    main()