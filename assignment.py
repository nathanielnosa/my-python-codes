# # ass1 
person = {
    'first_name': 'daniel',
    'last_name': 'alugo',
    'age':24
}
# person['hobbies'] = ['singing','chatting','reading','dancing']
# '''
# print(person['age'])
# print(person['hobbies'])
# print(person['hobbies'][2])

# '''
# person2 = person.copy()
# person2['height'] = 5.8
# print(person2)

# # ass2
# person = [
#     {
#     'first_name': 'daniel',
#     'last_name': 'alugo',
#     'age':24
#     },
#     {
#     'first_name': 'charles',
#     'last_name': 'akate',
#     'age':24
#     },
#     {
#     'first_name': 'zinab',
#     'last_name': 'alugo',
#     'age':24
#     },
#     {
#     'first_name': 'john',
#     'last_name': 'doe',
#     'age':24
#     },
# ]
# print(person[2])

# def calculator(num1, num2):
#     add = num1 + num2
#     print(add)
#     sub = num1 - num2
#     print(sub)
#     mul = num1 * num2
#     print(mul)
#     div = num1 / num2
#     print(div)
# calculator(10,5)

# ass 4
# num1 = float(input('Enter num one: '))
# num2 = float(input('Enter num two: '))
# addNum = num1 + num2

# print(addNum)

# # add 5
# def addNum(num1, num2=7):
#     num1 = float(input('Enter num one: '))
#     total = num1 + num2
#     return f'{total}'
# print(addNum(''))

# # add n minus 
# num1 = float(input('Enter num one: '))
# num2 = float(input('Enter num two: '))
# num3 = float(input('Enter num three: '))

# add3 = num1 + num2 + num3
# addSub = (num1 + num2) - num3 
# print(add3)
# print(addSub)

# ass 6
# num = int(input('Enter number: '))
# if num % 2 == 0:
#     print(f'{num} is an even number')
# else:
#     print(f'{num} is an odd number')

# ass 7
# value = input('Enter alphabet: ').lower()
# alphabet = ['a','e','i','o','u']

# if value in alphabet:
#     print(f'{value} is a vowel')
# elif value.isdigit():
#     print(f'{value} can not be a alphabet')
# else:
#     print(f'{value} is a consonant')

# ass 7
# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))
# num3 = int(input('Enter num3: '))

# if (num1> num2) and (num1 > num3):
#     print(f'{num1} is the greatest')
# elif (num2> num1) and (num2 > num3):
#     print(f'{num2} is the greatest')
# elif (num3> num1) and (num3 > num2):
#     print(f'{num3} is the greatest')
# else:
#     print('All numbers are equal')

# # ass 8 t
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
# print('''
#     Please select a number to continue
#       1. Addition           2. Subtraction
#       3. Multiplication     4. Division
# ''')
# select_num = int(input('Select a number: '))

# if(select_num == 1):
#     print('You select addition Enter two numbers')
#     num1 = int(input('Enter num one: '))
#     num2 = int(input('Enter num two: '))
#     print(add(num1,num2))
# elif(select_num == 2):
#     print('You select subtraction Enter two numbers')
#     num1 = int(input('Enter num one: '))
#     num2 = int(input('Enter num two: '))
#     print(sub(num1,num2))
# elif(select_num == 3):
#     print('You select multiplication Enter two numbers')
#     num1 = int(input('Enter num one: '))
#     num2 = int(input('Enter num two: '))
#     print(mul(num1,num2))
# elif(select_num == 4):
#     print('You select division Enter two numbers')
#     num1 = int(input('Enter num one: '))
#     num2 = int(input('Enter num two: '))
#     print(div(num1,num2))
# else:
#     print('Invalid selection')

# add 9
# score = int(input('Enter student score: '))
# if 80 <= score <= 100:
#     print('Excellent')
# elif 60 <= score <= 79:
#     print('v. good')
# elif 40 <= score <= 59:
#     print('good')
# elif 20 <= score <= 39:
#     print('fair')
# elif 0 <= score <= 19:
#     print('fail')
# else:
#     print('Invalid selection')
# if (score >= 80) and (score <= 100):
#     print('Excellent')
# elif (score >= 60) and (score <= 79):
#     print('v. good')
# elif (score >= 40) and (score <= 59):
#     print('good')
# elif (score >= 20) and (score <= 39):
#     print('fair')
# elif (score >= 0) and (score <= 19):
#     print('fail')
# else:
#     print('Invalid score')