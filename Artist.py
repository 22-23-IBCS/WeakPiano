import turtle

class Artist:
    def __init__(self, t):
        self.t = t

    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def square(self, size = 150):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def circle(self, size = 1):
        for i in range(360):
            self.t.right(1)
            self.t.forward(size)

    def star(self, size = 1):
        for i in range(5):
            self.t.forward(100)
            self.t.right(144)
            self.t.forward(size)

    def polygon(self, size = 1): #This one is octagon
        for i in range(8):
            self.t.forward(100)
            self.t.right(45)
            self.t.forward(size)

    def hexagon (self, size = 1): #hexagon and nonagon are the two other shapes
        for i in range(7):
            self.t.forward(100)
            self.t.right(60)
            self.t.forward(size)

    def nonagon (self, size = 1):
        for i in range(9):
            self.t.forward(100)
            self.t.right(40)
            self.t.forward(size)
            
            
    def move(self, x, y):
             self.t.penup()
             self.t.goto(x,y)
             self.t.pendown()
             
             
def main():
    canvas = turtle.Screen()
    canvas.bgcolor("cyan")
    canvas.title("Turtle Example")
    t = turtle.Turtle()
    t.shape = ("Turtle")
    t.speed(0)
    art=Artist(t)
    art.triangle()
    t.penup()
    t.forward(200)
    t.pendown()
    art.square()
    t.penup()
    art.move(150,200)
    t.pendown()
    art.circle()
    t.penup()
    art.move(-150,200)
    t.pendown()
    art.star()
    t.penup()
    t.forward(100)
    t.pendown()
    art.polygon()
    t.penup()
    t.forward(200)
    t.pendown()
    art.hexagon()
    t.penup()
    art.move(-100,200)
    t.pendown()
    art.nonagon()

    
if __name__ == "__main__":
    main()
