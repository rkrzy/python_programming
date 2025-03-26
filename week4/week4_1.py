# # 문자열에서 연속된 문자열 추출하는 프로그램
# '''
s = "Hello Python"

print("s = ", s)
print("s[0] = ", s[0])		
print("s[1] = ", s[1])
print("s[-1] = ", s[-1])
print("s[6:10] = ", s[6:10])
print("s[-6:-2] = ", s[-6:-2])
print("s[0:10:2] = ", s[0:10:2])
print("s[-1:-7:-1] = ", s[-1:-7:-1])
print("s[::-1] = ", s[::-1]) 
# '''

# 문자열 처리 예,  'abcdef'에서 'cde'만 출력
'''
print('abcdef'[2:5:1])
print('abcdef', '문자열 길이 : ', len('abcdef'))
'''

# 문자열 처리 예,  'abcdef'에서 'dcb'만 출력
'''
print('abcdef'[-3:-6:-1])
'''

## 자료 종류 확인
'''
x = 10
print(x, ": ", type(x))

x = 3.14
print(x, ": ", type(x))

x = 'python'
print(x, ": ", type(x))

x = 2+1j
print(x, ": ", type(x))

x = True
print(x, ": ", type(x))

x = [1,2,3,4]
print(x, ": ", type(x))

x = (1,2,3)
print(x, ": ", type(x))

x = {1:'a', 2:'b', 'c':3}
print(x, ": ", type(x))

def x():
    return 1
print(x, ": ", type(x))

x = None
print(x, ": ", type(x))
'''

#복소수 사칙연산
'''
c = 3 + 4j
c1 = 4 + 3j

print(c.real)                 # 실수부 출력
print(c.imag)               # 허수부 출력
print(c.conjugate())        # 켤레 복소수 출력
print(abs(c))                # 복소평면 원점에서 c까지 거리 출력

print(c * c.conjugate())        # 복소수 c와 켤레 복소수 곱 출력
print(c * c)                        # 복소수 c * c  출력
print(abs(c) * abs(c))          # 복소수 c 까지 거리 곱  출력

print(c + c1)                    # 복소수 c + c1  출력
print(c - c1)                    # 복소수 c - c1  출력
print(c * c1)                    # 복소수 c * c1  출력
print(c / c1)                    # 복소수 c / c1  출력
'''

# 변수의 주소 출력 id()
'''
x = 1
print("x = ", id(x))

x = 2
print("x = ", id(x))

x = 10
print("x = ", id(x))

y = [1,2,3]
print("y = ", id(y))
print("y[0] = ", id(y[0]))

y[0] = 10
print("y = ", id(y))
print("y[0] = ", id(y[0]))
'''


# 소금물의 농도는?
'''
print("소금물의 농도를 구하는 프로그램입니다")

salt = int(input("소금의 양은 몇 g입니까? "))
water = int(input("물의 양은 몇 g입니까? "))
density = salt / (salt+water) * 100

print("소금물의 농도: " + str(density) + "%")
'''

# 간단한 챗봇(ChatBot) 프로그램
'''
print("안녕하세요")
name = input('이름이 뭐예요? ')

print("만나서 반갑습니다. " + name + "님")
print(name + "님 이름의 길이는 다음과 같군요:", end=' ')
print(len(name))

age = int(input("나이가 어떻게 되요? "))         
print("내년이면 "+ str(age+1)+ "세가 되시는 군요")
'''

# 거북이와 인사 해봐요.
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "이름을 입력하시오: ")
t.write("안녕하세요?" + s +"씨, 터틀 인사드립니다.");

#사각형 그리기    
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''

# 암호프로그램 만들기
'''
P = "도서관에서 보자"

print("평문:",P)
print("암호문:", P[-1: -9 :-1])
print("암호문:", P[:  :-1])
'''

# 2050년에 나는 몇 살?
'''
import time
now = time.time()
thisYear = int(1970 + now//(365*24*3600))

print("올해는 " + str(thisYear)+"년입니다.")

age = int(input("당신의 나이를 입력 하세요: "))
print("2050년에는 "+str(age + 2050-thisYear)+"살이군요.")
'''

