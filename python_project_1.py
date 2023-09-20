#Python Lab 1
#Coder: Hisham D Macaraya

#Problem 1: Write a program that converts a temperature given in Celsius into Fahrenheit.

print("Celsius to Fahrenheit Converter")
print()
celsius = float(input("Write the temperature in Celsius: ")) #Input Teperature in Celsius
fahrenheit = (9.0 / 5.0 * celsius) + 32.0 #Formula
print(fahrenheit)

#Problem 2: Rewrite the Problem 1 and take celsius value as an Input from user and convert in to fahrenhiet.

print("Fahrenheit to Celsius Converter")
print()
fahrenheit = float(input("Write the temperature in Fahrenheit: ")) #Input Teperature in Celsius
celsius = (5.0 / 9.0) * (fahrenheit - 32.0) #Formula
print(celsius)

#Problem 3: Write a program that computes the average of five exam scores. Print all scores and average.

exam_score1 = float(89.0) #Exam score 1
print("Exam Score 1: ", exam_score1)
exam_score2 = float(75.25) #Exam score 2
print("Exam Score 2: ", exam_score2)
exam_score3 = float(86.15) #Exam score 3
print("Exam Score 3: ", exam_score3)
exam_score4 = float(77.0) #Exam score 4
print("Exam Score 4: ", exam_score4)
exam_score5 = float(97.50) #Exam score 5
print("Exam Score 5: ", exam_score5)
exam_average_score = round(((exam_score1 + exam_score2 + exam_score3 + exam_score4 + exam_score5) / 5), 2) #Formula
print("Average Exam Score", exam_average_score)

#Problem 4: Rewrite Problem 3 and take 5 exam scores as input from user. All other requirements will remain same.

print("Exam Score Average Calculator")
print()
exam_score1 = float(input("Exam Score 1: ")) #Input exam score 1
exam_score2 = float(input("Exam Score 2: ")) #Input exam score 2
exam_score3 = float(input("Exam Score 3: ")) #Input exam score 3
exam_score4 = float(input("Exam Score 4: ")) #Input exam score 4
exam_score5 = float(input("Exam Score 5: ")) #Input exam score 5
exam_average_score = round(((exam_score1 + exam_score2 + exam_score3 + exam_score4 + exam_score5) / 5), 2) #Formula
print()
print("Average Exam Score", exam_average_score)

#Problem 5: Write program to compute a multiplication table of any number.

#Multiplication Table of 8. We can do a for loop, but it is not yet discussed in this module.
print("Multiplication Table of 8")
print()
multiple = 8 #The factor
#Multiplication Table
print("8 x 1 = ", multiple * 1)
print("8 x 2 = ", multiple * 2)
print("8 x 1 = ", multiple * 3)
print("8 x 1 = ", multiple * 4)
print("8 x 1 = ", multiple * 5)
print("8 x 1 = ", multiple * 6)
print("8 x 1 = ", multiple * 7)
print("8 x 1 = ", multiple * 8)
print("8 x 1 = ", multiple * 9)
print("8 x 1 = ", multiple * 10)

#Problem 6: Rewrite Problem 5, and take user input and display a table of user input.

#Multiplication Table. We can do a for loop, but it is not yet discussed in this module.
print("Multiplication Table")
print()
multiple = int(input("What is your mutliplier? ", )) #Input the factor
#Multiplication Table
print("8 x 1 = ", multiple * 1)
print("8 x 2 = ", multiple * 2)
print("8 x 1 = ", multiple * 3)
print("8 x 1 = ", multiple * 4)
print("8 x 1 = ", multiple * 5)
print("8 x 1 = ", multiple * 6)
print("8 x 1 = ", multiple * 7)
print("8 x 1 = ", multiple * 8)
print("8 x 1 = ", multiple * 9)
print("8 x 1 = ", multiple * 10)

