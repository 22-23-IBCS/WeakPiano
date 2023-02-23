import random
class House:
    def __init__(self):
        self.rating = random.randint(1,10)
    def getRating(self):
        return self.rating
def randPath(m, num):
    p= []

    while (len(p)<num):
        p=[]



        
def main(): 
    m = [[],[],[],[],[]]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())
    for i in range (5):
        print(m[0][i], m[1][i],m[2][i],m[3][i],m[4][i])

    num = int(input("How many houses?_ \n"))
    x= random.randint(0,4)
    y= random.randint(0,4)
    m[x][y]
    print (random.choices(x,y))
    
    
    
if __name__ =="__main__":
    main()