# 문자열 처리 함수 upper(), lower(), swapcase(), title()
'''
s = 'Python is Easy.'

print("s = ", s)
print("upper() = ", s.upper())                 # 대문자 변환
print("lower() = ", s.lower())                  # 소문자 변환
print("swapcase() = ", s.swapcase())     # 대 -> 소,  소 -> 대 문자로 변환
print("title() = ", s.title())                       # 시작 문자만 대문자로 변환
'''

# 문자열 처리 함수 count(), find(), rfind(), index(), rindex(), startswith(), endswith()
'''
s = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'

print("s = ", s)
print("count() = ", s.count('공부'))     # 찾을 문자열 출연 개수 
print("find() = ", s.find('공부'))           # 왼쪽부터 찾을 문자열 시작 위치 값 
print("find() = ", s.find('공부', 5))       # 왼쪽 5번째에서 찾을 문자열 시작 위치 값
print("find() = ", s.find('없다'))
print("rfind() = ", s.rfind('공부'))         # 오른쪽 부터 찾을 문자열 시작 위치 값
print("index() = ", s.index('공부'))       # find()와 결과를 같음.
print("index() = ", s.index('공부', 5))
print("rindex() = ", s.rindex('공부'))
# print("index() = ", s.index('없다'))      # 오류 발생, find()와 다른 점
print("startswith() = ", s.startswith('파이썬'))  # 찾을 문자열로 시작하면 True, 아니면 False
print("startswith() = ", s.startswith('파이썬', 10))
print("endswith() = ", s.endswith('^^'))  # 찾을 문자열로 끝나면 True, 아니면 False
'''

# 문자열 처리 함수 strip(), rstrip(), lstrip(), replace()
'''
s = '   파  이  썬   '
print("s = ", s)
print("strip() =", s.strip())   # 문자열 양쪽 공백 제거
print("rstrip() =", s.rstrip()) # 문자열 오른쪽 공백 제거
print("lstrip() =", s.lstrip())  # 문자열 왼쪽 공백 제거

s = '---파--이--썬---'
print("s = ", s)
print("strip() =", s.strip('-'))   # 문자열 양쪽 '-' 제거

s = '<<==파--이--썬!>>'
print("s = ", s)
print("strip() =", s.strip('<=!>'))   # 문자열 양쪽 '<=!>' 제거

s = '열심히 파이썬 공부 중~~~'
print("s = ", s)
print("replace() = ", s.replace("파이썬", 'Python'))  # 현재문자열을 다음 문자열로 교체
'''

# 문자열 처리 함수 split(), splitlines(), join()
'''
s = '열심히 파이썬 공부 중~~~'
print("s = ", s)
print("split() = ", s.split())  # 공백으로 문자열 분리 후 list로 반환

s = '열심히:파이썬:공부:중~~~'
print("s = ", s)
print("split(':') = ", s.split(':'))  # ':' 로 문자열 분리 후 list로 반환

s = '열심히\n파이썬\n공부\n중~~~'
print("s = ", s)
print("splitlines() = ", s.splitlines())  # 행 단위로 문자열 분리 후 list로 반환

s = '%'
print("join() = ", s.join('python'))  # '%'를 문자열 join() 문자열 사이에 넣어줌
'''

# 문자열 처리 함수 center(), ljust(), rjust(), zfill()
'''
s = '파이썬'
print("s = ", s)
print("center() = ", s.center(11))      # 11자리에 문자열 가운데 정렬
print("center() = ", s.center(11, '*')) # 11자리에 문자열 가운데 정렬, 양쪽에 '*'로 마무리
print("ljust() = ", s.ljust(11))            # 11자리에 문자열 왼쪽 정렬
print("rjust() = ", s.rjust(11))            # 11자리에 문자열 오른쪽 정렬
print(".zfill() = ", s.zfill(11))             # 문자열 오른쪽 정렬 후 앞쪽 11자리 에 '0'으로 채움
'''

# 문자열 처리 함수 isdigit(), isalpha(), isalunm(), islower(), isupper(), isspace()
'''
print('123'.isdigit())
print('123'.isalpha())
print('123'.isalnum())

print('abc'.isdigit())
print('abc'.isalpha())
print('abc'.isalnum())

print('123abc'.isdigit())
print('123abc'.isalpha())
print('123abc'.isalnum())

print('Abc'.islower())
print('abc'.isupper())
print('ABc'.islower())
print('aBC'.isupper())
print('a B'.isspace())
print(' '.isspace())
print('    '.isspace())
'''













