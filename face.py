import turtle
from random import randrange

class Face:
    def __init__(self):
        print("face object initialized")


    def moduledata(self):
        print("Face module info ***************")
        # print("     Smile (show smile on screen)")
        # print("     Sad (show sadness on screen)")
        # print("     Move_mouth ( move mouth while talking)")
        # print("end of info *****************")

        emotion = input('How you doing? (s=sad, h=happy ,m=mad ,y=yuck )  :')

        s = turtle.Screen()
        #s.setup(400, 300)
        t= turtle.Turtle(shape='turtle')
        t.color('orange','yellow')
        if emotion == 'y':
            t.color('orange', 'green')
        elif emotion == 'm':
            t.color('orange', 'red')

        t.speed(0)      #fastest...
        t.begin_fill()  #fill up the face color..
        t.circle(100)
        t.end_fill()
        t.penup()

        t.color('black','red')
        #eye
        t.goto(-30,135)
        t.pendown()
        t.dot(25)
        t.penup()

        t.goto(30, 135)
        t.pendown()
        t.dot(25)
        t.penup()

        #mouth
        if emotion == 'h':
            t.goto(-60,60)
            t.pendown()
            t.setheading(-60)   #circle starting point
            t.circle(70,120)
        else:
            t.goto(60, 60)
            t.pendown()
            t.setheading(120)  # circle starting point
            t.circle(70, 120)

        t.hideturtle()


Face().moduledata()

turtle.done()
