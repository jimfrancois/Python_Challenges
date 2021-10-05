import math
import random
from typing import Pattern
from array import *
import csv
from tkinter import *

#Challenge01
fname = input("What is your first name? ")
print('Hello', fname)

#Challenge02
fname = input('what is your firstname? ')
surname = input('what is your surname? ')
print('Hello', fname, surname)

#Challenge03
print('What do you call a bear with no teeth?\n A gummy bear!')

#Challenge04
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a second number: '))
print('The total is', num1 + num2)

#Challenge05
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a second number: '))
num3 = int(input('Please enter a third number: '))
sum = (num1 + num2) * num3
print('The answer is', sum)

#Challenge06
slices_of_pizza = int(input('Enter the number of slices of pizza you started with: '))
slice_eaten = int(input("How many slices have you eaten: "))
slicesLeft = slices_of_pizza - slice_eaten
print('You have', slicesLeft, "Slices remaining.")

#Challenge07
name = input('What is your name: ')
age = int(input('How old are you: '))
newAge = age + 1
print(name, 'next birthday you will be', newAge)

#Challenge08
bill = int(input('what is the total cost of the bill?: '))
people = int(input('How many people are there?: ' ))
each = bill / people
print("Each person should pay $", each)

#Challenge09
days = int(input('Enter the number of days: '))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("In", days, "days there are...")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")

#Challenge10
kilo = int(input("Enter the number of kilos: "))
pound = kilo * 2.204
print("That is", pound, "pounds")

#Challenge11
larger = int(input("Enter a number over 100: "))
smaller = int(input("Enter a number under 10: "))
answer = larger // smaller
print(smaller, "goes into", larger, answer, "times")

#Challenge12
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2) 

#Challenge13
number = int(input("Enter a value that is less than 20: "))
if number >= 20:
    print("Too high")
else:
    print("Thank you")     

#Challenge14
num = int(input("Enter a value between 10 and 20: "))
if num >= 10 and num <= 20:
    print("Thank you")
else:
    print("Incorrect answer")   

#Challenge15
colour = input("Type in your favourite colour: ")
if colour == "red" or colour == "RED" or colour == "Red":
    print("I like red too")
else:
    print("I don't like that colour, I prefer red")      


#Challenge16
raining = input("Is it raining? ")
raining = str.lower(raining)
if raining == "yes":

    windy = input("Is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")     


#Challenge17
age = int(input("What is your age? "))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket") 
else:
    print("You can gpo Trick-or-Treating")  

#Challenge18
num = int(input("Enter a number: "))
if num < 10:
    print("Too low")
elif num >= 10 and num <= 20:
    print("Correct")
else:
    print("Too high")        


#Challenge19
num = int(input("Enter 1, 2 or 3: "))
if num == "1":
    print("Thank you")
elif num == "2":
    print("Well done")
elif num == "3":
    print("Correct") 
else:
    print("Error message")   


#Challenge20
name = input("Enter your first name: ")
length = len(name)
print(length)      

#Challenge21
firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
name = firstname + " " + surname
length = len(name)
print(name)
print(length)

#Challenge22
firstname = input("Enter your first name in lowercase: ")
surname = input("Enter your surname in lowercase: ")
firstname = firstname.title()
surname = surname.title()
name = firstname + " " + surname
print(name)

#Challenge23
phrase = input("Enter the first line of a nursery rhyme: ")
length = len(phrase)
print("This has", length, "letters in it")
start = int(input("ERnter a starting number: "))
end = int(input("ERnter a end number: "))
part = (phrase[start:end])
print(part)

#Challenge24
word = input("Enter a word: ")
word = word.upper()
print(word)

#Challenge25
name = input("Enter your first name: ")
if len(name) < 5:
    surname = input("Enter your surname: ")
    name = name + surname
    print(name.upper())
else:
    print(name.lower())


