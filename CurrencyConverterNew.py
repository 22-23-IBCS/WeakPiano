class Currency_Converter():
    countries = ["China", "Japan", "England", "Australia", "France", "Korea"]
    rates = {"China": 6.9457, "Japan": 134.62, "England": 0.7986, "France": 0.9152, "Australia" : 1.493, "Korea":1333.68}
    currencies= {"China": "CNY", "Japan":"JPY", "England": "GBP", "France": "EUR", "Australia": "AUD", "Korea":"KRW"}

    def __init__(self):
        self.result= 0
        
    def get_countries(self):
        return self.countries
    
    def get_conversion_rate(self,country):
        return self.rates[country]
    
    def USD_to_others(self,amount,country):
        self.result=  amount* self.get_conversion_rate(country)
    
    def country_convert_country(self,country1,amount, country2):
        self.result= amount/ self.get_conversion_rate(country1) * self.get_conversion_rate(country2)

    def display(self, country):
        print(self.result,self.currencies[country])

while True:
    print("1: convert an amount of US dollors to another country's currency")
    print("2: convert an amount of money (any currency) to another currency")
    print("3: quit")


    option = input("Enter your choice: \n")
    
    if option == "3":
        print("See you next time")
        break
    
    elif option == "1":
        obj = Currency_Converter()
        print("Avaiable countries:")
        print(obj.get_countries())
        
        country = input("Choose a country from the list above:")
        amount = float(input("Enter the amount of money (US dollar):"))
        
        obj.USD_to_others(amount,country)
        obj.display(country)

    elif option == "2":
        obj = Currency_Converter()
        print (obj.get_countries())
        country1 = input("Convert from: ")
        country2 = input("COnvert to: ")
        amount = float(input("Enter amount of money: "))
                       
        obj.country_convert_country(country1,amount,country2)
        obj.display(country2)

    else:
        print("Invalid input, try again")
