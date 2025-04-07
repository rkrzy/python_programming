### 직각삼각형 판별하기
##
##a = int(input("변a의 길이: "))
##b = int(input("변b의 길이: "))
##c = int(input("변c의 길이: "))
##
##if c ** 2 == a ** 2 + b ** 2:			
##    print("직각삼각형입니다.")
##else:
##    print("직각삼각형이 아닙니다.")



### 정수의 종류를 판별하는 스마트 터틀
##import turtle as t
##
##t.shape("turtle")
##t.penup()		# 펜을 올려서 그림이 그려지지 않게 합니다. 
##t.goto(100, 100)		# 터틀을 (100, 100)으로 이동시킵니다.
##t.write("입력된 정수는 양의 정수입니다.")
##t.goto(100, 0)
##t.write("입력된 정수는 0입니다.")
##t.goto(100, -100)
##t.write("입력된 정수는 음의 정수입니다.")
##
##t.goto(0, 0)		# (0, 0) 위치로 터틀을 이동시킵니다.
##t.pendown()		# 펜을 내려서 그림이 그려지게 합니다. down( )도 있습니다.
##s = t.textinput("", "숫자를 입력하시오: ")
##n = int(s)
##
##if n > 0 :
##    t.goto(100, 100)
##if n == 0 :
##    t.goto(100, 0)
##if n < 0 :
##    t.goto(100, -100)



### 주민등록번호 뒷자리 의미, 이런 뜻이?!
##import random as ra				# 난수 모듈을 불러옴
##
##print("주민등록번호의 성별 정보 번호를 생성합니다.")
##gender = ra.randrange(4)
##gender = gender + 1
##
##print("생성번호: ", gender)	   	# 문자와 숫자 연결하여 출력할 때를 주의
##
##if gender == 1 or gender == 3:	            # gender가 1 또는 3이면 남성
##    print("남성입니다")
##else :					# gender가 2 또는 4이면 여성
##    print("여성입니다")
##    
##print("프로그램을 종료합니다.")



### 동전 던지기 게임
##import turtle as t		    # 터틀 그래픽 모듈을 불러옴
##import random as ra		    # 난수 모듈을 불러옴
##
##screen = t.Screen()
##image1 = "앞.gif"
##image2 = "뒤.gif"
##
##screen.addshape(image1)
##screen.addshape(image2)
##
##coin = ra.randint(0, 1)	# 동전의 앞, 뒤 정보 만들기
##
##if coin == 0 :
##    t.shape(image1)
##    t.stamp()
##else : 
##    t.shape(image2)
##    t.stamp()



### 찌릿찌릿 전기 회로
##
##a = input("1번 전지가 있습니까? (Y/N) ")
##b = input("2번 전지가 있습니까? (Y/N) ")
##
##if a.upper() == 'Y' and b.upper() == 'Y':
##    print("직렬연결 : 전구에 불이 켜집니다.")
##else :
##    print("직렬연결 : 전구에 불이 꺼집니다.")
##
##if a.upper() == 'Y' or b.upper() == 'Y':
##    print("병렬연결 : 전구에 불이 켜집니다.")
##else :
##    print("병렬연결 : 전구에 불이 꺼집니다.")



### 윤년판단
##
##year = int(input("연도를 입력하시오: "))
##if ( (year % 4 ==0 and year % 100 != 0) or year % 400 == 0):
##    print(year, "년은 윤년입니다.")
##else :
##    print(year, "년은 윤년이 아닙니다.")



### 이차방정식 판별
##
##a=float(input("a값 입력: "))
##b=float(input("b값 입력: "))
##c=float(input("c값 입력: "))
##
##D = b ** 2 - 4 * a * c
##
##if D > 0 :
##    print("방정식의 근은 서로 다른 두 실근입니다.")
##elif D == 0 :
##    print("방정식은 서로 같은 두 실근(중근)입니다.")
##else :
##    print("방정식은 서로 다른 두 허근입니다.")



