#composition is a clsas thta exists inside of another class (class ha other clsas)

class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
    
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"
    
class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque

    def ignite(self):
        print("vroom vroom whee hee hohoho teehee chugga chugga choo choo grahhh")
    
myEngine = Engine("V8", 5.8, 326, 344)
myCar = Car("Mazda", "Mazda3", "1378", myEngine)

#to access a composite class you need to call that item. obviously

print(myCar)
myCar.engine.ignite()