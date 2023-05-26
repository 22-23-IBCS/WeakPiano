# Each method below currently does not run properly. Either it throws an error
# or it prints out/returns the wrong thing. Fix each method one by one.
# Comment out the method call in the main to run it and test it.
# You may need to import a library to get something to work!


#formal greeting. get the user's name and formally say hello to them
import math

def greet():
    name= {}
    name = input("What's your name?\n")
    greeting = "Hello, {}. It is nice to meet you"
    print(greeting.format(name))


#determine the area of a circle given its radius
def circleArea(r):
    if r <= 0:
        return "Invalid circle dimensions"
    else: 
        return round(math.pi * r ** 2,2)



#given a dictionary of students and their grades, print out which students
#need to study more (grade below 73)
def studyMore(D):
    for student, grade in D.items():
        if grade < 73:
            print(student+ " needs to study more.")

#given a dictionary of students and their grades, calculate
#the mean and median of the grades. print them out
def meanMedian(D):
    total = 0
    list = []
    for student in D:
        total = total + D.get(student)
        list.append(int(D.get(student)))
        list.sort()
        median = list[(len(list) // 2)]
        mean = round(total/len(D),2)


    print("Average grade was: " + str(mean))
    print("Median grade was: " + str(median))

def main():
    D = {"Jake" : 90,
         "Betty" : 20,
         "Aristotle" : 100,
         "Genghis" : 25,
         "Shirley" : 88,
         "Salt" : 6,
         "Charlie" : 91,
         "Seacrest" : 72,
         "Ryan": 73}

    r = float(input("Enter the radius of the circle: "))
    area = circleArea(r)
    print("The area of the circle is : " + str(area))
    greet()
    circleArea(r)
    studyMore(D)
    meanMedian(D)


if __name__ == "__main__":
    main()
