import turtle as t
t.down()
k = 10
for i in range(4):
    t.forward(14 * k)
    t.right(120)
t.up()
for x in range(-1, 16):
    for y in range(-15, 2):
        t.goto(x * k, y * k)
        t.dot(2)
t.mainloop()