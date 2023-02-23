import random
import time 

def main():

    L = []
    n = 15000
    for i in range(n):
        L.append(random.randint(0,n))

    print(L)
    print("commence selection sort")
    start = time.time()

    #Selection sort
    for i in range(len(L) - 1):
        x = L[i]
        indexx = i
        for j in range(i, len(L)):
            if L[j] < x:
                x = L[j]
                indexx= j

        #swap
        temp = L[i]
        L[i] = L[indexx]
        L[indexx] = temp
    #print(L)
    print("done")
    stop = time.time()
    total = stop-start
    print("For " + str(n) + " elements") 
    print("Time passed:" + str(total))


if __name__ == "__main__":
    main()
