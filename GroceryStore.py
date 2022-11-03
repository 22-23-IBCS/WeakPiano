class GroceryStore():


   def __init__(self):
        self.Cooking_Oil = 10.00
        self.Pizza = 5.00
        self.Cheese = 1.00
        self.Egg = 2.00
        self.Potato = 1.00
        self.Cereal = 4.00
        self.Bread = 5.00
        self.Meat = 15.00
        self.Icecream = 6.00
        self.Tomato = 5.00
        self.product = {"Cooking_Oil" : 10.00,
               "Pizza" : 5.00,
               "Cheese" : 0.50,
               "Egg" : 4.00,
               "Potato" : 1.00,
               "Cereal" : 6.00,
               "Bread" : 5.00,
               "Meat" : 15.00,
               "Icecream" : 6.00,
               "Tomato" : 5.00}
        self.product = ""

        def getPrice(self, x):
            self.Price = x

        def setProduct(self):
            return self.product        

def main():

    grocery = {"Cooking_Oil" : 10.00,
               "Pizza" : 5.00,
               "Cheese" : 1.00,
               "Egg" : 4.00,
               "Potato" : 1.00,
               "Cereal" : 6.00,
               "Bread" : 5.00,
               "Meat" : 15.00,
               "Icecream" : 6.00,
               "Tomato" : 5.00}
    print("Welcome to Frank's grocery store, we have the following products:\n")
    print(list(grocery.keys()))
    
    request = input("\nWhat food would you like to buy?\n")
    price = grocery.get(request)
    many = int(input("How many would you want?\n"))
    print("Here you go\nYou got " + str(many) + " "+ request)
    print("That would be $" + str(price*many) + " dollars")

    toBuy=[]
    while True:
       print(list(grocery.keys()))
       request2 = input("If you want to stop shopping, type stop, or you can shop once again.\n")
       if request2 == "stop":
          print("Thank you for shopping with us.")
          break
       else:
          price2 = grocery.get(request2)
          many2 = int(input("How many would you want?\n"))
          print("Here you go\nYou got " + str(many2) + " "+ request2)
          print("That would be another $" + str(price2*many2) + " dollars")
      

if __name__ =="__main__":
    main()
