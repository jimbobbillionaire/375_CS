from graphics import *
size = eval(input("How big do you want to make the window? "))

win = GraphWin("Scaling Example", size, size)
win.setCoords(0, 0, size, size)


def main():

    win.setBackground('black')


    edge1 = Line(Point(15,15), Point(-15,-15))
    edge1.setOutline('white')
    edge1.setFill('white')
    edge1.draw(win)
    edge2 = Line(Point(15,-15), Point(-15,15))
    edge2.setOutline('white')
    edge2.setFill('white')
    edge2.draw(win)
    center = Circle(Point(0,0), 10)
    center.setFill('black')
    center.setOutline('black')
    center.draw(win)

    while True:
        click_point = win.getMouse()
        current_x = center.getCenter().getX()
        current_y = center.getCenter().getY()

        next_x = click_point.getX()
        next_y = click_point.getY()

        delta_x = next_x - current_x
        delta_y = next_y - current_y

        center.move(delta_x, delta_y)

        cxe1p1 = edge1.getP1().getX()
        cye1p1 = edge1.getP1().getY()
        nxe1p1 = click_point.getX()
        nye1p1 = click_point.getY()
        dxe1p1 = nxe1p1 - cxe1p1
        dye1p1 = nye1p1 - cye1p1

        edge1.move(delta_x, delta_y)
        edge2.move(delta_x, delta_y)

        draw_head_shot()

input("hit enter to stop")

def draw_head_shot():
    edge = Circle(Point(size/2,size/1.5), size/20)
    edge.setFill('black')
    edge.setOutline('white')
    edge.draw(win)
    centerhs = Circle(Point(size/2,size/1.5), size/40)
    centerhs.setFill('red')
    centerhs.setOutline('red')
    centerhs.draw(win)
    line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(centerhs.getCenter().getX(),edge.getRadius()))
    line.setOutline('white')
    line.setFill('white')
    line.draw(win)
    line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(centerhs.getCenter().getX(),edge.getRadius()))
    line.setOutline('white')
    line.setFill('white')
    line.draw(win)
    line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(edge.getRadius(),centerhs.getCenter().getY()))
    line.setOutline('white')
    line.setFill('white')
    line.draw(win)
    line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(edge.getRadius(),centerhs.getCenter().getY()))
    line.setOutline('white')
    line.setFill('white')
    line.draw(win)

main()