#Challenge26
word = input("Please enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
    print(newword.lower()) 

#Challenge27
num = float(input("Enter a number with lots of decimal places: "))
print(num * 2)    

#Challenge28
num = float(input("Enter a number with lots of decimal places: "))
answer = num * 2
print(answer)
print(round(answer, 2))

#Challenge29
num = int(input("Enter a number over 500: "))
answer = math.sqrt(num)
print(round(answer, 2))

#Challenge30
print(round(math.pi, 5))


#Challenge31
radius = int(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print(area)

#Challenge32
radius = int(input("Enter the radius of the circle: "))
depth = int(input("Enter depth: "))
area = math.pi * (radius ** 2)
volume = area * depth
print(round(volume, 3))

#Challenge33
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

ans1 = num1 // num2
ans2 = num1 % num2
print(num1, "divided by", num2, "is", ans1, "with", ans2, "remainng.")


#Challenge34
print('1 Square')
print('2 Triangle')
print()
menuselection = int(input("Enter a number: "))
if menuselection == 1:
    side = int(input("Enter the length of one side: "))
    area = side * side
    print("The area of your chosen shape is", area)

elif menuselection == 2:
    base = int(input("Enter the length of the base: ")) 
    height = int(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print("The area of your chosen shape is", area)

else:
    print("Incorrect option selected")


#Challenge35
name = input("Type your name: ")
for x in range(0, 3):
    print(name) 


#Challenge36
name = input("Type your name: ")
number = int(input("Enter a number: "))
for i in range(0, number):
    print(name)              


#Challenge37
name = input("Enter your name: ")
for i in name:
    print(i)   
    

#Challenge38
num = int(input("Enter a number: "))
name = input("Enter your name: ")
for x in range(0, num):
    for i in name:
        print(i)     


#Challenge39
num = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
    answer = i * num
    print(i, "x", num, "=", answer)


#Challenge40
num = int(input("Enter a number below 50: "))
for i in range(50, num-1, -1):
    print(i)    

#Challenge41
name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0, 3):
        print("Too high")     

#Challenge42
total = 0
for i in range(0, 5):
    num = int(input("Enter a number: "))
    ans = input("Do you want this number included? (y/n")
    if ans == "y":
        total = total + num
print(total) 


#Challenge43

direction = input("Do you want to count up or down? (u/d) ")
if direction == "u":
    num = int(input("What is the top number? "))
    for i in range(1, num + 1):
        print(i)
elif direction == "d":
    num = int(input("Enter a number below 20: "))
    for i in range(20, num - 1, -1 ):
        print(i)
else:
    print("I don't understand") 


#Challenge44
num = int(input("How many friends do you want to invite to the party? "))
if num < 10:
    for i in range(0, num):
        name = input("Enter a name: ")
        print(name, "has been invited")
else:
    print("Too many people") 

#Challenge45
total = 0
while total <= 50:
    number = int(input("Enter a number: "))
    total = total + number
print("The total is", total) 

#Challenge46
number = 0
while number <= 5:
    number = int(input("Enter a number: "))
print("The last number you entered was a", number) 


#Challenge47
num1 = int(input("Enter a number: "))
total = num1
again = "y"
while again == "y":
    num2 = int(input("Enter another number: "))
    total = total + num2
    again = input("Do you want to add another number? (y/n) ")
print("The total is ", total)


#Challenge48
again = "y"
count = 0
while again == "y":
    name = input("Enter a name of somebody you want to invite to your party: ")
    print(name, "has now invited")
    count = count + 1
    again = input("Do you want to invite somebody else? (y/n) ")
print("You have", count, "people coming to your party")


#Challenge49
compnum = 50
usr = int(input("Can you guess the number I am thinking of? "))
count = 1
while usr != compnum:
    if usr < compnum:
        print("Too low")
    else:
        print("Too high")
    count = count + 1
    usr = int(input("Have another guess: "))
print("Well done, you took", count, "attempts")



#Challenge50
numbr = int(input("Enter a number between 10 and 20: "))
while numbr < 10 or numbr > 20:
    if numbr < 10:
        print("Too low")
    else:
        print("Too high")
    numbr = int(input("Try again: "))
print("Thank you") 


#Challenge51
num = 10
while num > 0:
    print("There are ", num, "green bottles hanging on the wall.")
    print(num, "green bottles hanging on the wall")
    print("And if 1 green bottle should accidentally fall,")

    num = num - 1
    answer = int(input("How many green bottles will be hanging on the wall?"))

    if answer == num:
        print("There will be", num, "green bottles hanging on the wall.")
        
    else:
        while answer != num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall.") 


#Challenge52
number = random.randint(1,100)
print(number)


#Challenge53
fruit = random.choice(["apple", "orange", "grape", "banana", "strawberry", ""])
print(fruit)


#Challenge54
coin = random.choice(['h', 't'])
usr = input("Enter (h)eads or (t)ails): ")

if usr == coin:
    print("You win")
else:
    print("Bad luck")

if coin == "h":
    print("It was heads")
else:
    print("It was tails")


#Challenge55
number = random.randint(1,5) 
guess = int(input("Enter a number: "))

if guess == number:
    print("well done")

elif guess > number:
    print("Too high")
    guess = int(input("Guess again: "))

    if guess == number:
        print("Incorrect")

    else: 
        print("Youl ose") 

elif guess < number:
    print("Too low")
    guess = int(input("Guess again: ")) 
    if guess == number:
        print("Incorrect")
else: 
    print("Youl ose") 



#Challenge56
num = random.randint(1, 10)
correct = False 

while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True


#Challenge57

num = random.randint(1, 10)
correct = False 

while correct == False:
    guess = int(input("Enter a number: "))

    if guess == num:
        correct = True

    elif guess > num:
        print("Too high")

    else:
        print("Too low")         


 #Challenge58
score = 0
for i in range(1, 6):
    numb1 = random.randint(1, 50) 
    numb2 = random.randint(1, 50) 
    correct = numb1 + numb2
    print(numb1, "+", numb2, "=")

    answr = int(input("Your answer: "))
    print() 
    if answer == correct:
        score = score + 1
print("You scored", score, "out of 5")  

#Challenge59
Colour = random.choice(["red", "blue", "green", "white", "pink"])
print("Select from red, blue, green, white or pink")
tryAgain = True

while tryAgain == True:
    theirchoice = input("Enter a colour: ")
    theirchoice = theirchoice.lower()

    if colour == theirchoice:
        print("Well done")
        tryAgain = False

    else:
        if colour == "red":
            print("I bet you are seeing RED right now!")

        elif colour == "blue":
            print("Don't feel BLUE.")

        elif colour == "green":
                print("I bet you are GREEN with envy right now.") 

        elif colour == "white": 
            print("Are you WHITE as a sheet, as you didn't guess correctly?") 

        elif colour == "pink": 
            print("Shame you arenot feeling in the PINK,as you got it wrong!") 


#Challenge60
import turtle

for x in range(0, 4):
    turtle.forward(100)
    turtle.right(90)

turtle.exitonclick()   

#Challenge61
import turtle

for i in range(0, 3):
    turtle.forward(100)
    turtle.left(120)

turtle.exitonclick() 


#Challenge62
import turtle

for x in range(0, 360):
    turtle.forward(1)
    turtle.right(1)

turtle.exitonclick() 


#Challenge63
import turtle

turtle.color("black", "red")
turtle.begin_fill()

for x in range(0, 4):
    turtle.forward(70)
    turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()

for x in range(0, 4):
    turtle.forward(70)
    turtle.right(90)

turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()

for x in range(0, 4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick() 

#Challenge64
import turtle

for i in range(0, 5):
    turtle.forward(100)
    turtle.right(144)

turtle.exitonclick() 

#Challenge65
import turtle

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(45)
turtle.left(180)
turtle.forward(45)
turtle.left(180)
turtle.forward(45)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

turtle.hideturtle()

turtle.exitonclick()


#Challenge66

import turtle
import random

turtle.pensize(3)

for i in range(0, 8):
    turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "orange"]))

    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()


