# 문제 1
# 정수 한 개를 입력 받고, 해당 숫자가 0보다 큰 숫자라면 True 아니면 False를 출력하세요.

n = int(input("정수를 입력하세요 > "))
if n > 0:
    print(True)
else:
    print(False)

# 문제 2
# 정수 두 개를 입력 받고, 크기가 더 큰 정수를 출력하세요.
# 두 정수가 같으면 False를 출력하세요.

n1 = int(input("첫번째 정수를 입력하세요 > "))
n2 = int(input("두번째 정수를 입력하세요 > "))

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(False)

# 문제 3
# 정수 한 개를 입력 받고, 해당 정수가 1 보다 크고, 10보다 작다면 True 아니면 False를 출력하세요.
n = int(input("정수를 입력하세요 > "))
if n > 1:
    if n < 10:
        print(True)
else:
    print(False)

# 문제 4
# 정수 한 개를 입력 받고 0 보다 크고, 짝수라면 True 아니면 False를 출력하세요.
n = int(input("정수를 입력하세요 > "))
if n > 0:
    if n % 2:
        result = True
else:
    result = False
print(n)

# 문제 5
# 정수 한 개를 입력 받고, 아래 조건에 따라 출력하세요.
'''
값이 100 초과 / 0 미만이면 "에러" 출력
값이 60 이상이면 "합격" 출력
값이 60 미만이면 "불합격" 출력
'''

n = int(input("정수를 입력하세요 > "))
if n < 60:
    result = '불합격'
elif n >= 60:
    result = '합격'
    if n > 100:
        result = '에러'
else:
    result = '에러'
print(result)

# 문제 6
# 문자열을 입력 받고, 입력 받은 문자열을 반대로 한 글자씩 출력하세요.
char = input("문자열을 입력하세요 > ")

for i in char[::-1]:
    print(i)

# 문제 7 
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 오름차순으로 출력하세요.
# 두 값이 같으면 False를 출력하세요
n1 = int(input("첫 번째 정수를 입력하세요 > "))
n2 = int(input("두 번째 정수를 입력하세요 > "))

for i in range(n1,n2):
    print(i)
    if n1 == n2:
        print('False')

# 문제 8
# 정수 두 개를 입력 받고, 두 수 사이의 정수를 내림차순으로 한 줄에 모두 출력하세요.
# 두 값이 같으면 False를 출력
n1 = int(input("첫 번째 정수를 입력하세요 > "))
n2 = int(input("두 번째 정수를 입력하세요 > "))
result = sorted(range(n1,n2),reverse=True)

for i in result:
    print(i)
    if n1 == n2:
        print('False')

# 문제 9
# 정수 한 개를 입력 받고, 1 부터 입력 값 사이의 정수 중 홀수만 출력하세요.
# 입력 값이 1보다 작으면 False를 출력하세요.
n = int(input("정수를 입력하세요 > "))

for i in range(1,n):
    odd = i
    if i == n % 2:
        print(i)
    else:
        break
print(False)

# 문제 10
# 구구단을 출력하세요.
for i in range(1,10):
    for n in range(1,10):
        print('{0} X {1} = {2}'.format(i,n,i*n))