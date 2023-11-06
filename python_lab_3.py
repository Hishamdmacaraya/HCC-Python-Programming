#Python Lab 1
#Coder: Hisham D Macaraya

#Write a Python program to print your name 10 times.

for i in range(10):
    print("My name is Hisham Macaraya")


#Write a Python program to print the numbers 1 to 20.

for i in range(1, 21):
    print(i, end = " ")


#Write a Python program to print all alphabets from a to z.

for i in range(97, 123):
    print(chr(i), end = " ")


#Write a Python program to print all even numbers between 1 to 100.

for i in range(2, 101, 2):
    print(i, end = " ")


#Write a Python program to print all the numbers in between First and Last limit. Take First limit and Last limit as a number from user as Input.

first = int(input("Enter the first number: ", ))
last = int(input("Enter the last number: ", ))

for i in range(first, last + 1):
    print(i, end = " ")


#Write a Python program to generate the multiplication table of a number entered by the user.

number = int(input("Enter a number: ", ))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


#Write a Python program that determines the nth Fibonacci number, given the first two numbers.

a, b = 0, 1
n = int(input("Enter a number: ", ))
for i in range(n - 1):
    a, b = b, a + b
print("Fibonacci number", n, "is:  ", b)


#Write a Python program to display the Fibonacci sequence of first n numbers entered by the user. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21.

first = 0
second = 1
n = int(input("Enter a number: ", ))

print("The sequence of fibonacci number", n, "is: \n")     
for i in range(0, n + 1):
    if i <= 1:
        next = i
    else:
        next = first + second
        first = second
        second = next
    print(next, end = " ")

