class Car:#product1
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

class Manual:#product 2
     def __init__(self):
        self.content = ""
#builder interface
class Builder:
    def reset(self):
        pass
    def set_seats(self, seats): 
        pass
    def set_engine(self, engine): 
        pass
    def set_trip_computer(self):
        pass
    def set_gps(self):
        pass
    def get_product(self):
        
        pass

#concrete classes 

class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_seats(self, seats):
        self.car.seats = seats

    def set_engine(self, engine):
        self.car.engine = engine

    def set_trip_computer(self):
        self.car.trip_computer = True

    def set_gps(self):
        self.car.gps = True

    def get_product(self):
        return self.car

class CarManualBuilder(Builder):
    def __init__(self):
        self.manual = Manual()

    def reset(self):
        self.manual = Manual()

    def set_seats(self, seats):
        self.manual.content += f"Document car seat features: {seats}\n"

    def set_engine(self, engine):
        self.manual.content += f"Add engine instructions: {engine}\n"

    def set_trip_computer(self):
        self.manual.content += "Add trip computer instructions\n"

    def set_gps(self):
        self.manual.content += "Add GPS instructions\n"

    def get_product(self):
        return self.manual

# Director
class Director:
    def construct_sports_car(self, builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("SportEngine")
        builder.set_trip_computer()
        builder.set_gps()

class Application:
    def make_car(self):
        director = Director()

        car_builder = CarBuilder()
        director.construct_sports_car(car_builder)
        car = car_builder.get_product()

        manual_builder = CarManualBuilder()
        director.construct_sports_car(manual_builder)
        manual = manual_builder.get_product()

        print(car.__dict__)
        print(manual.__dict__)

app = Application()
app.make_car()


