### 코드를 줄여보아요.
##
##import turtle 
##
##t = turtle.Turtle()
##
##for count in range(6):
##    t.circle(100)
##    t.left(360/6)


### 도돌이표
##
##print("연주 순서")
##print("A", end=" ")
##print("B", end=" ")
##
##for i in range(2):
##    print("C", end=" ")
##    print("D", end=" ")


### n각형 그리기
##
##import turtle as t
##
##t.shape("turtle")
##n = int(t.textinput("", "몇 각형을 원하시나요?:"))
##
##for i in range(n):
##    t.forward(100)
##    t.left(360/n)


### 랜덤 워크 시뮬레이션
##
##import turtle as t
##import random as ra
##
##t.shape("turtle")
##
##for i in range(30):		
##   length = ra.randint(1, 100)
##   t.forward(length)
##   angle = ra.randint(-180, 180)
##   t.right(angle)


### 범인 찾기 게임
##
##import random as ra
##score = 0
##
##while True :
##    room = ra.randint(1, 3)
##    n = int(input("방 번호를 입력 하세요: "))
##
##    if n == room :
##        print("범인 체포!")
##        score += 10
##        break
##    elif n > 3 :
##        print(n,"번 방은 없습니다.")
##    else:
##        print("범인이 없습니다.")
##        score -= 10
##
##
##print("게임 종료")
##print("점수:", score,"점")


### 몬드리안 터틀
##
##import turtle, random
##
##t = turtle.Turtle( )
##t.pensize(3)
##
##for i in range(20) :		# 20개의 도형을 만듭니다.
##    r = random.random( )      # 0.0에서 1.0 사이의 난수 값 생성
##    g = random.random( )
##    b = random.random( )
##
##    x = random.randint(-300,300)      # -300에서 300 사이의 난수 값 생성
##    y = random.randint(-300,300)
##    length = random.randint(10,300)
##
##    t.penup()
##    t.goto(x,y)
##    t.pendown()
##    t.color(r, g, b)
##    
##    t.begin_fill( )
##    for j in range(4) :      # 사각형을 그린다. 
##        t.forward(length)
##        t.right(90)
##    t.end_fill( )


### 모든 약수 구하기
##
##n = int(input("자연수 입력: "))
##
##for i in range(1, n+1):
##    if n % i == 0 :
##        print(i, end=" ")


### 최대 공약수 구하기
##
##n = int(input("정수1 입력: "))
##m = int(input("정수2 입력: "))
##
##if n < m :
##        n, m = m, n
##
##while m > 0 :
##        r = n % m
##        n, m = m, r
##        
##if n != 1 :
##        print("두 수의 최대공약수:", n)
##else:
##        print("두 수는 서로소이다")


### 별 그리는 터틀
##
##import turtle as t
##
##t.shape("turtle")
##
##i = 0
##while i < 5:
##    t.forward(200)
##    t.right(144)
##    i += 1


### 숫자 맞추기 게임
##
##import random as ra
##
##tries = 1		# 게임 시도 횟수를 저장합니다.
##guess = 0		# 사용자가 입력한 수를 저장합니다.
##answer = ra.randint(1, 100)	# 1~100 사이의 임의의 수를 저장합니다.
##
##
##print("1부터 100 사이의 숫자를 맞추시오")
##guess = int(input("숫자를 입력하시오: "))
##
##while guess != answer:
##   tries = tries + 1
##   
##   if guess < answer:
##       print("낮음!")
##   elif guess > answer:
##       print("높음!")
##       
##   guess = int(input("숫자를 입력하시오: "))
##
##if guess == answer:
##    print("축하합니다. 시도횟수=", tries)


###     *
###    **
###   ***
###  ****
### *****
##
##for i in range(1, 6):
##    for j in range(1, 6 - i):
##        print(" ", end="")
##        
##    for j in range(1, i + 1):
##        print("*", end="")
##    print()


### 시작 정수와 높이를  입력 받아  다음을 출력 하는 프로그램 작성
### 시작 : 8
### 높이 : 5
### 8
### 89
### 890
### 8901
### 89012
##
##s = int(input("시작 : "))
##h = int(input("높이 : "))
##
##for i in range(1, h + 1):
##    for j in range(1, i + 1):
##        print((s + j - 1) % 10, end="")
##    print("")


### 시그마 (1/n)**2 = (pi**2) / 6
##
##s = 0
##n = int(input('정수 입력 : '))
##
##for i in range(1, n + 1):
##    s = s + (1/i)**2
##    
##print('결과는 %f입니다.'%s)


### 천천히 움직이는 직선 비행 경로 출력
##
##import turtle as t
##
##t.shape()
##t.up()
##t.goto(-900, 0)
##t.down()
##
##for i in range(600):
##    t.fd(i / 100)


### 비행기 이륙 경로 출력
##
##import turtle as t
##
##t.shape()
##t.up()
##t.goto(-450, -350)
##t.down()
##
##for i in range(200):
##    t.left(i / 1000)
##    t.fd(i / 20)


### 회전하면서 비행하는 경로 출력
##
##import turtle as t
##
##t.shape()
##
##for i in range(400):
##    t.left((400 - i) / 30)
##    t.fd(i / 40)


### 고장난 비행 경로 출력
##
##import turtle as t
##import random as ra
##
##t.shape()
##
##for i in range(400):
##    t.left(ra.randrange(-20, 50))
##    t.fd(i / 30)


### 구구단 출력
##
##for i in range(2, 10):
##    for j in range(1, 10):
##        print(i, '*', j, '=', i*j, end = ' ')
##    print()


### 1개의 반복문으로 구구단 출력
##
##i = 2
##
##for n in range(72):
##    j = (n % 9) + 1
##    print(i, '*', j, '=', i*j, end = ' ')
##
##    if j == 9:
##        i += 1
##        print()












