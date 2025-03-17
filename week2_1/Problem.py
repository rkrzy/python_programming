import turtle as t

#오륜기 그리기
t.pensize(5)
t.up()
t.goto(-150, 0)
t.down()
t.color("blue")
t.circle(70)

t.up()
t.goto(0, 0)
t.down()
t.color("black")
t.circle(70)

t.up()
t.goto(150, 0)
t.down()
t.color("red")
t.circle(70)

t.up()
t.goto(-75, -75)
t.down()
t.color("yellow")
t.circle(70)

t.up()
t.goto(75, -75)
t.down()
t.color("green")
t.circle(70)

t.done()