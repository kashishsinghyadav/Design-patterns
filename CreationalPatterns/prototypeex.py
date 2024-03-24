import copy 
class UIComponent:
    def clone(self):
        return copy.deepcopy(self)
    
class Button(UIComponent):
    def __init__(self,label):
        self.label=label

    def render(self):
        return f"Buttoon:{self.label}"
    
class Textfield(UIComponent):
    def __init__(self,holder):
        self.holder=holder
    def render(self):
        return f"textfield:{self.holder}"
    
btproto=Button('submit')
textproto=Textfield('enter your name')
print(btproto.render())
print(textproto.render())
obj1=btproto.clone()
obj2=textproto.clone()
obj1.label='Next'
obj2.holder='enter details'
print(obj1.render())
print(obj2.render())
