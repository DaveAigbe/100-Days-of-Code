# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# colors_tuple = []
# for index in range(len(rgb_colors)):
#     colors_tuple.append((rgb_colors[index].r, rgb_colors[index].g, rgb_colors[index].b))
#
# print(rgb_colors)
# print(colors_tuple)

from turtle import Turtle, Screen
import random

colors_tuple = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

pointer = Turtle()
pointer.color('purple2')
pointer.shape('turtle')
pointer.speed('fastest')
pointer.penup()

x = -235
y = -235

screen = Screen()
screen.colormode(255)


for row in range(10):
    pointer.setposition(x, y)
    for draw_dots in range(10):
        pointer.dot(20, random.choice(colors_tuple))
        pointer.forward(50)
    y += 50

screen.exitonclick()