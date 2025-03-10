import turtle
# 변수 사용하기
x = 100
y = 200
print("x =", x)
print("y =", y)
print(x+y)
sum = x + y
print(sum)
sum = sum + 10
print(sum)


name1 = "홍길동"
name2 = "성춘향"
address = "서울시 종로구 1번지"
print(name1)
print(name2)
print(address)

print("23" + "56")
print(23 + 56)

#snake_case
my_new_car = "나의 새로운 차"
myNewCar = "나의 새로운 차"

#한번에 여러 값을 출력하기
x = 100
y = 200
sum = x+y
print(x, "과", y, "의 합은", sum, "입니다.")


#입력을 받을때는 키보드를 누르면 아스키코드값을 생성하고 -> 컴퓨터의 CPU로 전달된다.->CPU는 아스키 코드로 인식을 한다.
#키보드로 들어오는 모든 입력은 문자열이다. 
#문자열 입력받기
'''
a = input()
print(a)
a = input("입력")
print(a)
'''

'''
name = input("이름을 입력하시오: ")
print(name, "씨 안녕하세요?")
print("파이썬에 오신 것을 환영합니다.")
'''

#수 입력받기
x = int(input("첫 번째 정수를 입력하시오:"))
y = int(input("두 번째 정수를 입력하시오:"))
sum = x + y
print(x, "과", y, "의 합은", sum, "입니다.")

print(x, "+", y, "=",x+y)
print(x, "-", y, "=",x-y)
print(x, "*", y, "=",x*y)
print(x, "/", y, "=",x/y)

x = float(input('실수 입력 : '))
y = float(input('실수 입력 : '))
print(x)
print(y)
print(x + y)

turtle.done()  # 창을 닫지 않고 유지