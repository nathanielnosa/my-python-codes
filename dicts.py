'''
Dictionary in python is just like an object in js, php
An object consists of key and value, between the key and value we use the column ":"
and end it with a comma for the next key and value.
to write an object we use the curly bracket - {}
'''

# person={
#     'f_name':'John',
#     'l_name':'Doe',
#     'age':23,
#     'm_status':'married',
#     'disability':False
# }
# # print(type(person))
# # print(person)
# # print(person('m_status'))

# # print(person['m_status'])
# person['phone'] = +234912345678

# # print(person.keys())
# # print(person.items())
# person2 = person.copy()
# person2['height'] = 5.6

# print(len(person))
# print(person2)


# LIST OF DICTIONARY

people = [
    {
        'id':1,
        'f_name':'Alugo',
        'l_name':'Zainab',
        'm_status':'married',
        'age': 25
    },
    {
        'id':2,
        'f_name':'Akata',
        'l_name':'Daniel',
        'm_status':'complicated',
        'age': 27
    },
    {
        'id':3,
        'f_name':'Eromose',
        'l_name':'Charles',
        'm_status':'single',
        'age': 26
    }
]
# print(people)

# print(people[1]) #charles
# r2
# print(people('m_status')) # daniel
# print(people[2('m_status')]) # zainab wt #charles
# print(people[2]['m_status']) 

num1 = int(input('Enter num one: '))
num2 = int(input('Enter num two: '))
num3 = int(input('Enter num three: '))

if (num1 > num2) and (num1 > num3):
    print(f'{num1} is big')
elif (num2 > num1) and (num2 > num3):
    print(f'{num2} is big')
elif (num3 > num1 )and (num3 > num2):
    print(f'{num3} is big')
else:
    print('they are all equal')
