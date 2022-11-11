from graphics import*
from Button import*

def main():

    win = GraphWin("Character Creation", 800, 600)

    B1 = Button(win, Point(650, 50), Point(750, 125), "salmon", "Face")

    B2 = Button(win, Point(650, 150), Point(750, 225), "Blue", "Big Eyes")
    
    B3 = Button(win, Point(650, 250), Point(750, 325), "Brown", "Small Eyes")
    
    B4 = Button(win, Point(650,350), Point(750, 425), "Red", "Closed Mouse")

    B5 = Button(win, Point(650, 400), Point(750, 450), "Yellow", "Open Mouse")

    B6 = Button(win, Point(550,70), Point(650,130), "Orange", "Round Nose")

    B7 = Button(win, Point(550,250), Point(650,300), "Green", "Flat Nose")
    
    Face = Oval(Point(150, 50), Point(550, 550))
    #Face.draw(win)
    bigEye1 = Circle(Point(350, 250), 40)
    #bigEye1.draw(win)Button(win, Point(650, 450), Point(750, 525), "salmon", "Smile Mouse")

    bigEye2 = Circle(Point(450, 250), 40)
    #bigEye2.draw(win)
    smallEye1 = Circle(Point(350, 250), 20)
    smallEye2 = Circle(Point(450, 250), 20)
    ClosedMouse = Oval(Point(350,400),Point(500,400))
    OpenMouse = Rectangle(Point(350,450),Point(500,400))
    RoundNose = Circle(Point(400, 300), 30)
    FlatNose = Rectangle(Point(450,300),Point(400,300))
    

    Q = QuitButton(win, Point(650, 500), Point(750, 575))

    while True:
        m = win.getMouse()
        if B1.isClicked(m):
            Face.undraw()
            Face.draw(win)

        if B2.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()

            bigEye1.draw(win)
            bigEye2.draw(win)

        if B3.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            smallEye1.undraw()
            smallEye2.undraw()

            smallEye1.draw(win)
            smallEye2.draw(win)
            
        if B4.isClicked(m):
            ClosedMouse.undraw()
            OpenMouse.undraw()
            ClosedMouse.draw(win)

        if B5.isClicked(m):
            OpenMouse.undraw()
            ClosedMouse.undraw()
            OpenMouse.draw(win)

        if B6.isClicked(m):
            RoundNose.undraw()
            FlatNose.undraw()
            RoundNose.draw(win)

        if B7.isClicked(m):
            FlatNose.undraw()
            RoundNose.undraw()
            FlatNose.draw(win)


        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
