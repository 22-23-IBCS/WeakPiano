import random
def RandomInteger():

    x=random.randint(1,100)
    if x%2 != 0:
        return False
        if x%3!=0:
            return False
        if x%5 != 0:
            return False
    else:
        return True
        
def RandList(x):
    for i in range(10):
        x= random.randint(1,50)
        print(x)
        
    
        
def main():
    print(x)
