class Currency:


    def __init__(self):
        self.name = "Welcom to Currency Converter-"
        self.currencies = {1 : "USD", 2 : "EUR", 3 : "RMB", 4 : "JPY", 5: "GBP", 6: "INR"}
        self.exchangeUSD = {1: "1",
                          2: "0.93",
                          3: "6.79",
                          4: "131.44",
                          5: "0.83",
                          6: "82.71"}
        
        self.exchangeEUR = {1: "1.07",
                            2: "1",
                            3: "7.28",
                            4: "140.86",
                            5: "0.89",
                            6: "88.69"}
        
        self.exchangeRMB = {1: "0.15",
                            2: "0.14",
                            3: "1",
                            4: "19.35",
                            5: "0.12",
                            6: "12.18"}

        self.exchangeJPY = {1: "0.008",
                            2: "0.007",
                            3: "0.052",
                            4: "1",
                            5: "0.006",
                            6: "0.628"}

        self.exchangeGBP = {1: "1.202",
                            2: "1.122",
                            3: "8.158",
                            4: "158.45",
                            5: "1",
                            6: "99.482"}
        
        self.exchangeINR = {1: "0.012",
                            2: "0.011",
                            3: "0.082",
                            4: "1.592",
                            5: "0.01",
                            6: "1"}
        
    def op(self, ques, moneyin, rate):
        if ques == "1":
            h = self.convUSD.get(rate)
            k = (moneyin * float(h))
            return k
            
        if ques == "2":
            h = self.convEuro.get(rate)
            k = (moneyin *float(h))
            return k
            
        if ques == "3":
            h = self.convYuan.get(rate)
            k = (moneyin * float(h))
            return k
            
        if ques == "4":
            h = self.convLira.get(rate)
            k = (moneyin * float(h))
            return k

        if ques == "5":
            h = self.convVND.get(rate)
            k = (moneyin * float(h))
            return k

        if ques == "6":
            h = self.convBaht.get(rate)
            k = (moneyin * float(h))
            return k



def main():
    Z = Currency()
    print(Z.getName())
    x=(input("Please enter which type of currency you have.\n" + (Z.getCurrencies)))
                





if __name__=="__main__":
    main()
