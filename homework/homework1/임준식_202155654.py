def rotate_left(value, n):
    return ((value<<n) | (value >> (32-n))) & 0xFFFFFFFF

def rotate_right(value, n):
    return ((value >> n) | (value << (32-n))) & 0xFFFFFFFF

def print_binary(value):
    return format(value,'032b')


print("32비트 양방향 rotate 프로그램\n")

number1 = int(input("32비트 정수 입력 : "))
number2 = int(input("1~31 정수 입력 : "))
rotate = input("방향 l은 왼쪽, r은 오른쪽 : ").lower()
result = 0
binary_value = print_binary(number1)

print(f"입력 2진수 : {binary_value} 를 ", end='')

if rotate == 'l':
    result = rotate_left(number1, number2)
    print(f"왼쪽 {number2} 비트 rotate 하면")
elif rotate == 'r':
    result = rotate_right(number1, number2)
    print(f"오른쪽 {number2} 비트 rotate 하면")
else: 
    exit()

binary_value = print_binary(result)
print(f"출력 2진수 : {binary_value}")

