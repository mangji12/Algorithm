# 문제 1
number = input("숫자를 입력해주세요 > ") # 사용자 입력
number1 = int(number) + 10
print(number1)

# 문제 2
fav_food = input("좋아하는 음식을 입력해 주세요 > ")
print("좋아하는 음식 > {}".format(fav_food))

# 문제 3
name = input("이름을 입력해 주세요 > ")
since = input("태어난 년도를 입력해주세요 > ")
age = 2023 - int(since)
print("저의 이름은 {0} 이고, 올해 나이는 {1}세 입니다.".format(name,age))

# 문제 4

first_sen = input("첫 번째 문장을 입력해주세요 > " ) # 사용자 입력
second_sen = input("두 번째 문장을 입력해주세요 > ") 
print(first_sen + second_sen)

# 문제 5
num = int(input("숫자를 입력해주세요 > "))
num_neg = num * -1
print(num_neg)

# 문제 6
num = int(input("첫 번째 숫자를 입력해주세요 > "))
num2 = int(input("두 번째 숫자를 입력해주세요 > "))
print("더하기 연산 : " + str(num + num2))
print("곱하기 연산 : " + str(num * num2))
print("몫 연산 : " + str(num // num2))
print("나머지 연산 : " + str(num % num2))

# 문제 7
num1 = int(input("첫 번째 숫자를 입력해주세요 > "))
num2 = int(input("두 번째 숫자를 입력해주세요 > "))
num3 = int(input("세 번째 숫자를 입력해주세요 > "))
print(num2)

# 문제 
num1 = int(input("첫 번째 숫자를 입력해주세요 > "))
num2 = int(input("두 번째 숫자를 입력해주세요 > "))
num3 = int(input("세 번째 숫자를 입력해주세요 > "))
num4 = int(input("네 번째 숫자를 입력해주세요 > "))
num5 = int(input("다섯 번째 숫자를 입력해주세요 > "))
print(list(num1,num2,num3,num4,num5))

# 문제 9
str = str(input("문자열을 입력해주세요 > "))
int = int(input("숫자를 입력해 주세요 > "))
print(str*int)

# 문제 10
num1 = int(input("첫 번째 숫자를 입력해주세요 > "))
print(num1)
num2 = int(input("두 번째 숫자를 입력해주세요 > "))
print(num1 + num2)
num3 = int(input("세 번째 숫자를 입력해주세요 > "))
print(num1 + num2 + num3)
num4 = int(input("네 번째 숫자를 입력해주세요 > "))
print(num1 + num2 + num3 + num4)
num5 = int(input("다섯 번째 숫자를 입력해주세요 > "))
print(num1 + num2 + num3 + num4 + num5)