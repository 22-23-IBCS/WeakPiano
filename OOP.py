# IBCS Python Coding Quiz Practice #1
# Name: 

# Read the questions below carefully. Each question describes a
# method that you will need to define with code. In order to demonstrate
# that your method works and test your code, you will need to 'un-comment'
# the method call in the main() method


# 1. Define a method which takes in one two integers, prints out
# which one is smaller and which one is larger. Also, it returns
# the sum of the numbers, the product of the two numbers, and the
# the quotient of the numbers where the larger number is the denominator.
def twoNumCalc(num1, num2):
    if num1 > num2:
        larnum = num1
        smlnum = num2
        qut = num1/num2
        
        
    else:
        larnum = num2
        smlnum = num1
        qut = num2/num1
        
    total = num1 + num2
    prod = num1 * num2
    
    
    return 'Larger', larnum, 'Smaller', smlnum, 'Sum', total, 'Product', prod, 'Quotient', qut



# 2. Define a method which asks the user to input a first name. Then asks
# the user to input a last name. The method should create an email for
# them which starts with the first 3 letters of their first name and
# ends with the last 4 letters of their last name. The email address
# should include '@example.com' and should be returned
# Example: "Zack Considine" --> "zacdine@example.com"
def newEmail(firstname, lastname):
    firstname = firstname.lower()

    lastname = lastname.lower()

    part1 = firstname[0] + firstname[1] + firstname[2]

    part2 = lastname[0] + lastname[1] + lastname[2] + lastname[3]
    
    print("Email: " + part1 + part2 + "@example.com")
    


def main():

    #print(twoNumCalc(2, 5))
    #print(twoNumCalc(3, 8))
    print(twoNumCalc(10, 4))

    newEmail(input("Enter your first name\n"), input("Enter your last name\n"))
    

if __name__ == "__main__":
    main()
