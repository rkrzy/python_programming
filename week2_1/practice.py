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

n = 100
f = 3.141592
c = 'A'
s = "string"

print("%d = "%n, type(n), "%f = "%f, type(f), "%c = "%c, type(c), "%s = "%s, type(s))




