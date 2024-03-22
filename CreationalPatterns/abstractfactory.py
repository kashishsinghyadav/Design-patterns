#The Abstract Factory Pattern is another creational design pattern, similar to the Factory Pattern, but with an added layer of abstraction. It provides an interface for creating families of related or dependent objects without specifying their concrete classes
from abc import ABC,abstractmethod 

#abstract factory 
class GUI(ABC):
    @abstractmethod
    def button(self):
        pass 
    @abstractmethod
    def checkbox(self):
        pass 

class WindowGui(GUI):
    def button(self):
        return Windowbutton()
    def checkbox(self):
        return Windowcheckbox()
    
class MacGui(GUI):
    def button(self):
        return Macbutton()
    def checkbox(self):
        return Maccheckbox() 
    
class Button(ABC):
    @abstractmethod
    def render(self):
        pass 
class Cheackbox(ABC):
    @abstractmethod
    def render(self):
        pass 
class Windowbutton(Button):
    def render(self):
        return "Render Window button"
    
class Windowcheckbox(Cheackbox):
    def render(self):
        return "Render window checkbox"
class Macbutton(Button):
    def render(self):
        return "Render Mac button"
class Maccheckbox(Button):
    def render(self):
        return "Render Mac checkbox"
    
def create_gui(factory):
    bt=factory.button()
    ch=factory.checkbox()
    return bt.render(),ch.render() 

window=WindowGui()
windowbt,windowch=create_gui(window)
print(windowbt)
print(windowch)
mac=MacGui()
macbt,macch=create_gui(mac)
print(macbt)
print(macch)
    
