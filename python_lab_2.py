print("Python Lab 2")
print("Coder: Hisham D Macaraya")
print()

print("Problem 1: Odd or Even Checker") 
#Write a Python program to check if the number entered by the user is even or odd.

number = int(input("Enter a number: ", ))

if number % 2 == 0:
    print("The number", number, "is even.")
else:    
    print("The number", number, "is odd.")

print()

print("Problem 2: Highest Number Checker") 
#Write a Python program to find highest value of a number among three numbers. Take 3 numbers as input from the user. (Take first limit, last and then finally determine the number is smaller or grater then first or last number).

first = int(input("Enter the first number: ", ))
second = int(input("Enter the second number: ", ))
third = int(input("Enter the third number: ", ))

if first > second and first > third:
    print("The highest number is:", first)
elif second > first and second > third:
    print("The highest number is:", second)
else:                       
    print("The highest number is:", third)

print()

print("Problem 3: Positive or Negative Checker") 
#Write a Python program to check if the number entered by the user is positive or negative.

number = int(input("Enter a number: ", ))

if number > 0:      
    print("The number", number, "is positive.")

elif number < 0:
    print("The number", number, "is negative.")

else:   
    print("The number", number, "is zero.")

print()

print("Problem 4: Alphabet Checker") 
#Write a Python program to check if the character entered by the user is an alphabet or not.

character = input("Enter a character: ", )

if character.isalpha():
    print("The character", character, "is an alphabet.")

else:
    print("The character", character, "is not an alphabet.")

print()

print("Problem 5: Character Checker") 
#Write a Python program to check if the character entered by the user is an alphabet, digit or special character.

character = input("Enter a character: ", )

if character.isalpha():
    print("The character", character, "is an alphabet.")

elif character.isdigit():
    print("The character", character, "is a digit.")

else:
    print("The character", character, "is a special character.")