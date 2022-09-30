class Cat:
    
    def __init__(self, breed, eyecolor, tail ):
        self.numLegs= 4
        self.breed = breed
        self.eyecolor = eyecolor
        self.tail = tail
        

    def getBreed(self):
        return self.breed

    def setBreed(self, x):
        self.breed = x

    def getEyecolor(self):
        return self.eyecolor

    def setEyecolor(self, y):
        self.eyecolor = y

    def getTail(self):
        return self.tail

    def setTail(self, z):
        self.tail = z

   


def main():
    print("My favorite pet are cats, my cats' apperance are:")
    cat1 = Cat("British Shorthair:", "Black colored eye,", "medium tail.")
    cat2 = Cat("Pastoral cat:", "Yellow colored eye,", "long tail.")
    x= cat2.getBreed()
    y= cat2.getEyecolor()
    z= cat2.getTail()
    print(x,y,z)
    cat1.setBreed("British Shorthair:")
    print(cat1.getBreed(), cat1.getEyecolor(),cat1.getTail())
    

    

if __name__ == "__main__":
    main()
