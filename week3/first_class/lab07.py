number = int(input("정수를 입력하시오: "))

sum = 0
sum = sum + number % 10      
number = number // 10        

sum = sum + number % 10      
number = number // 10        

sum = sum + number % 10      
number = number // 10           # 100자리 수 삭제

sum = sum + number % 10      # 1000자리 수 추출
number = number // 10           # 1000자리 수 삭제

print("자릿수의 합: %d" %sum)