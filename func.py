# function is a block of code that only runs when it is been called upon

# basic
# def sayHello():
#     print(f'hello how are you')
# sayHello()

# def listOfPeople():
#     people= ['zainab','Charles','Daniel']
#     print(people)
# listOfPeople()

# # ::: function with argument
# def sayMyName(name,age):
#     print(f'hello my name is {name},and i am {age} years old')
# sayMyName('zainab',23)
# function with default argument

# def sayHello(name='Nathaniel'):
#     print(f'hello my name is {name}')
# sayHello('Nosa')

# :::Return value 
# def sayHello():
#     return f'Hello how are you'
# print(sayHello())

# def sayHello(name='Nathaniel'):
#     return(f'hello my name is {name}')
# print(sayHello('Nosa'))

# def getSum(num1,num2):
#     num1 = float(input('Enter num one: '))
#     num2 = float(input('Enter num two: '))
#     total = num1 + num2
#     return f'{total}'

# print(getSum('2','4'))

# def calculate(num1,num2,num3=4):
#     sumNum = num1+num2+num3
#     # return(sumNum)
#     return f' the sum of {num1} + {num2} + {num3} = {sumNum}'
# print(calculate(2,3))

# getSum = lambda num1, num2 : num1 + num2
# print(getSum(3, 5))

# CONDITION
# if & else statement
# x = 10
# y = 5
# if x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{x} is not equal to {y}')

# name = input('Enter your name: ').lower()
# if name == 'zainab':
#     print(f'allow her to take the exam')
# else:
#     print(f'you are not a registered user')

# # rain, sunny, harmattan 
# weather = input('Enter weather: ').lower()

# if weather == 'rainy':
#     print(f' Kindly take your umbrella.')
# elif weather == 'sunny':
#     print(f'Put on your sunshades.')
# elif weather == 'harmattan':
#     print(f'Use your cardigan.')
# else:
#     print(f'The weather is good ')

# # 5-30
# age = int(input('Enter age for immunization: '))
# if age >= 5 and age <=30:
#     print(f'Yes you are eligible for the immunization')
# elif age >30:
#     print('you are too old for this program')
# else:
#     print(f'eat well to grow fast')

# Nested if
# x = 6
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than 10')

# # logical operator
# # and
# if x > 2 and x > 10:
#     print(f'{x} is greater than 2 and less than 10')
# else:
#     print(f'{x} is greater than 2 and less than 10')

# # or
# if x > 2 or x > 10:
#     print(f'{x} is greater than 2 and less than 10')
# else:
#     print(f'{x} is greater than 2 and less than 10')

# # not
# if not(x > 2 and x < 10):
#     print(f'{x} is greater than 2 and less than 10')
# else:
#     print(f'false')

# number = [1,2,3,4,5,6]
# x= 6
# if x in number:
#     print(x in number)

# # # not in
# number = [1,2,3,4,5,6]
# x= 7

# if x not in number:
#     print(x in number)


# Identity Operators
# # is
# x = 10
# y = 10
# if x is y:
#     print(x is y)

# #is not
# x = 10
# y = 5
# if x is not y:
#     print(x is not y)