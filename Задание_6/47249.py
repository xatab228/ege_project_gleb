import turtle as t
t.down()
k = 30
for i in range(6):
    t.forward(13*k)
    t.right(120)
t.up()
for x in range(40):
    for y in range(-15, 1):
        t.goto(x * k, y * k)
        t.dot()
t.mainloop()