#Challenge67
import turtle
import random

for x in range(0, 10):
    for i in range(0, 8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()

turtle.exitonclick()

#Challenge68
import turtle
import random

lines = random.randint(5, 20)

for x in range(0, lines):
    turtle.random.randint(25, 100)
    rotate = random.randint(1, 365)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()

#Challenge69

country_tuple = ("Haiti", "R. Dominicaine", "Porto-Rico", "USA")
print(country_tuple)

print()
country = input("Please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))

#Challenge70
country_tuple = ("Haiti", "R. Dominicaine", "Porto-Rico", "USA")
print(country_tuple)

print()
country = input("Please enter one of the countries from above: ")
print(country, "has index number", country_tuple.index(country))
print()
num = int(input("Enter a number between 0 and 4: "))

print(country_tuple[num])

#Challenge71
sports_list = ["tennis", "footbal"]

sports_list.append(input("What is your favourite sport? "))
sports_list.sort()
print(sports_list)

#Challenge72
subject_list = ["maths", "engelish", "computing", "history", "science", "spanish"]

print(subject_list)
dislike = input("Which of these subjects do you dislike? ")

getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)

#Challenge73
food_dictionary = {}
food1 = input("Enter a food you like: ")
food_dictionary[1] = food1

food2 = input("Enter another food you like: ")
food_dictionary[2] = food2

food3 = input("Enter a third food you like: ")
food_dictionary[3] = food3

food4 = input("Enter one last food you like: ")
food_dictionary[4] = food4

print(food_dictionary)
dislike = int(input("Which of these do you want to get rid of? "))

del food_dictionary[dislike]
print(sorted(food_dictionary.values()))

#Challenge74
colours = ["red", "blue", "yellow", "green", "pink", "orange"]
start = int(input("Enter a starting number (0-4): "))

end = int(input("Enter an end number (5-9): "))

print(colours[start:end])


#Challenge75

nums = [123, 345, 234, 765]

for i in nums:
    print(i)
selection = int(input("Enter a number from the list: ")) 

if selection in nums:
    print(selection, "is in position", nums.index(selection))

else:
    print("That is not in the list")


#Challenge76

name1 = input("Enter a name of somebody you want to invite to your party: ")

name2 = input("Enter another name: ")

name3 = input("Enter a third name: ")

party = [name1, name2, name3]
another = input("Do you want to invite another (y/n): ")

while another == "y":
    new_name = party.append(input("Enter another name: "))

    another = input("Do you want to invite another (y/n): ")

print("You have", len(party), "people coming to your party")  

#Challenge77
name1 = input("Enter a name of somebody you want to invite to your party: ")

name2 = input("Enter another name: ")

name3 = input("Enter a third name: ")

party = [name1, name2, name3]
another = input("Do you want to invite another (y/n): ")

while another == "y":
    new_name = party.append(input("Enter another name: "))

another = input("Do you want to invite another (y/n): ")

print("You have", len(party), "people coming to your party")

print(party)

selection = input("Enter one of the names: ")
print(selection, "is in position", party.index(selection), "on the list")
stillcome = input("Do you still want them to come (y/n): ")

if stillcome == "n":
    party.remove(selection)
print(party) 


#Challenge78
tv = ["Task Master", "Top Gear", "The Big Bang Theory", "How I Met Your Mother"]

for i in tv:
    print(i)

print()
newtv = input("Enter another TV show: ") 

position = int(input("Enter a number between 0 and 3: "))
tv.insert(position, newtv)

for i in tv:
    print (i)


#Challenge79
num = []
count = 0
while count < 3 :
    nums = int(input("Enter a number: "))
    num.append(nums)
    print(num)
    count = count + 1

lastnum = input("Do you want the last number saved (y/n): ") 

if lastnum == "n":
    num.remove(nums)
print(num) 


#Challenge80

fname = input("Enter your first name: ")
print("That has", len(fname), "characters in it")

sname = input("Enter your surname: ")
print("That has", len(sname), "characters in it")

name = fname + " " + sname
print("Your full name is", name)
print("That has", len(name), "characters in it")

#Challenge81

subject = input("Enter your favourite school subject: ")
for letter in subject:
    print(letter, end="-")


#Challenge82

poem = "Oh, I wish I'd looked after me theeth,"
print(poem)

start = int(input("Enter a starting number: "))
end = int(input("Enter a end number: "))
print(poem[start:end])   


#Challenge83

msg = input("Enter a message in uppercase: ")
tryagain = False

while tryagain == False:
    if msg.isupper():
        print("Thank you")
    tryagain = True

else:
    print("Try again")
    msg = input("Enter a message in uppercase: ") 


#Challenge84
postcode = input("Enter your postcode: ")
start = postcode[0:2]
print(start.upper())   


#Challenge85

name = input("Enter your name: ")
count = 0
name = name.lower()

for y in name: 
    if y == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        count = count + 1
print("Vowels =", count)    

#Challenge86
new_password = input("Enter a new password: ")
confirm_password = input("re-enter the password again: ")

if new_password == confirm_password:
    print("Thank you")

elif new_password.lower() == confirm_password.lower():
    print("They must be in the same case")

else:
    print("Incorrect")


#Challenge87

user_word = input("Please enter a word: ")
length = len(user_word)
number = 1
for x in user_word:
    position = length - number
    letter = user_word[position]
    print(letter)
    number = number + 1


#Challenge88
numbers = array('i', [])

for i in range(0, 5):
    number = int(input("Enter a number: "))
    numbers.append(number)

numbers = sorted(numbers)
numbers.reverse()
print(numbers) 


#Challenge89

numbers = array('i', [])

for i in range(0, 5):
    number = random.randint(1, 100)
    numbers.append(number)

for i in numbers:
    print(i)


#Challenge90

numbers = array('i', [])
while len(numbers) < 5:
    number = int(input("Enter a number between 10 and 20: "))
    if number >= 10 and number <= 20:
        numbers.append(number)
    else:
        print("Outside the range")
for i in numbers:
    print(i) 


#Challenge91
       
numbers = array('i', [6,8,3,7,8])

for i in numbers:
    print(i)

    number = int(input("Enter a number: "))
    if numbers.count(number) == 1:
        print(number, "is in the list once")
    else:
        print(number, "is in the list", numbers.count(number),"times")


#Challenge92

num1 = array('i', [])
num2 = array('i', [])

for i in range(0, 3):
    num = random.randint(1, 100)
    num2.append(num)

num1.extend(num2)

num1 = sorted(num1)

for i in num1:
    print(i)



#Challenge93

nums = array("i", [])

for i in range(0, 5):
    num = int(input("Enter a number: "))
    nums.append(num)

nums =sorted(nums)

for i in nums:
    print(i)

num = int(input("Select a number from the array: "))
if num in nums:
    nums.remove(num)
    num2 = array('i', [])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That is not a value in the array")   


#Challenge94

nums = array('i', [4, 6, 8, 2, 5])

for i in nums:
    print(i)

num = int(input("Select one of the numbers: "))

tryagain = True
while tryagain == True:
        if num in nums:
            print("This is in position",nums.index(num))
            tryagain = False
        else:
            print("Not in array")
            num = int(input("Select one of the numbers: "))     


#Challenge95

nums = array('f', [34, 27, 99.58, 45, 28.65])
tryagain = True

while tryagain == True:
    num = int(input("Enter a number between 2 and 5: "))
    if num < 2 or num > 5:
        print("Incorrect value, try again.")
    else:
        tryagain = False

for i in range(0, 5):
    ans = nums[i] / num
    print(round(ans, 2))


#Challenge96
my_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]] 

