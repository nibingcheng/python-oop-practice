#
# Instructions:
# Work through the following prompts. Prompts marked with "We Do", we will work
# on together, as a class; prompts marked with "You Do", you will be given time
# to work through on your own.
#
# Tip: comment out your solution to each prompt before moving on to the next
# one! This will keep your console clear.
#

#
# Prompt 1: We Do
#
# Define a class for a Car. Your Car class should have the following
# properties:
#
#    - make
#    - model
#    - color
#
# Your Car class should have the following methods:
#
#    - drive: print 'vroom vroom' to the console
#
# Once you create your class definition create two instances.
#
# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color

#     def drive(self):
#         print('vroom vroom')

# first_car = Car('Ford', 'Taurus', 'Black')
# second_car = Car('Honda', 'Civic', 'Gray')

# print(first_car.color)
# second_car.drive()


#
# Prompt 2: We Do
#
# We're going to modify our Car class from the previous prompt and extend it to
# create a Toyota class:
#
#   - Extend your Car class to create a Toyota class. The make property will always
#     be 'Toyota'. Add a drive method to your Toyota class.
#
# Make an instance of your Toyota class.
#
# class Toyota(Car):
#     def __init__(self, model, color, make='Toyota'):
#         super().__init__(make, model, color)
#         # self.make = 'Toyota'
#         # self.model = model
#         # self.color = color
        
#     def __str__(self):
#         return f'{self.make} {self.model} {self.color}'

# third_car = Toyota('RAV4', 'White')
# # print(third_car)
# # third_car.drive()
    
    
#
# Prompt 3: You Do
#
# Define a class for your favorite animal (dog, cat, giraffe, etc). Give your
# class 3 attributes and two methods.
#
# After you've defined your class, create 3 instances.
#
# class Lion:
#     def __init__(self, sex, size, color):
#         self.sex = sex
#         self.size = size
#         self.color = color

#     def hunt(self):
#         print('Lion can kill')
        
#     def eat(self):
#         print('Lion eats a lot')
        
#     def __str__(self):
#         return f'{self.sex} {self.size} {self.color}'
        
# lion1 = Lion('female', 'small', 'brown')
# lion2 = Lion('male', 'large', 'gray')
# lion3 = Lion('female', 'mid-size', 'black')

# print(lion1, '\n', lion2, '\n', lion3)
# lion2.hunt()
# lion3.eat()



# Prompt 4: You Do
#
# Once we've completed the above, work through the following changes to your
# Car and Toyota classes:
#
#   - move the color property to your Toyota class
#   - move the drive method to your Car class
#   - add a property to your Toyota class
#   - add a property to your Car class and "fill it in" for your Toyota class
#
class Car:
    def __init__(self, make, model, style):
        self.make = make
        self.model = model
        self.style = style
        
    def drive(self):
        print('vroom vroom')

class Toyota(Car):
    def __init__(self, model, style, color, trans, make='Toyota'):
        super().__init__(make, model, style)

        self.trans = trans
        self.color = color
        
    def __str__(self):
        return f'{self.make} {self.model} {self.color} {self.style} {self.trans}'
    

new_car = Toyota('Camry', 'sedan', 'red', 'manual')
# print(new_car)
# new_car.drive()


#
# Prompt 5: You Do
#
# Define and Animal class with the following properties and methods:
#
#   - group (Invertebrates, Fish, Amphibians, Reptiles, Birds, and Mammals)
#   - eat: log "yum yum" to the console
#   - sleep: log "zzzzz" to the console
#
# Modify your animal from the previous prompt so that it extends your new
# Animal class.
#
# Create an instance of your animal class (the one that extends the Animal
# class).
#
class Animal:
    def __init__(self, group):
        self.group = group
       
    def sleep(self):
        print('zzzzz')
        
    def eat(self):
        print('yum yum')
        
    def __str__(self):
        return f'{self.group}'

class Lion(Animal):
    def __init__(self, group='Mammals'):
        super().__init__(group)
        
    def __str__(self):
        return f'{self.group}'
    
new_lion = Lion()    
# print(new_lion)
# new_lion.eat()
# new_lion.sleep()    


#
# Prompt 6: You Do
#
# Define a Card class with the following properties:
#
#   - suit (hearts, spades, clubs, diamonds)
#   - rank (Ace, 2, 3, 4, .. Jack, King, Queen)
#   - score (1, 2, 3, 4, ... 11, 12, 13)
#
# Define a Deck class with the following properties and methods:
#
#   - length (the number of cards - should start at 52)
#   - cards (an array of cards in the deck)
#   - draw: return a random card from the cards array
#
# When you create an instance of your Deck class (i.e. in your constructor),
# fill in the cards array with 52 instances of your Card class. You can do
# this with a nested for loop - first loop through an array of all possible
# suits, then loop through an array of all possible ranks. Inside your inner
# loop, create an instance of your Card class and push it into the Deck's cards
# array.
#
# Instantiate an instance of your Deck and start drawing random cards!
#
