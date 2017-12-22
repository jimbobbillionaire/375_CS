#This program is a simulator for the killfeed in Call of Duty. As you click the crosshair of the weapons follows your mouse.
#Everytime you click it simulates a kill
#The player getting the kills name is Jokiilo
#The players usernames on the recieving end of kills are Jimbobbillionaire, ebilton, and tds6161
#If i had more time, i would add the players on the screen randomly appearing so you are required to click them in order for the kills to show up in the feed
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
        #This part of the program makes it so everytime you click, the crosshair moves with the mouse and a kill show up in the feed.
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

        draw_head_shot_2()

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

        draw_head_shot_3()

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

        draw_head_shot_4()



#The four "draw_headshot" functions are the drawings of the 4 seperate kills in the feed

def draw_head_shot():
    edge = Circle(Point(size/2,size/1.5), size/20)
    edge.setFill('black')
    edge.setOutline('white')
    edge.draw(win)
    centerhs = Circle(Point(size/2,size/1.5), size/40)
    centerhs.setFill('red')
    centerhs.setOutline('red')
    centerhs.draw(win)
    #These lines are intented to form the crosshair in the center of the circle, however getting the lines to work the way i intended was difficult
    #line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(centerhs.getCenter().getX(),edge.getRadius()))
    #line.setOutline('white')
    #line.setFill('white')
    #line.draw(win)
    #line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(centerhs.getCenter().getX(),edge.getRadius()))
    #line.setOutline('white')
    #line.setFill('white')
    #line.draw(win)
    #line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(edge.getRadius(),centerhs.getCenter().getY()))
    #line.setOutline('white')
    #line.setFill('white')
    #line.draw(win)
    #line = Line(Point(centerhs.getCenter().getX(),centerhs.getCenter().getY()), Point(edge.getRadius(),centerhs.getCenter().getY()))
    #line.setOutline('white')
    #line.setFill('white')
    #line.draw(win)
    #
    jokiilo1 = Text(Point(centerhs.getCenter().getX() - size/4.5,centerhs.getCenter().getY()), "Jokiilo")
    jokiilo1.setTextColor('blue')
    jokiilo1.draw(win)
    jvmpbarresi = Text(Point(centerhs.getCenter().getX() + size/4.5,centerhs.getCenter().getY()), "jvmpbarresi")
    jvmpbarresi.setTextColor('red')
    jvmpbarresi.draw(win)

def draw_head_shot_2():
    edge2 = Circle(Point(size/2,size/2), size/20)
    edge2.setFill('black')
    edge2.setOutline('white')
    edge2.draw(win)
    centerhs2 = Circle(Point(size/2,size/2), size/40)
    centerhs2.setFill('red')
    centerhs2.setOutline('red')
    centerhs2.draw(win)
    jokiilo2 = Text(Point(centerhs2.getCenter().getX() - size/4.5,centerhs2.getCenter().getY()), "Jokiilo")
    jokiilo2.setTextColor('blue')
    jokiilo2.draw(win)
    jimbob = Text(Point(centerhs2.getCenter().getX() + size/3.75,centerhs2.getCenter().getY()), "jimbobbillionaire")
    jimbob.setTextColor('red')
    jimbob.draw(win)
#
def draw_head_shot_3():
    edge = Circle(Point(size/2,size/2.5), size/20)
    edge.setFill('black')
    edge.setOutline('white')
    edge.draw(win)
    centerhs3 = Circle(Point(size/2,size/2.5), size/40)
    centerhs3.setFill('red')
    centerhs3.setOutline('red')
    centerhs3.draw(win)
    jokiilo3 = Text(Point(centerhs3.getCenter().getX() - size/4.5,centerhs3.getCenter().getY()), "Jokiilo")
    jokiilo3.setTextColor('blue')
    jokiilo3.draw(win)
    ebilton = Text(Point(centerhs3.getCenter().getX() + size/4.5,centerhs3.getCenter().getY()), "ebilton")
    ebilton.setTextColor('red')
    ebilton.draw(win)

def draw_head_shot_4():
    edge = Circle(Point(size/2,size/3.5), size/20)
    edge.setFill('black')
    edge.setOutline('white')
    edge.draw(win)
    centerhs4 = Circle(Point(size/2,size/3.5), size/40)
    centerhs4.setFill('red')
    centerhs4.setOutline('red')
    centerhs4.draw(win)
    jokiilo4 = Text(Point(centerhs4.getCenter().getX() - size/4.5,centerhs4.getCenter().getY()), "Jokiilo")
    jokiilo4.setTextColor('blue')
    jokiilo4.draw(win)
    tds6161 = Text(Point(centerhs4.getCenter().getX() + size/4.5,centerhs4.getCenter().getY()), "tds6161")
    tds6161.setTextColor('red')
    tds6161.draw(win)

main()
