from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass 

class Dog(Animal):

    def speak(self):
        return 'boo booo'
class Lion(Animal):
    def speak(self):
        return 'he he he'
    
# factoryyy classs 
class FactoryClass:
    def getanimal(self,animal):
        if animal=='dog':
            return Dog()
        elif animal=='lion':
            return Lion()
        else:
            ValueError('you are fool')

obj=FactoryClass()
dog=obj.getanimal('dog')
print(dog.speak())
lion=obj.getanimal('lion')
print(lion.speak())
