# we do this on friday
# # CLASS
# class BluePrintDogs:
#     # instance of a class
#     # property
#     def __init__(self,height,name,color,leg):
#         self.name = name
#         self.height = height
#         self.color = color
#         self.leg = leg
#     # method
#     def bark(self):
#         return f'my name is {self.name} and i can bark'
#     def run(self):
#         return f'I saw {self.name} run with is {self.leg} legs'


# # create objects - initializing a class object
# d1 = BluePrintDogs(2.5,'Bingo','Black',4)
# print(d1.bark())
# print(d1.run())

# ::: inheritance

# # Inheritance
# class Person:
#     def __init__(self, name, email,age):
#         self.name = name
#         self.email = email
#         self.age = age
#     def greetings(self):
#         return f'My name is {self.name} i am {self.age}, you can mail me {
#         self.email}'
    
# class User(Person):
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.sex = 'Male'
#     def gender(self, sex):
#         self.sex = sex

# john = User('Zainab', 'john@gmail.com', 20)
# john.gender('Male')
# print(john.sex)

# # ::classes of class
# class Circle:
#     pi = 3.142    @classmethod
#     def value(cls):
#         return f'a circle has a default pie value = {cls.pi}'

# # initialize a circle object
# c1 = Circle(5)

# print(c1.pi)
# print(c1.value())
# print(Circle.pi)


# class Planet:
#     #class properties
#     shape = 'round'
#     #instance properties
#     def __init__ (self, name, radius):
#         self.name = name
#         self.radius = radius
#     #instance method
#     def orbit(self):
#         return f'{self.name} is a good planet'
#     # class method
#     @classmethod
#     def common(cls):
#         return f'all the planet are {cls.shape} due to gravity'

# # initialise an object

# venus = Planet('Venus', 3)
# print(venus.name)
# print(venus.radius)
# print(venus.shape)
# print(venus.orbit())
# print(venus.common())
# print(Planet.shape)
# print(Planet.common())


