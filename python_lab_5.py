print()
print("Python Lab 4")
print("Coder: Hisham D Macaraya")
print()


'''
Problem 1
Write a Python program to store 5 integer numbers in a list. 
Take these numbers as input from user. 
Finally display the sum of these 5 numbers.
'''

print("Solution 1")
print()

numbers = [] #Empty list
for i in range(5): #Limit the number of inputs to 5
    number = int(input("Enter an integer number: "))
    numbers.append(number)

# Calculate the sum of the numbers
sum_of_numbers = sum(numbers)

#Display the numbers
print("Numbers:", numbers, end = "\n\n")

# Display the sum
print("Sum of the numbers:", sum_of_numbers)
print()


'''
Problem 2
Write a Python program to display the number stored on index 3, 
entered by the user in problem 1.
'''

print("Solution 2")
print()

# Display the number stored on index 3
print("Number stored on index 3:", numbers[3])
print()


'''
Problem 3
Write a Python program to search and display the largest element in the list entered by the user in problem 1.
'''

print("Solution 3")
print()

# Display the largest element in the list
print("Largest element in the number list:", max(numbers))
print()


'''
Problem 4
Write a Python program to search and display the smallest element in the list entered by the user in problem 1.
'''

print("Solution 4")
print()

# Display the smallest element in the list
print("Smallest element in the number list:", min(numbers))
print()


'''
Problem 5
Write a Python program to sort an integer list of 5 numbers.(Use problem 1 and apply selection sort)
'''

print("Solution 5")
print()

# Display the unsorted list
print("Unsorted list:", numbers)
print()

# Sort the list
sorted_list = numbers.sort()

# Display the sorted list
print("Sorted list:", numbers)