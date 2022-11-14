import turtle as t

t.bgcolor('black')
t.pencolor('green')
for i in range(220):
    t.rt(i)
    t.speed(speed=0.1)
    t.circle(220,i)
    t.fd(i)
    t.rt(90)
t.done()
