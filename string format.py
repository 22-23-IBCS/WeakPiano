import random

def main():
    L1 = []
    sample = open("oneSyllable.txt")
    myString = sample.read()
    myList = myString.split()
    for word in myList:
        word = word.lower()
        L1.append(word)
        

    L2 = []
    sample = open("twoSyllable.txt")
    myString = sample.read()
    myList = myString.split()
    for word in myList:
        word = word.lower()
        L2.append(word)
        

    L3 = []
    sample = open("threeSyllable.txt")
    myString = sample.read()
    myList = myString.split()
    for word in myList:
        word = word.lower()
        L3.append(word)
        

    L4 = []
    sample = open("fourSyllable.txt")
    myString = sample.read()
    myList = myString.split()
    for word in myList:
        word = word.lower()
        L4.append(word)

    Haiku =  

    
            
if __name__ == "__main__":
    main()