#Challenge97
my_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Select a row: "))
col = int(input("Selcet a column: "))
print(my_list[row][col])

#Challenge98
my_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Which row would you like to display? "))
print(my_list[row])

newvalue = int(input("Enter a new value: "))
my_list[row].append(newvalue)
print(my_list[row])


#Challenge99

my_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

row = int(input("Which row would you like to display? "))
print(my_list[row])

col = int(input("Which column would you like to display in that row? "))
print(my_list[row][col])

change_value = input("Do you want to change the value (y/n): ")
if change_value == 'y':
    new_value = int(input("Enter a new value: "))
    my_list[row][col] = new_value
print(list[row])


#Challenge100
sales = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
}


#Challenge101


sales = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
}

person_name = input("Enter a sales person's name: ")
region = input("Enter a sales person's region: ")
print(sales[person_name][region])

new_data = int(input("Enter new data: "))
sales[person_name][region] = new_data
print(sales[person_name])


#Challenge102

list = {}
for i in range(0, 4):
    name = input("Please feel free to enter a name: ")
    age = int(input("What is your age? "))
    shoe_size = int(input("Enter a size: "))
    list[name] = {"Age": age, "Shoe_size": shoe_size}

user = input("Enter the name of one of the people: ")
print(list[user])


#Challenge103

