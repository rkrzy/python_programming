# 한 번에 여러 값을 출력하기
'''
x = 100
y = 200
sum = x + y
print(x, "과", y, "의 합은", sum, "입니다.")
'''

# 문자열 입력받기
'''
name = input("이름을 입력하시오: ")
print(name, "씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")
'''

# 수  입력받기

#############################################
## 정수 2개 입력받기
## x = int(input("첫 번째 정수를 입력하시오: "))
## y = int(input("두 번째 정수를 입력하시오: "))
## sum = x + y
## print(x, "과", y, "의 합은", sum, "입니다.")


#############################################
## 사용자로부터 2개의 정수를 받아서 사칙연산(+, -, *, /)의 결과를 출력
'''
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))

print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "*", y, "=", x * y)
print(x, "/", y, "=", x / y)
'''

# 반지름을 입력 받아 원 넓이, 원주 구하여 출력
'''
radius = int(input("반지름 입력 :  "))
PI = 3.141592
area = PI * radius * radius
circum = PI * radius * 2

print("반지름이 ", str(radius), "인 원의 넓이는 ", str(area), "원주는", str(circum))
'''

#      print() 함수 서식
#      %d ==== 10진수
#      %x ==== 16진수
#      %o ==== 8진수
#      %f ==== 실수(소수점이 있는 수)
#      %c ==== 문자 
#      %s ==== 문자열

#  형식지정자가 있는 print() 사용법
'''
n = 100
print("10진수 100 = %d" %n) 
print("100의 16진수 =  %x" %n)
print("100의 8진수 =  %o" %n)
'''
# 문자열과 수를 함께 출력할 때 형식지정자를 사용
'''
print("100의 16진수, 8진수는 ", "%d, %x, %o" %(100, 100, 100), "입니다.")
'''

# 10진수를  bin(), oct(), hex() 내장 함수를 사용하여 변환
'''
print(bin(100))
print(oct(100))
print(hex(100))
'''

# 진법 변환과 변수 입력 input()
'''
sel = int(input("입력 진수 결정(16/10/8/2) : "))
num = input("값 입력 : ")

if sel == 16 :
    num10 = int(num, 16)
if sel == 10 :
    num10 = int(num, 10)
if sel == 8 :
    num10 = int(num, 8)
if sel == 2 :
    num10 = int(num, 2)
    
print("16진수 ==> ", hex(num10))
print("10진수 ==> ", num10)
print(" 8진수 ==> ", oct(num10))
print(" 2진수 ==> ", bin(num10))
'''

# 보기 좋은 출력 예시
'''
print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")
'''
# format() 함수와 { }를 사용하여 형식 지정
'''
print("%d %5d %05d" %(123, 123, 123))
print("{0:d} {1:5d} {2:05d}" .format(123, 123, 123))
'''

# 이스케이프 문자
#       \n  ==== 줄 바꿈
#       \t   ==== 탭
#       \b  ==== 백스페이스
#       \\ ==== \ 출력
#       \'   ==== ' 출력
#       \"   ==== " 출력
'''
print("\n줄 바꿈\n연습 ")
print("\t탭 키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")
'''
# print(r"")형식은 이스케이프 문자까지 그대로 출력

# 변수의 type()

'''
n = 100
f = 3.141592
c = 'A'
s = "string"

print("%d = "%n, type(n), "%f = "%f, type(f), "%c = "%c, type(c), "%s = "%s, type(s))
'''

# 웹 사이트 오픈
'''
import webbrowser

url = input("사이트 url 입력 : ")
webbrowser.open(url)
'''

# https://docs.python.org/ko/3/library/turtle.html
# 오륜기 그리기, 오륜기 이미지 검색
# turtle 좌표 체계는 화면 정중앙이 (0, 0)
# pensize(), up(), down(), goto(), color(), circle() 사용
'''
import turtle
t = turtle.Turtle()
t.pensize(10)


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
'''

