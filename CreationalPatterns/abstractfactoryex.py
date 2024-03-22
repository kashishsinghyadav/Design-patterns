from abc import ABC,abstractmethod 
#abstract factory 

class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass 
    @abstractmethod
    def create_topping(self):
        pass 

class IndianStylePizza(PizzaFactory):
    def create_pizza(self):
        return IndianPizza()
    def create_topping(self):
        return Indiantopping()
    
class RussianStylePizza(PizzaFactory):
    def create_pizza(self):
        return RussianPizza()
    def create_topping(self):
        return Russiantopping()
    
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass
class Topping(ABC):
    @abstractmethod
    def addtopping(self):
        pass 

class IndianPizza(Pizza):
    def prepare(self):
        return "Preparing indian pizza "
class Indiantopping(Topping):
    def addtopping(self):
        return "added more masala :)" 
class RussianPizza(Pizza):
    def prepare(self):
        return "preparing russian pizza" 
class Russiantopping(Topping):
    def addtopping(self):
        return "added russian :)"
    
def orderpizza(factory):
    piz=factory.create_pizza()
    top=factory.create_topping()
    return piz.prepare(),top.addtopping()

fact=IndianStylePizza()
factp,facttop=orderpizza(fact)
print(factp)
print(facttop)
factR=IndianStylePizza()
factr,factrtop=orderpizza(factR)
print(factr)
print(factrtop)

    

