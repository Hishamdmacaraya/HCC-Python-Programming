print()
print("Python Lab 4")
print("Coder: Hisham D Macaraya")
print()


'''
Problem 1
Write a Python program to create the following pattern

*
* *
* * *
* * * *
* * * * *
'''

print("Solution 1:")
print()

def asterisk_pattern():
    for i in range(1, 6): #Number of rows specified
        for j in range(i):
            print("*", end = "")
        print()

asterisk_pattern() #Function called to print the pattern
print()


'''
Problem 2
Write a Python program to create the following pattern

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

print("Solution 2:")
print()

def num_pattern():
    for i in range(1, 6): #Number of rows specified
        for j in range(i):
            num = j + 1 #Number to be printed
            print(num, end = "")
        print()

num_pattern() #Function called to print the pattern
print()


'''
Problem 3
Write a Python program to create the following pattern:

1 
2 3 
4 5 6 
7 8 9 10
11 12 13 14 15
'''

print("Solution 3:")
print()

def num_pattern2(max_num):
    num = 1 #Number Container
    current_row = 1 #Current Row Container
    while num <= max_num: 
        for i in range(current_row):
            print(num, end = " ")
            num += 1
            if num > max_num:
                break

        print()
        current_row += 1

max_num = 15 #Max number of the pattern

num_pattern2(max_num) #Function called to print the pattern
print()


'''
Problem 4
Write a Python program to create the following pattern

        *
       * *
      * * *
    * * * * *
  * * * * * * * 
'''

print("Solution 4:")
print()

def asterisk_diamond(rows):

    for i in range(rows): #Upper side of the diamond
        print(" ", " "*(rows-i-1) + "* "*(i+1))

    for i in range(rows + 2): #Middle row
        print("*", end = " ")
    print()

    for i in range(rows): #Lower side of the diamond
        print(" ", " "*(i) + "* "*(rows-i))


rows = 7 #Number of rows specified
asterisk_diamond(rows) #Function called to print the pattern
print()


'''
Problem 5
Write a Python program to create the following pattern

        *
       * *
      * * *
    * * * * *
  * * * * * * * 
    * * * * *
      * * *
       * *
        *
'''
print("Solution 5:")
print()

def asterisk_diamond(rows):

    for i in range(rows): #Upper side of the diamond
        print(" ", " "*(rows-i-1) + "* "*(i+1))

    for i in range(rows + 2): #Middle row
        print("*", end = " ")
    print()

    for i in range(rows): #Lower side of the diamond
        print(" ", " "*(i) + "* "*(rows-i))


rows = 7 #Number of rows specified
asterisk_diamond(rows) #Function called to print the pattern

print()


'''
Problem 6
Write a Python program to create the following pattern

A
A B
A B C
A B C D
A B C D E
'''

print("Solution 6:")
print()

def alph_pattern():
    for i in range(1, 6): #Number of rows specified
        for j in range(i):
            num = j + 1 #Number to be printed
            char = chr(num + 64) # Convert number to corresponding uppercase letter
            print(char, end = "")
        print()

alph_pattern() #Function called to print the pattern

print()

'''
Problem 7
Write a Python program to create the following pattern

a
b c
d e f
g h i j
'''

print("Solution 7:")
print()

def alph_pattern2(max_number):
    number = 1
    current_row = 1
    while number <= max_number:
        for _ in range(current_row):
            char = chr(number + 96)
            print(char, end=" ")
            number += 1
            if number > max_number:
                break
        print()
        current_row += 1

max_number = 10 # The maximum number in the pattern

alph_pattern2(max_number) #Function called to print the pattern

print()

print("End of Python Lab 4")
print()