# import modules 
from PIL import Image
from numpy import asarray
import turtle

# open image 
img = Image.open("mahakal.jfif")
# get with and height
width,height = img.size
print(width)
print(height)
# convert Image into array 
img = asarray(img)

# print(img[100][400][0])


# set screen size 
turtle.screensize(canvwidth= width,canvheight= height,bg="white")
print(turtle.screensize())
# set the colormode
turtle.colormode(255)

tur = turtle.Turtle()

# setting pen speed 
tur.speed(0)

# setting pen to begin 
tur.penup()
tur.goto(-width/2,height/2)
tur.pendown()

# setting background color 
# turtle.bgcolor("cyan")

# variable to move tur to next line 
wid = 0
hei = height/2
# pixel skip level 
move = 2

for x in range(0,height,move):
    for y in range(0,width,move):
        cur_pix = img[x][y]
        print(cur_pix)
        tur.pencolor((cur_pix[0],cur_pix[1],cur_pix[2]))
        tur.dot(move)
        wid+=move
        tur.penup()
        tur.forward(move)
        tur.pendown()
        if wid >= width:
            wid = 0 
            hei-=move
            tur.penup()
            tur.goto(-width/2,hei)
            tur.pendown()

turtle.mainloop()
