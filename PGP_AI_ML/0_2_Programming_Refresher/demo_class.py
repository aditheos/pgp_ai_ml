'''
Created on 4 Oct. 2021

@author: praka
'''
class Animal():
    eyes = 2
    def talk(self):
        return "Animal Talk"
    
class Dog(Animal):
    legs = 4
    def talk(self):
        return "Woof Woof"
    
bingo = Dog()
print("Bingo has " + str(bingo.eyes) + " eyes")
print("Bingo has " + str(bingo.legs) + " legs")
print("Bingo says " + bingo.talk())