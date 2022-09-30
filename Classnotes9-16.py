def main():
    name = input("What is your name?\n")

    print("Hello, " + name + "!")

    age = int(input("How old are you?\n")) #Str of the number
    age= age + 10    #10 is integer, concatnate str and int 
    print("Wow. Old! " + str(age)) #change age back to string to print

if __name__ == "__main__":
    main()
