class Vehicle:
    
    #constructor method (Need to define how the class instances are created
    def __init__(self, brand, color):
        self.numWheels = 4
        self.brand = brand
        self.color = color

    def getBrand(self):
        return self.brand

    def setBrand(self, x):
        self.brand = x

    


def main():
    #print("Hello World")
    veh1 = Vehicle("Toyota", "blue")
    x = veh1.getBrand()
    print(x)
    veh1.setBrand("Bugatti")
    print(veh1.getBrand())

if __name__ == "__main__":
    main()
