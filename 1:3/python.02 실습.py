numeric = ("첫","두","세","네","다섯")

result = 0
n1 = int(input ('첫 번째 정수형 숫자를 입력해주세요 >'))
result += n1
print(result)
n2 = int (input('두 번째 정수형 숫자를 입력해주세요 > '))
result += n2
print(result)
n3 = int(input ('세 번째 정수형 숫자를 입력해주세요 > '))
result += n3
print(result)
n3 = int(input ('세 번째 정수형 숫자를 입력해주세요 > 1'))
result += n4
print(result)
ns = int(input('다섯 번째 정수형 숫자를 입력해주세요 > '))
result += n5
print(result)

for i in range(1,6):
    result += int(input(f"{i} 번째 정수형 숫자를 입력해주세요"))
    print(result)

# 예제
a = -10
if a >= 0:
    print('양수')
else:
    print('음수')
print(a)

# 실습문제
# 조건문을 통해 변수 num의 값의 홀수 짝수 여부를 출력,
num = int(input('값을 입력하세요 : '))
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
print(num)

# 복수 조건문 : 실습 문제
# 다음은 미세먼지 농도에 따른 등급일 때, dust 값에 따라 등급을 출력하는 조건식을 작성

dust = 0
if dust <= 30:
    print('좋음')
elif dust <= 80:
    print('보통')
elif dust <= 150:
    print('나쁨')
else:
    print('매우나쁨')

# for문
for num in range(3):
    print(num**2)

word = 'apple'
for i in word:
    if i == 'a':
        print('a 입니다')