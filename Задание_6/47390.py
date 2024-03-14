import turtle as t
k = 30
t.speed(0)
for i in range(12):
    t.rt(60)
    t.fd(1 * k)
    t.rt(60)
    t.fd(1 * k)
    t.rt(270)

t.up()

for x in range(-10, 5):
    for y in range(-5, 4):
        t.goto(x * k, y * k)
        t.dot(3)
t.mainloop()