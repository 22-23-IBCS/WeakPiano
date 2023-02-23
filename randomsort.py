import random
import time 

def main():

    L = []
    n = 100
    for i in range(n):
        L.append(random.randint(0,n))


    #print(L)
    print("commence random sort")

    #sort with Bubble sort
    start = time.time()


    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                #swap
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
            print(L)
    stop = time.time()
    total = stop-start
    print("For " + str(n) + " elements") 
    print("Time passed:" + str(total))
            
if __name__ == "__main__":
    main()
