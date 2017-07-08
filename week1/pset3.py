#Assume s is a string of lower case characters.

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh

#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc


s = 'abcbcd'
alphabet = list('abcdefghijklmnopqrstuvwxyz')
final = ""
counter = 0
for letter in s:
    index_letter = counter
    index_letter_alp = alphabet.index(letter)
    index_next_letter = index_letter
    temp = letter

    while index_next_letter < len(s):
        index_next_letter += 1
        if index_next_letter < len(s):

            index_next_letter_in_alph = alphabet.index(s[index_next_letter])

            if index_next_letter_in_alph >= index_letter_alp:
                temp += s[index_next_letter]
                index_letter_alp = index_next_letter_in_alph
            else:
                break

    if len(temp) > len(final):
        final = temp


    counter += 1
print("Longest substring in alphabetical order is: ", final)