list = {}
for i in range(0, 4):
    name = input("Please feel free to enter a name: ")
    age = int(input("What is your age? "))
    shoe_size = int(input("Enter a size: "))
    list[name] = {"Age": age, "Shoe_Size": shoe_size}

for name in list:
    print((name), list[name]["Age"])


#Challenge104

list = {}
for i in range(0, 4):
    name = input("Enter a name: ")
    age = int(input("What is your age? "))
    shoe_size = int(input("Enter a size: "))
    list[name] = {"Age": age, "Shoe_Size": shoe_size}

getrid = input("Enter the name of the person you want to remove: ")
del list[getrid]

for name in list:
    print((name), list[name]["Age"], list[name]["Shoe_Size"])


#Challenge105

file = open("Numbers.txt", 'w')
file.write("5, ")
file.write("7, ")
file.write("12, ")
file.write("20, ")
file.write("87")
file.close()   

#Challenge106
file = open("Names.txt", 'w')
file.write("Jim, ")
file.write("Kendy, ")
file.write("Sam, ")
file.write("Valery, ")
file.write("Noah")
file.close()

#Challenge107
file = open("Names.txt", "r")
print(file.read())
file.close()

#Challenge108
file = open("Names.txt", "a")
file.write(input("Enter another name: " + "\n"))
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()

#Challenge109
print("1) Create a new file")
print("2) Display the file")
print("3)Add a new item to the file")

choose = int(input("Make a selection 1, 2 or 3: "))
if choose == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(subject + "\n")
    file.close()

elif choose == 2:
    file = open("Subject.txt", "r")
    print(file.read())

elif choose == 3:
    file = open("Subject.txt", "a")
    subject = input("Enter a school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())

else:
    print("Invalid option")


#Challenge110
file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
selectedname = input("Enter  name from the list: ")
selectedname = selectedname + "\n"

for row in file:
    if row != selectedname:
        file = open("Names2.txt", "a")
        newrecord = row
        file.write(newrecord)
        file.close()
file.close()

#Challenge111

file = open("Books.csv", "w")
newrecord = "To kill A Mockingbird, Harper lee, 1960\n"
file.write(str(newrecord))

newrecord = "A Bried History of time, Stephen HHawking, 1988\n"
file.write(str(newrecord))

newrecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newrecord))

newrecord = "The Man who Mistook His wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newrecord))

newrecord = "Pride and prejudice, Jane Austen, 1813\n"
file.write(str(newrecord))
file.close()

#Challenge112

file = open("books.csv", "a")
title = input("Enter a title: ")
author = input("Enter an author: ")
year = input("Enter the year it was released: ")

newrecord = title + "," + author + "," + year + "\n"
file.write(str(newrecord))
file.close()

file = open("Books.csv", "r")
for row in file:
    print(row)
file.close()


#Challenge113
num = int(input("How many books do you want to add to the list? "))
file = open("Books.csv", "a")

for x in range(0, num):
    title = input("Entyer a title: ")
    author = input("Enter an author: ")
    year = input("Enter the year it was released: ")

    newrecord = title + "," + author + "," + year + "\n"
    file.write(str(newrecord))
file.close()

searchauthor = input("Enter an authors name to search for: ")

file = open("Books.csv", "r")
count = 0

for row in file:
    if searchauthor in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("There are no books by that author in this list.")
file.close()   


#Challenge114
start =int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)
    
x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
    x = x + 1   


 #Challenge115
file = open("Books.csv", "r")
x = 0

for row in file:
    display = "Row: " + str(x) + " - " + row
    print(display)
    x = x + 1   

#Challenge116
file = list(csv.reader(open("Books.csv")))
Booklist = []

for row in file:
    Booklist.append(row)
    
x = 0
for row in Booklist:
    display = x, Booklist[x]
    print(display)
    x = x + 1
getrid = int(input("Enter a row number to delete: "))
del Booklist[getrid]


x = 0
for row in Booklist:
    display = x, Booklist[x]
    print(display)
    x = x + 1
alter = int(input("Enter a row number to alter: "))


x = 0
for row in Booklist[alter]:
    display = x, Booklist[alter][x]
    print(display)
    x = x + 1
part = int(input("Which part do you want to change? "))
newdata = input("Enter new data: ")
Booklist[alter][part] = newdata
print(Booklist[alter])

file = open("Books.csv", "w")
x = 0
for row in Booklist:
    newrecord = Booklist[x][0] + ", " + Booklist[1] + ", " + Booklist[x][2] + "\n"
    file.write(newrecord)
    x = x + 1
file.close()  


#Challenge117