# 마우스로 그림 그리기(마우스 이벤트 처리) 
# 함수 사용, 아직 배우지 않았음
# 기능1 : 마우스 왼쪽 버튼 클릭
#           이전 좌표에서 마우스 왼쪽 버튼 클릭한 위치까지 임의의 색상으로 선 그리기
# 기능2 : 마우스 오른쪽 버튼 클릭
#           이전 좌표에서 마우스 오른쪽 버튼 클릭한 위치까지 선을 그리지 않고 이동
# 기능3 : 마우스 중앙 버튼 클릭
#            거북이를 임의의 크기로 변경, 선도 임의의 색으로 변경
# random 라이브러리 사용, 사용법 검색
# random(), randrange(), onscreenclick()
'''
import turtle as t
import random as ra

def sLeft(x, y):
    global r, g, b
    t.color((r, g, b))
    t.down()
    t.goto(x, y)

def sMid(x, y):
    global r, g, b
    tSize = ra.randrange(1, 5)
    t.shapesize(tSize)
    pSize = ra.randrange(1, 11)
    t.pensize(pSize)
    r = ra.random()
    g = ra.random()
    b = ra.random()

def sRight(x, y):
    t.up()
    t.goto(x, y)

def key_reset():                    # 추가된 키 이벤트 처리 함수 
    t.resetscreen()

def key_quit():                      # 추가된 키 이벤트 처리 함수
    t.bye()

r = g = b = 0.0

t.title("마우스로 그림 그리기")
t.shape("turtle")
s = t.Screen()                       # 키 이벤트 추가

t.onscreenclick(sLeft, 1)        # 마우스 왼쪽 버튼 클릭 이벤트 
t.onscreenclick(sMid, 2)        # 마우스 중앙 버튼 클릭 이벤트 
t.onscreenclick(sRight, 3)      # 마우스 오른쪽 버튼 클릭 이벤트 

s.onkey(key_reset, 'r')          # r 키 프레스 이벤트          
s.onkey(key_quit, 'q')           # q 키 프레스 이벤트 
s.listen()
'''

# 3개의 정수를 입력 받아 제일 큰수를 찾는 방법
'''
w = int(input("첫번째 정수 입력 : "))
x = int(input("두번째 정수 입력 : "))
y = int(input("세번째 정수 입력 : "))
z = int(input("네번째 정수 입력 : "))

if w > x and w > y and w > z:
    print("w = %d 이/가 제일 큰 정수 입니다." %w)
elif x > y and x > z:
    print("x = %d 이/가 제일 큰 정수 입니다." %x)
elif y > z:
    print("y = %d 이/가 제일 큰 정수 입니다." %y)
else:
    print("z = %d 이/가 제일 큰 정수 입니다." %z)
'''

# 3개의 정수 중 가장 큰 홀수 출력, 만일 홀수가 없으면 가장 작은 수 출력
# max(), min() 사용
'''
w = int(input("첫번째 정수 입력 : "))
x = int(input("두번째 정수 입력 : "))
y = int(input("세번째 정수 입력 : "))

if w % 2 != 0 and x % 2 != 0 and y % 2 != 0:
    print("가장 큰 홀수 는 %d" %max(w, x, y))
    
if w % 2 != 0 and x % 2 != 0 and y % 2 == 0:
    print("가장 큰 홀수 는 %d" %max(w, x))
    
if w % 2 != 0 and x % 2 == 0 and y % 2 != 0:
    print("가장 큰 홀수 는 %d" %max(w, y))
    
if w % 2 == 0 and x % 2 != 0 and y % 2 != 0:
    print("가장 큰 홀수 는 %d" %max(x, y))
    
if w % 2 != 0 and x % 2 == 0 and y % 2 == 0:
    print("가장 큰 홀수 는 %d" %w)
    
if w % 2 == 0 and x % 2 != 0 and y % 2 == 0:
    print("가장 큰 홀수 는 %d" %x)
    
if w % 2 == 0 and x % 2 == 0 and y % 2 != 0:
    print("가장 큰 홀수 는 %d" %y)
    
if w % 2 == 0 and x % 2 == 0 and y % 2 == 0:
    print("가장 작은  짝수 는 %d" %min(w, x, y))
'''

# 개선된 방법
'''
w = int(input("첫번째 정수 입력 : "))
x = int(input("두번째 정수 입력 : "))
y = int(input("세번째 정수 입력 : "))

ans = min(w, x, y)

if w % 2 != 0:
    ans = w

if x % 2 != 0 and x > ans:
    ans = x
    
if y % 2 != 0 and y > ans:
    ans = y
    
print("실행 결과 : %d" %ans)
'''






