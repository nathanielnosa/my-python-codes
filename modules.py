# # core modules

# import datetime
# today =datetime.date.today()
# print(today)

# # ex 2
# from datetime import date
# today = date.today()
# print(today)

# # ex 3
# from uuid import uuid4
# id = uuid4()
# print(id)

# # ex 4
# import uuid
# id = uuid.uuid4()
# print(id)

# # Installed module
# # import camelcase
# from camelcase import CamelCase

# # c = camelcase.CamelCase()
# c = CamelCase()
# text = 'hello, welcome to torilo'
# print(c.hump(text))


# custom
from assignment import person
from assignment import person as py
from assignment import *

print(py)

print('''
    Please select a number to continue
      1. Addition           2. Subtraction
      3. Multiplication     4. Division
''')
select_num = int(input('Select a number: '))

if(select_num == 1):
    print('You select addition Enter two numbers')
    num1 = int(input('Enter num one: '))
    num2 = int(input('Enter num two: '))
    print(add(num1,num2))
elif(select_num == 2):
    print('You select subtraction Enter two numbers')
    num1 = int(input('Enter num one: '))
    num2 = int(input('Enter num two: '))
    print(sub(num1,num2))
elif(select_num == 3):
    print('You select multiplication Enter two numbers')
    num1 = int(input('Enter num one: '))
    num2 = int(input('Enter num two: '))
    print(mul(num1,num2))
elif(select_num == 4):
    print('You select division Enter two numbers')
    num1 = int(input('Enter num one: '))
    num2 = int(input('Enter num two: '))
    print(div(num1,num2))
else:
    print('Invalid selection')
