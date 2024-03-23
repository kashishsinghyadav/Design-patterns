
class Pizza:# this is called builder
    def __init__(self,builder):
        self.size=builder.size 
        self.cheese=builder.cheese
        self.pepperoni=builder.pepperoni
        self.mushroom=builder.mushroom
    def __str__(self):
        return f"size:{self.size},cheese:{self.cheese},pepperoni:{self.pepperoni},mushroom:{self.mushroom}"

class PizzaBuilder:
    def __init__(self,size):
        self.size=size
        self.cheese=False
        self.pepperoni=False
        self.mushroom=False 
    def add_cheese(self):
        self.cheese=True
        return self 
    def add_pepperoni(self):
        self.pepperoni=True
        return self
    def add_mushroom(self):
        self.mushroom=True 
        return self 
    
    def build(self):
        return Pizza(self)
    
builder = PizzaBuilder(size="Large")
builder.add_cheese().add_pepperoni().add_mushroom()
pizza = builder.build()
print(pizza)