score = 0
name = input("What is your name: ")
q1_num1 = random.randint(10, 50)
q1_num2 = random.randint(10, 50)
question1 = str(q1_num1) + " + " + str(q1_num2) + " = "
ans1 = int(input(question1))
realans1 = q1_num1 + q1_num2

if ans1 == realans1:
    score = score + 1
    
q2_num1 = random.randint(10, 50)    
q2_num2 = random.randint(10, 50) 
question2 = str(q2_num1) + " + " + str(q2_num2) + " = "
ans2 = int(input(question2))
realans2 = q2_num1 + q2_num2

if ans2 == realans2:
    score = score + 1
    
file = open("QuizScore.csv", "a") 
newrecord = name + "," + question1 + "," + str(ans1) + "," + question2 + "," + str(ans2) + "," + str(score) + "\n"
file.write(str(newrecord))
file.close()

#Challenge118
def ask_value():
    num = int(input("Enter a number: "))
    return num

def count(num):
    n = 1
    while n <= num:
        print(n)
        n = n + 1
        
def main():
    num = ask_value()
    count(num)
    
main() 

#Challenge119
def pick_num():
    low = int(input("Enter the bottom of the range: "))
    high = int(input("Enter the top of the range: "))
    comp_num = random.randint(low, high)
    return comp_num

def first_guess():
    print("I am thinking of a number...")
    guess = int(input("What am i thonking of:"))
    return guess

def check_answer(comp_num, guess):
    try_again = True
    while try_again == True:
        if comp_num == guess:
            print("Correct, you win.")
            try_again = False
        
        elif comp_num > guess:
            guess = int(input("Too low, try again: "))
            
        else:
            guess =int(input("Too high, try again: "))
    
def main():
    comp_num = pick_num()
    guess = first_guess()
    check_answer(comp_num, guess)
    
main() 


#Challenge120
def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print(num1, "+", num2, "= ")
    user_answer = int(input("Your answer: "))
    actual_answer = num1 + num2
    answers = (user_answer, actual_answer)
    return answers

def substraction():
    num3 = random.randint(5, 20)
    num4 = random.randint(5, 20)
    print(num3, "-", num4, "= ")
    user_answer = int(input("Your answer: "))
    actual_answer = num3 - num4
    answers = (user_answer, actual_answer)
    return answers

def check_answer(user_answer, actual_answer):
    if user_answer == actual_answer:
        print("Correct")
        
    else:
        print("Incorrect, the answer is", actual_answer)
        
def main():
    print("1) Addition")
    print("2) Substraction")
    selection = int(input("Enter 1 or 2: "))
    
    if selection == 1:
        user_answer, actual_answer = addition()
        check_answer(user_answer, actual_answer)

    elif selection == 2:
        user_answer, actual_answer = addition()
        check_answer(user_answer, actual_answer)
        
    else:
        print("Incorrect seelection")
    
main()     

#Challenge121

def add_name():
    name = input("Enter a new name: ")
    names.append(name)
    return names

def change_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to change: "))
    name = input("Enter new name: ")
    names[select_num] = name
    return names

def delete_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to delete: "))
    del names[select_num]
    return names

def view_names():
    for x in names:
        print(x)
    print()
    
def main():
    again = "y"
    while again == "y":
        print("1) Add a name")
        print("2) Change a name")
        print("3) Delete a name")
        print("4) View names")
        print("5) Quit")
        selection = int(input("What do you want to do? "))
        
        if selection == 1:
            names = add_name()
            
        elif selection == 2:
            names = change_name()
            
        elif selection == 3:
            names = delete_name()
            
        elif selection == 4:
            names = view_names()
            
        elif selection == 5:
            again = "n"
        
        else:
            print("Incorrect option: ")
            data = (names, again)
            
            
names = []
main()


