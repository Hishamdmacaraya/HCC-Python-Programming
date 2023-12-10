#Section 1: Introduction

#Import the necesary libraries
import turtle
import time
from math import *

win = turtle.Screen()
win.setup(1300,1100)
win.bgcolor('black')
win.tracer(0)

sun = turtle.Turtle()
sun.shape('circle')
sun.shapesize(5,5)
sun.color('yellow')

# Draw text on the upper left window
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(-550, 450)  # Adjust the coordinates as needed
text_turtle.color("white")
text_turtle.write("Solar System Mini-Dictionary", font=("Arial", 30, "bold"))

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.goto(-500, 400)  # Adjust the coordinates as needed
text_turtle.color("white")
text_turtle.write("by Hisham D Macaraya", font=("Arial", 20, "normal"))

class Planet(turtle.Turtle):
    def __init__(self,radius, color, size, star, offset):
        super().__init__(shape='circle')
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.size = size
        self.shapesize(size,size)
        #self.up()
        self.angle = 0
        self.star = star
        self.offset = offset
    

    def move(self):
        x = self.offset +  self.radius*cos(self.angle) # Angle in radians
        y = self.radius*sin(self.angle)*0.3 

        self.goto(self.star.xcor()+x,self.star.ycor()+y)


earth = Planet(300,'blue', 1, sun, 100)
mercury = Planet(110, 'grey', 0.6, sun, 0)
venus = Planet(180, 'orange', 0.8, sun, 50)
mars = Planet(400, 'red', 0.9, sun, 100)

moon = Planet(40, 'grey', 0.2, earth, 0) # Moon a 'planet' that revolves around earth
phobos = Planet(40, 'grey', 0.2, mars,0)
deimos = Planet(35, 'white', 0.2, mars, 0)

myList = [mercury, venus, earth, moon, mars, phobos, deimos]

for i in myList:
    i.penup()
    i.goto(i.radius+i.offset, 0)
    if i.star == sun:
        i.pendown()


# Main loop
for _ in range(1000):  # Replace 1000 with the number of iterations you want
    win.update()
    for i in myList:
        i.move()

    # Increase the angle by 0.0x radians (further away - smaller angle change)
    moon.angle += 0.06
    phobos.angle += 0.06
    deimos.angle += 0.08
    
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007

    time.sleep(0.01)

turtle.bye()  # Close the turtle window

#Section 2: Welcome Message
print() 

message = "Welcome to Solar System Mini-Dictionary"
length = len(message)

# Print top line of asterisks
for i in range(length + 4):
    print('*', end='')
print()

# Print message
print('*', message, '*')

# Print bottom line of asterisks
for i in range(length + 4):
    print('*', end='')
print()
print()
#Ask the user for his/her name
name = input("What is your name? ")
print()
print("Hello, " + name + ". Welcome to Solar System Mini-Dictionary!")

#Section 3: The Dictionary
print()

# Mini Dictionary Program in Python
print(name + ', ' + "Please search the Solar System words below: ")


# Initialize dictionary
dictionary = {}

# Function to add word to dictionary
def add_word(word, definition):
    dictionary[word.lower()] = definition

# Function to find a word in the dictionary
def find_word(word):
    if word in dictionary:
        print()
        return dictionary.get(word.lower())
        print()
    else:
        print()
        return "Word not found"
        print()

# Function to delete a word from the dictionary
def delete_word(word):
    if word in dictionary:
        del dictionary[word.lower()]
    else:
        print()
        return "Word not found"

# Function to search for a word in the dictionary
def search_word():
    while True:
        word = input("Enter a word to search: ")
        print(word, "-", find_word(word.lower()))
        another_query = input("Do you want to make another query? (yes/no): ")
        while another_query.lower() != 'yes' and another_query.lower() != 'no':
            print()    
            print("Invalid input. Please enter 'yes' or 'no'.")
            another_query = input("Do you want to make another query? (yes/no): ")
        if another_query.lower() == 'no':
            print()
            print("Exiting the search function... \nThank you for using the dictionary.")
            break

# Test the functions
add_word("Planet", "A celestial body moving in an elliptical orbit around a star.")
add_word("Sun", "The star at the center of the Solar System (our solar system), which shines in our sky, represented in astronomy and astrology by ☉.")
add_word("Moon", "The Earth's moon; the sole natural satellite of the Earth, represented in astronomy and astrology by ☾.")
add_word("Mercury", "The planet in the solar system with the closest orbit to the Sun, named after the god; represented by ☿")
add_word("Venus", "The planet in the solar system with the second closest orbit to the Sun, named after the goddess; represented by ♀")
add_word("Earth", "The planet in the solar system with the third closest orbit to the Sun, the only planet known to support life, named after the goddess; represented by ⊕")
add_word("Mars", "The planet in the solar system with the fourth closest orbit to the Sun, named after the god; represented by ♂")
add_word("Jupiter", "The planet in the solar system with the fifth closest orbit to the Sun, named after the god; represented by ♃")
add_word("Saturn", "The planet in the solar system with the sixth closest orbit to the Sun, named after the god; represented by ♄")
add_word("Uranus", "The planet in the solar system with the seventh closest orbit to the Sun, named after the god; represented by ♅")
add_word("Neptune", "The planet in the solar system with the eighth closest orbit to the Sun, named after the god; represented by ♆")
search_word()  # Prompts the user to enter a word and prints the definition

#Section 4: The Menu Options
print()

def option_menu():
    while True:
        print("\nMini Dictionary Options:")
        print("1. Add a word")
        print("2. Find a word")
        print("3. Delete a word")
        print("4. Exit")
        option = input("Choose an option (1-4): ")

        if option == '1':
            word = input("Enter a word to add: ")
            definition = input("Enter the definition: ")
            add_word(word, definition)
        elif option == '2':
            word = input("Enter a word to find: ")
            print(word, "-", find_word(word))
        elif option == '3':
            word = input("Enter a word to delete: ")
            delete_word(word)
        elif option == '4':
            break
        else:
            print("Invalid option. Please enter a number between 1 and 4.")

# Test the function
option_menu()

#Section 5: Thank you message
print()

message = "Thank you for using the Solar System Mini-Dictionary"
length = len(message)

# Print top line of asterisks
for i in range(length + 4):
    print('*', end='')
print()

# Print message
print('*', message, '*')

# Print bottom line of asterisks
for i in range(length + 4):
    print('*', end='')
print()