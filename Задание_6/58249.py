import turtle
scale = 10
turtle.color("black", "red") # (black - border) (red - inside/fill)
turtle.begin_fill() # Start filling

turtle.seth(90)
turtle.width(2)
turtle.speed(20)


for i in range(5):
    turtle.seth(0)
    turtle.circle(5 * scale, 180)
    turtle.seth(90)
    turtle.circle(5 * scale, 180)
    turtle.seth(180)
    turtle.circle(5 * scale, 180)
    turtle.seth(270)
    turtle.circle(5 * scale, 180)

turtle.end_fill()

canvas = turtle.getcanvas()
count = 0

for x in range(-100 * scale, 100 * scale, scale):
    for y in range(-100 * scale, 100 * scale, scale):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1
print(count)
turtle.done()