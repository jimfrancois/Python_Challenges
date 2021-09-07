import math

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