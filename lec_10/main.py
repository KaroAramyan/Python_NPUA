from Vehicle import vehicle

class Car(vehicle):
    def __init__(self, color, year, price):
        super().__init__(color, year, price)
    def WhatIsThis(self):
        print("This is Car")    
    
class Plane(vehicle):
    def __init__(self, color, year, price):
        super().__init__(color, year, price)
    def WhatIsThis(self):
        print("This is Plane")
class Boat(vehicle):
    def __init__(self, color, year, price):
        super().__init__(color, year, price)
    def WhatIsThis(self):
        print("This is Plane")
    