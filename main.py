import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("black")
drawing_board.title("Drawing Board")

turtle_instance=turtle.Turtle()
turtle_instance.color("white")

def go_left():
    turtle_instance.left(10)
def go_right():
    turtle_instance.right(10)
def go_forward():
    turtle_instance.forward(20)
def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()
def turtle_pen_up():
    turtle_instance.penup()
def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()

drawing_board.onkey(go_right,"d")
drawing_board.onkey(go_forward,"w")
drawing_board.onkey(go_left,"a")
drawing_board.onkey(clear_screen,"c")
drawing_board.onkey(return_home,"h")
drawing_board.onkey(turtle_pen_down,"u")
drawing_board.onkey(turtle_pen_down,"y")

turtle.mainloop()