#Challenge122

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter a name: ")
    salary = int(input("Enter Salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()
    
def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close() 
    
    
tryagain =  True
while tryagain == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print()
    
    selection = input("Enter the number of your selection: ")
    if selection == 1:
        addtofile()
    
    elif selection == 2:
        viewrecords()
        
    elif selection == 3:
        tryagain = False
        
    else:
        print("Incorrect option")


#Challenge123

def addtofile():
    file = open("Salaries.csv", "a")
    name = input("Enter a name: ")
    salary = int(input("Enter Salary: "))
    newrecord = name + ", " + str(salary) + "\n"
    file.write(str(newrecord))
    file.close()


def viewrecords():
    file = open("Salaries.csv", "r")
    for row in file:
        print(row)
    file.close()

def  deleterecord():
    file = open("Salaries.csv", "r")
    x = 0
    tmplist = []
    for row in file:
        tmplist.append(row)
    file.close()
    
    for row in tmplist:
        print(x, row)
        x = x + 1
    rowtodelete = int(input("Enter the row number to delete: "))
    del tmplist[rowtodelete]
    file = open("Salaries.csv", "w")
    for row in tmplist:
        file.write(row)
    file.close()    
        
tryagain = True
while tryagain == True:
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print()

    selection = input("Enter the number of your selection: ")
    if selection == 1:
        addtofile()

    elif selection == 2:
        viewrecords()

    elif selection == 3:
        tryagain = False

    else:
        print("Incorrect option")


#Challenge124

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2["text"] = message
    
window = Tk()
window.geometry("500x200")

label1 = Label(text = "Enter your name:")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 20, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text = "Press me", command = click)
button1.place(x = 30, y = 50, width = 120, height = 25)
    
textbox2 = Message(text = "")
textbox2.place(x = 150, y = 50, width = 200, height = 25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()        


# 125

def click():
    num = random.randint(1, 6)
    answer["text"] = num
    
window = Tk()
window.title("Roll a dice")
window.geometry("100x120")

button1 = Button(text="Roll", command=click)
button1.place(x=30, y=30, width=50, height=25)

answer = Message(text="")
answer.place(x=40, y=70, width=30, height=25)

window.mainloop()

# 126

def add_on():
    num = enter_txt.get()
    num = int(num)
    answer = output_txt["text"]
    answer = int(answer)
    total = num + answer
    output_txt ["text"] = total


def reset():
    total = 0
    output_txt["text"] = 0
    enter_txt.delete(0, END)
    enter_txt.focus()

total = 0
num = 0

window = Tk()
window.title("Adding Together")
window.geometry("450x100")

enter_lbl = Label(text="Enter a number: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_txt = Entry(text=0)
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt["justify"] = "center"
enter_txt.focus()

add_btn = Button(text="Add", command= add_on)
add_btn.place(x=300, y=20, width=50, height=25)

output_lbl = Label(text="Answer = ")
output_lbl.place(x=50, y=50, width=100, height=25)

output_txt = Message(text=0)
output_txt.place(x=150, y=50, width=100, height=25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

clear_btn = Button(text="Clear", command = reset)
clear_btn.place(x=300, y=50, width=50, height=25)

window.mainloop()


# 127

def add_name():
    name = name_box.get()
    name_list.insert(END, name)
    name_box.delete(0, END)
    name_box.focus()

def clear_list():
    name_list.delete(0, END)
    name_box.focus()


window = Tk()
window.title("Name list")
window.geometry("400x200")

label1 = Label(text="Enter a name:")
label1.place(x=20, y=20, width=100, height=25)

name_box = Entry(text=0)
name_box.place(x=120, y=20, width=100, height=25)
name_box.focus()

button1 = Button(text="Add to list", command=add_name)
button1.place(x=250, y=20, width=100, height=25)

name_list = Listbox()
name_list.place(x=120, y=20, width=100, height=25)

button2 = Button(text="Clear List", command=clear_list)
button2.place(x=250, y=50, width=100, height=25)

window.mainloop()


# 128

def convert2():
    km = textbox1.get()
    km = int(km)
    mesage = km * 0.6214
    textbox2.delete(0, END)
    textbox2.insert(END, message)
    textbox2.insert(END, " miles")
    
window = Tk()
window.title("Distance")
window.geometry("260x200")

label1 = Label(text="Enter the value you want to convert:")
label1.place(x=30, y=20)

textbox1 = Entry(text="")
textbox1.place(x=30, y=50, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

convert1 = Button(text="Convert miles to km", command=convert1)
convert1.place(x=30, y=80, width=200, height=25)

convert2 = Button(text="Convert km to mile", command=convert2)
convert2.place(x=30, y=110, width=200, height=25)

textbox2 = Entry(text="")
textbox2.place(x=30, y=140, width=200, height=25)
textbox2["justify"] = "center"

window.mainloop()

# 129

def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END, num)
        num_box.delete(0, END)
        num_box.focus()

    else:
        num_box.delete(0, END)
        num_box.focus()

def clearList():
    num_list.delete(0, END)
    num_box.focus()

window = Tk()
window.title("Number list")
window.geometry("400x200")

label1 = Label(text="Enter a number:")
label1.place(x=20, y=20, width=100, height=25)

num_box = Entry(text=0)
num_box.place(x=120, y=20, width=100, height=25)
num_box.focus()

button1 = Button(text="Add to list", command=add_number)
button1.place(x=250, y=20, width=100, height=25)

num_list = Listbox()
num_list.place(x=120, y=20, width=100, height=25)

button2 = Button(text="Clear list", command=clearList)
button2.place(x=250, y=50, width=100, height=25)

window.mainloop()

# 130

def add_number():
    num = num_box.get()

    if num.isdigit():
        num_list.insert(END, num)
        num_box.delete(0, END)
        num_box.focus()

    else:
        num_box.delete(0, END)
        num_box.focus()

def clearList():
    num_list.delete(0, END)
    num_box.focus()

def save_list():
    file = open("numbers.csv", "w")
    tmplist = num_list.get(0, END)
    item = 0

    for x in tmplist:
        newrecord = tmplist[item] + "\n"
        file.write(str(newrecord))
        item = item + 1
    file.close()

window = Tk()
window.title("Number list")
window.geometry("400x200")

label1 = Label(text="Enter a number:")
label1.place(x=20, y=20, width=100, height=25)

num_box = Entry(text=0)
num_box.place(x=120, y=20, width=100, height=25)
num_box.focus()

button1 = Button(text="Add to list", command=add_number)
button1.place(x=250, y=20, width=100, height=25)

num_list = Listbox()
num_list.place(x=120, y=20, width=100, height=25)

button2 = Button(text="Clear list", command=clearList)
button2.place(x=250, y=50, width=100, height=25)

button3 = Button(text="Save list", command=save_list)
button3.place(x=250, y=80, width=100, height=25)

window.mainloop()


# 131

def create_new():
    file = open("ages.csv", "w")
    file.close()

def save_list():
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newrecord = name + ", " + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()

window = Tk()
window.title("People List")
window.geometry("400x100")

label1 = Label(text="Enter a name:")
label1.place(x=20, y=20, width=100, height=25)

name_box = Entry(text="")
name_box.place(x=120, y=20, width=100, height=25)
name_box["justify"] = "left"
name_box.focus()

label2 = Label(text="Enter their age:")
label2.place(x=20, y=50, width=100, height=25)

age_box = Entry(text="")
age_box.place(x=120, y=50, width=100, height=25)
age_box["justify"] = "left"

button1 = Button(text="Create new file", command=create_new)
button1.place(x=250, y=20, width=100, height=25)

button2 = Button(text="Add to file", command=save_list)
button2.place(x=250, y=50, width=100, height=25)

window.mainloop()


# 132

def save_list():
    file = open("ages.csv", "a")
    name = name_box.get()
    age = age_box.get()
    newrecord = name + ", " + age + "\n"
    file.write(str(newrecord))
    file.close()
    name_box.delete(0, END)
    age_box.delete(0, END)
    name_box.focus()

def read_list():
    name_list.delete(0, END)
    file = list(csv.reader(open("ages.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        name_list.insert(END, data)
        x = x + 1


window = Tk()
window.title("People List")
window.geometry("400x200")

label1 = Label(text="Enter a name:")
label1.place(x=20, y=20, width=100, height=25)

name_box = Entry(text="")
name_box.place(x=120, y=20, width=100, height=25)
name_box["justify"] = "left"
name_box.focus()

label2 = Label(text="Enter their age:")
label2.place(x=20, y=50, width=100, height=25)

age_box = Entry(text="")
age_box.place(x=120, y=50, width=100, height=25)
age_box["justify"] = "left"

button1 = Button(text="Add to file", command=save_list)
button1.place(x=250, y=20, width=100, height=25)

button2 = Button(text="Read list", command=read_list)
button2.place(x=250, y=50, width=100, height=25)

label3 = Label(text="Saved Names:")
label3.place(x=20, y=80, width=100, height=25)

name_list = Listbox()
name_list.place(x=120, y=80, width=230, height=100)

window.mainloop()


# 133

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["text"] = message

window = Tk()
window.title("Names")
window.geometry("450x350")
window.wm_iconbitmap("strips.ico")
window.configure(background="black")

logo = PhotoImage(file="")
logoimage = Label(image=logo)
logoimage.place(x=100, y=20, width=200, height=150)

label1 = Label(text="Enter your name:")
label1.place(x=30, y=200)
label1["bg"] = "black"
label1["fg"] = "white"

textbox1 = Entry(text="")
textbox1.place(x=150, y=200, width=200, height=25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text = "Press me", command= click)
button1.place(x=30, y=250, width=120, height=25)
button1["bg"] = "yellow"

textbox2 = Message(text="")
textbox2.place(x=150, y=250, width=200, height=25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()

# 134

def checkans():
    theirans = ansbox.get()
    theirans = int(theirans)
    
    num1 = num1box["text"]
    num1 = int(num1)
    
    num2 = num2box["text"]
    num2 = int(num2)
    
    ans = num1 + num2
    if theirans == ans:
        img = PhotoImage(file="correct.gif")
        imgbx.image = img
    else:
        img = PhotoImage(file="wrong.gif")
        img.image = img
        
    imgbx["image"] = img
    imgbx.update()
    
    
def nextquestion():
    ansbox.delete(0, END)
    num1 = random.randint(10, 50)
    num1box["text"] = num1

    num2 = random.randint(10, 50)
    num2box["text"] = num2
    
    img = PhotoImage(file="")
    imgbx.image = img
    imgbx["image"] = img
    imgbx.update()
    
window = Tk()
window.title("Addition")
window.geometry("250x300")

num1box = Label(text="0")
num1box.place(x=50, y=30, width=25, height=25)

addsymbl = Message(text="+")
addsymbl.place(x=75, y=30, width=25, height=25)

num2box = Label(text="0")
num2box.place(x=100, y=30, width=25, height=25)

eqlsymbl = Message(text="=")
addsymbl.place(x=125, y=30, width=25, height=25)

ansbox = Entry(text="")
ansbox.place(x=150, y=30, width=25, height=25)
ansbox["justify"] = "center"
ansbox.focus()

checkbtn = Button(text="Check", command=checkans)
checkbtn.place(x=50, y=60, width=75, height=25)

nextbtn = Button(text="Next", command=nextquestion)
nextbtn.place(x=130, y=60, width=75, height=25)

img = PhotoImage(file="")
imgbx = Label(image=img)
imgbx.image = img
imgbx.place(x=25, y=100, width=200, height=150)

nextquestion()

window.mainloop()
