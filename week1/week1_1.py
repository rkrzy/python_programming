import turtle
# 문자 출력하기
'''
 print("반가워요" * 20)
 print("100" + "200")
 print(100 + 200)
'''

#그림 그리기
'''
t = turtle.Turtle()
t.shape("turtle")   
t.forward(100)
t.left(90)
t.forward(50)
'''

#사각형 그리기
'''
t = turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
'''

#삼각형 그리기
'''
t = turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
'''

#다각형 여러개 그리기
'''
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5
'''

#원 그리기
'''
t = turtle.Turtle()
t.shape("turtle")
t.circle(100)
'''
#정육각형 그리기
'''
t = turtle.Turtle()
t.shape("turtle")
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
'''

#선 굵게 그리기
'''
t = turtle.Turtle()
t.shape("turtle")
t.width(10)

t.forward(100)
t.left(90)
t.forward(100)
'''
#거북이 색깔 바꾸기
'''
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

t.forward(100)
t.left(90)
t.forward(100)
'''
# 모양 바꾸기
'''
t = turtle.Turtle()
t.shape("square")

t.forward(100)
t.left(90)
t.forward(100)
'''

# 펜사용하기
t = turtle.Turtle()
t.shape("square")

t.down()
t.goto(100,0)
t.up()
t.goto(0,200)
t.down()
t.goto(100, 200)
turtle.done()  # 창을 닫지 않고 유지


