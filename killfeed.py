from graphics import *
size = eval(input("How big do you want to make the window? "))

win = GraphWin("Scaling Example", size, size)
win.setCoords(0, 0, size, size)


def main():

    win.setBackground('black')

    win.getMouse()
    draw_head_shot()
    input("hit enter to stop")


def draw_head_shot():
    circle = Circle(Point(size/2,size/2), size/20)
    circle.setFill('black')
    circle.setOutline('white')
    circle.draw(win)
    line = Line(Point(size/2, size/2), (5, 5))
    line.setOutline('white')
    line.setFill('white')
    line.draw(win)

main()
