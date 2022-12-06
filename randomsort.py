import random

def main():

    L = [32, 14, 4, 90, 50, 55, 22, 78, 12]
    print(L)


    while True:
       maxPos = len(L) -1 
       x = []
       for i in range(len(L)):
           randomPos = random.randint(0, maxPos)
           x.append(L[randomPos])

       isSorted = True
       print(x)

       for i in range(len(L) -1):
           if x[i] > x[i+1]:
                isSorted = False
       if isSorted == True:
            break

if __name__ == "__main__":
    main()
