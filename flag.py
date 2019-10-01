import turtle
import math

tur = turtle.Turtle()

cell = 30
smallstar_center_coord = [[-5, 8], [-3, 6], [-3, 3], [-5, 1]]
bigstart_center_coord = [-10.0, 5.0]
raw_to_deg = 180/math.pi
deg_to_raw = math.pi/180


def draw_rectangle():
    tur.goto(-15*cell, 10*cell)
    tur.color('red', 'red')
    tur.begin_fill()
    for i in range(2):
        tur.forward(cell * 15 * 2)
        tur.right(90)
        tur.forward(cell * 10 * 2)
        tur.right(90)
    tur.end_fill()


def draw_star(len):
    tur.color('yellow', 'yellow')
    tur.begin_fill()
    for i in range(5):
        tur.forward(len)
        tur.right(144)
    tur.end_fill()
    tur.color('red', 'red')


def draw_smallstar():
    for coord in smallstar_center_coord:
        dertX = bigstart_center_coord[0] - coord[0]
        dertY = bigstart_center_coord[1] - coord[1]

        tur.goto((coord[0]+dertX/math.sqrt(math.pow(dertX, 2)+math.pow(dertY, 2)))*cell,
                    (coord[1]+dertY/math.sqrt(math.pow(dertX, 2)+math.pow(dertY, 2)))*cell)
        tur.left(math.atan(dertY/dertX)*raw_to_deg + 18)
        draw_star(2*cell*math.cos(18 * deg_to_raw))
        tur.right(math.atan(dertY/dertX)*raw_to_deg + 18)

def draw_flag():
    # 绘制国旗面
    draw_rectangle()

    # 绘制大星星
    tur.goto(-10*cell, 8*cell)
    tur.right(72)
    draw_star(6*cell*math.cos(18 * deg_to_raw))
    tur.left(72)

    # 绘制小星星
    draw_smallstar()

draw_flag()

turtle.mainloop()

# github:NotFound404Forbidden


