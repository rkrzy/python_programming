
# #LAB 01
# print("반지름이 10인 원의 넓이:", 10 * 10 * 3.14)
# print("반지름이 20인 원의 넓이:", 20 * 20 * 3.14)
# print("반지름이 30인 원의 넓이:", 30 * 30 * 3.14)
# print("반지름이 40인 원의 넓이:", 40 * 40 * 3.14)
# print("반지름이 50인 원의 넓이:", 50 * 50 * 3.14)


# PI = 3.14
# print("반지름이 10인 원의 널이:", 10 * 10 * PI)
# print("반지름이 20인 원의 널이:", 20 * 20 * PI)
# print("반지름이 30인 원의 널이:", 30 * 30 * PI)
# print("반지름이 40인 원의 널이:", 40 * 40 * PI)
# print("반지름이 50인 원의 널이:", 50 * 50 * PI)

# #LAB 02
# import turtle 
# t = turtle.Turtle()
# t.shape("turtle")

# radius = int(input("원의 반지름을 입력하시오:"))
# color = input("원의 색깔을 입력하시오:")

# t.color(color)
# t.begin_fill()
# t.circle(radius)
# t.end_fill()

# LAB 03
# second = int(input("측정 시간(초) 입력:"))
# light = 300000
# sound = 340

# lightDistance = 300000000 * second
# soundDistance = 340 * second

# print("자신의 위치에서 번개가 친 장소까지의 거리=",soundDistance)

# # x + y 출력하기
# x = 100
# y = 200
# sum = x + y
# print(x,"와",y,"의 합은", sum, "입니다")

# 이름을 입력받고 출력하기
'''
name = input("이름을 입력하세요")
print(name, "씨, 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")
'''

# 사칙 연산
'''
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))


print(x , "+", y ,"=", x + y)
print(x , "-", y ,"=", x - y)
print(x , "/", y ,"=", x / y)
print(x , "*", y ,"=", x * y)
'''

# 형식지정자가 있는 print() 사용법
n = 100
print("10진수 100 = %d" %n)
print("100의 8진수 = %o" %n)
print("100의 16진수 = %x" %n)

print(bin(100))
print(oct(100))
print(hex(100))

