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