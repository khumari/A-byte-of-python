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

# from mymodule import say_hi, __version__

# say_hi()
# print('version ', __version__)

###################################################################################################
# import this
###################################################################################################
# The dir function, try it in interactive python interpreter
# import sys

# dir(sys)

# a = 5
# b = 8
# dir()

###################################################################################################
# Data structure: List

# shoplist = ['apple', 'pomegranate', 'banana', 'carrot', 'peach', 'grape']

# print('I have ', len(shoplist), ' items to purcahse')
# print('These items are ')
# for items in shoplist:
#     print(items)

# print('This is my list', shoplist)

# shoplist.sort()

# print('This is my list after sort', shoplist)

# shoplist.append('kiwi')

# print('This is my current list', shoplist)

# old_item = shoplist[0]

# del shoplist[0]

# print('I purchased ', old_item)

# print('These are items left now I need to purchase', shoplist)


###################################################################################################
# Data structure: Tuple

# zoo = ('python','elephant','pengquin')
# print('number animals in the zoo is ', len(zoo))

# new_zoo = 'monkey', 'camel', zoo
# print('number of cage in the new zoo is ', len(new_zoo))

# print('all animal in new zoo are', new_zoo)
# print('animala brought from old zoo are ', new_zoo[2])
# print('last animal brought from old zoo is ', new_zoo[2][2])
# print('number of animals in new zoo is', len(new_zoo)-1 + len(new_zoo[2]))


# #empty tuple
# emypty_tuple = ()
# #sinle item in tupe: have to put comma after
# single_item = ('2',)
# print(single_item[0])
###################################################################################################
# Data structure: Sequence

# shoplist = ['apple', 'mango', 'carrot', 'banana']
# name = 'swaroop'

# #indexing or 'subscript' operation
# print('Item 0 is ', shoplist[0])
# print('Item 1 is ', shoplist[1])
# print('Item 2 is ', shoplist[2])
# print('Item 3 is ', shoplist[3])
# print('Item -1 is ', shoplist[-1])
# print('Item -2 is ', shoplist[-2])
# print('Character 0 is ', name[0])

# #slicing on a list

# print('Item 1 to 3 is ', shoplist[1:3])
# print('Item 2 to end is ', shoplist[2:])
# print('Item 1 to -1 is ', shoplist[1:-1])
# print('Item start to end is ', shoplist[:])

# #slicing on a string
# print('character 1 to 3 is ', name[1:3])
# print('character 2 to end is ', name[2:])
# print('character 1 to -1 is ', name[1:-1])
# print('character start to end is ', name[:])

###################################################################################################
# Data structure: Set

# bri = set(['russia', 'pakistan', 'india'])
# if 'kabul' in bri:
#     print('true')
# else:
#     print('false')

# bric = bri.copy()
# bric.add('afghanistan')
# print(bric)
# bri.remove('india')
# print(bri)
# bric.remove('pakistan')
# print(bri & bric)


###################################################################################################
# Data structure: Refrences

# shoplist = ['apple','kiwi', 'melon', 'banana']
# mylist = shoplist

# print('shoplist ', shoplist)
# print('mylist ', mylist)

# mylist = shoplist[:]
# del mylist[1]
# print('mylist ', mylist)
# print('shoplist ', shoplist)

###################################################################################################
# #Data structure: More about String
# list = ['apple','banana','orange']
# name = 'swaroop'

# if name.startswith('swa'):
#     print('yes the string starts with swa')
# if 'a' in name:
#     print('yes the string contain a')
# if name.find('swaroop') != -1:
#     print('the string complete')

# delimter = '__*__'
# print(delimter.join(list))

###################################################################################################