### 사용자가 원하는 도형 그리기
##import turtle as t
##
##t.shape("turtle")
##s = t.textinput("", "도형을 입력하시오: ")
##
##if s == "직사각형" :
##    w = int(t.textinput("","가로: "))    
##    h = int(t.textinput("","세로: "))    
##    t.forward(w)
##    t.left(90)
##    t.forward(h)
##    t.left(90)
##    t.forward(w)
##    t.left(90)
##    t.forward(h)
##elif s == "정삼각형" :
##    w = int(t.textinput("","한 변의 길이: "))    
##    t.forward(w)
##    t.left(120)
##    t.forward(w)
##    t.left(120)
##    t.forward(w)
##    t.left(120)
##elif s == "원" :
##    w = int(t.textinput("","반지름의 길이: "))    
##    t.circle(w)



### 두 원 위치 관계 시뮬레이션
##import turtle as t
##
##t.shape()
##x1 = int(input("큰 원의 중심좌표 x1: "))
##y1 = int(input("큰 원의 중심좌표 y1: "))
##r1 = int(input("큰 원의 반지름: "))
##x2 = int(input("작은 원의 중심좌표 x2: "))
##y2 = int(input("작은 원의 중심좌표 y2: "))
##r2 = int(input("작은 원의 반지름: "))
##
##t.penup( )
##t.goto(x1, y1 - r1)         # circle( )의 특성으로 인해 원을 그리는 위치 조정
##t.pendown( )
##t.circle(r1)
##
##t.penup( )
##t.goto(x2, y2 - r2)         # circle( )의 특성으로 인해 원을 그리는 위치 조정
##t.pendown( )
##t.circle(r2)
##
###dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5  	#두 원의 중심사이의 거리
##dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
##
##if dist == 0:
##    t.write("동심원")
##elif dist == r1 - r2:
##    t.write("내접")
##elif r1 - r2 < dist < r1 + r2:
##    t.write("두 점에서 만납니다.")
##elif dist > r1 + r2:
##    t.write("만나지 않고 외부에 있습니다.")
##elif dist == r1 + r2:
##    t.write("외접")
##elif dist < r1 - r2: 
##    t.write("만나지 않고 내부에 있습니다.")



### 10진수를 2진수로 변환
##n = int(input("255이하 정수 입력 : "))
##b = ''
##d = n
##for i in range(8):
##    if d % 2 :
##        b += '1'
##        d //= 2
##    else:
##        b += '0'
##        d //= 2
##
##print("10진수 %d는 2진수로 : "%n, b[ : :-1])



### bin()을 사용한 2진수 출력
##n = int(input("255이하 정수 입력 : "))
##print("10진수 %d는 2진수로 : "%n, bin(n))
##print("10진수 %d는 2진수로 : "%n, bin(n)[2::])
##print("10진수 %d는 2진수로 : "%n, format(bin(n)[2::]).zfill(8))



### 10진수를 16진수로 변환
##n = int(input("255이하 정수 입력 : "))
##b = ''
##d = n
##for i in range(2):
##    r = d % 16
##
##    if r < 10:
##        b += str(r)
##        d //= 16
##    elif r == 10:
##        b += 'a'
##        d //= 16
##    elif r == 11:
##        b += 'b'
##        d //= 16
##    elif r == 12:
##        b += 'c'
##        d //= 16
##    elif r == 13:
##        b += 'd'
##        d //= 16
##    elif r == 14:
##        b += 'e'
##        d //= 16
##    else:
##        b += 'f'
##        d //= 16    
##
##print("10진수 %d는 16진수로 : "%n, b[ : :-1])



### 중첩 if문 예
##n = int(input("2 또는 3으로 나누어지는지 판별할 정수 입력 : "))
##
##if n % 2 == 0:
##    if n % 3 == 0:
##        print("2와 3으로 나누어짐")
##    else:
##        print("3으로 나누어지지 않고, 2로 나누어짐")
##elif n % 3 == 0:
##    print("2로 나누어지지 않고, 3으로 나누어짐")
##else:
##    print("2와 3 모두  나누어지지 않음")


### 3항 조건 연산자
##n = int(input("점수 입력 : "))
##point = 0
##
##print(n, "점은 합격 입니다.") if n >= 60 else print(n, "점은 불합격 입니다.")



### 3개의 정수 중 가장 큰 정수
##x = 10
##y = 20
##z = 3
##
##if x > y and x > z:
##    print("x = %d 이/가 제일 큰 정수 입니다." %x)
##elif y > z:
##    print("y = %d 이/가 제일 큰 정수 입니다." %y)
##else:
##    print("z = %d 이/가 제일 큰 정수 입니다." %z)
##
##print((x if x > z else z) if x > y else (y if y > z else z))










