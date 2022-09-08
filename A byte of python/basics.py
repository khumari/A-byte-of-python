###################################################################################################
# The if statement
# number = 20
# guess = int(input('guess an integer number'))

# if guess == number:
#     print('congratulation you guessed it right')

# elif guess < number:
#     print('the number is higher than this')

# else:
#     print('the number is smaller than this')

# print('done')
###################################################################################################
# Dictionary
# ab = {'khumari': 'kbarakzai@gmail.com', 'muska':'mbarak@gmail.com', 'muzamil':'muz@uyahoo.com' }

# # print('printing {} the items insidie the dictionary:' .format(len(ab)))
# # ab = {'amina': 'amina@yahoo.com'}
# ab['amina'] = 'amena@yahoo.com'
# print('printing {} the items insidie the dictionary:' .format(len(ab)))

# for name, address in ab.items():
#     print('contact of {} is {}' .format(name, address))

# if 'khumari' in ab:
#     print("\n khumari is working hard and her address is", ab['khumari'])
# del ab['khumari']

# for name, address in ab.items():
#     print('contacts {}' .format(address))


###################################################################################################
# The while statement

# number = 23
# running = True

# while running:
#     guess = int(input('Guess a number'))

#     if guess == number:
#         print('you guessed it right!!! wohoo')
#         running = False
#     elif guess < number:
#         print('you guessed a smaller number try again')
#     else:
#         print('you guessed a larger number try again')

# else:
#     print('Good job you are done')

# print('byeeee')

###################################################################################################
# The for loop

# for i in range(1,5):
#     i = 2 * i
#     print(i)
# else:
#     print('The for loop is over')

###################################################################################################
# The break statement

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Done')

###################################################################################################
# The continue statement

# while True:
#     s = input('Enter something : ')
#     if s == 'quit':
#         break
#     if len(s) < 3:
#         print('Too small')
#         continue
#     print('Input is of sufficient length')

###################################################################################################
#Functions

# def sayhello():
#     print('Hello world')


# sayhello()
# sayhello()
# sayhello()
# sayhello()
# sayhello()

###################################################################################################
#function paratmeters

# def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to ', b)
        
#     else :
#         print(b, 'is maximum')
        
# print_max(12, 14)

# x = 5
# y = 7

# # pass variables as arguments
# print_max(x, y)
###################################################################################################
#Deafult Argument Values

# def say(message, times =1):
#     print(message * times)

# say('hello')
# say('hello', 5)

###################################################################################################
# Keywords Arguments

# def func(a , b = 1 , c = 3):
#     print('a is ', a , 'b is ', b , 'c is ', c)

# func(10)

###################################################################################################
# VarArgs parameters

# def total(a = 5, *numbers, **phonebook):
#     print('a ', a)

#     #iterate through all items in tuple
#     for single_item in numbers:
#         print('Single_item ', single_item)

#     #iterate through all items in dictionary
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)

# total(10,1,2,3,4, jack = 1234, bob = 2341, john = 8769)

###################################################################################################
# The return statement

# def maximum(x, y):
#     if x>y:
#         return x
#     elif x == y:
#         return 'x is equal to y'

#     else:
#         return y

# print(maximum(3,3))

###################################################################################################
#DocStrings

# def print_max(x, y):
#     '''Prints the maximum of two numbers.

#     The two values must be integers.'''
#     #convert to integers if possible
#     x = int(x)
#     y = int(y)

#     if x > y:
#         print(x, 'is maximum')
#     else:
#         print(y, 'is maximum')

# print_max(9,5)
# print(print_max.__doc__)


###################################################################################################
#Modules

# import sys
# import os

# print('command line arguments are ')
# for i in sys.argv:
#     print(i)

# # print('\n\n\n The Pythonpath is ', sys.path)
# print(os.getcwd())

#copy this in terminal bellow:python basics.py we are are arguments
###################################################################################################
# Byte-Compiled .pyc files

 ###################################################################################################
# The from import statement

# from math import sqrt

# print('sqare root of 16 is ', sqrt(16))

###################################################################################################
#A module's __name__
# import math

# if __name__ == '__main__':
#     print('This program is run by itself')
# else:
#     print('I am being imported from another module')

###################################################################################################
# Making your own modules

# import mymodule

# mymodule.say_hi()
# print('version ', mymodule.__version__)

#Here is the version utilizing from.. import syntax

from mymodule import say_hi, __version__

say_hi()
print('version ', __version__)