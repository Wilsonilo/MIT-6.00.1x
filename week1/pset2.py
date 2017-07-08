# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2


index = 0
total = 0
for char in s:
    if char == 'b':
        if (index+2) < len(s):
            createBob = s[index] + s[index+1] + s[index+2]
            if createBob == "bob":
                total += 1
    index += 1

print("Number of times bob occurs is: ", total)