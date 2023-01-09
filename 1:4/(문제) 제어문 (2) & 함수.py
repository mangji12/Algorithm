# 문제 1
'''
정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.

#단, abs() 함수는 사용하지 마세요.

출력 예시 1
정수를 입력하세요 > 1 # 사용자 입력
1
출력 예시 2
정수를 입력하세요 > -1 # 사용자 입력
1
출력 예시 3
정수를 입력하세요 > 0 # 사용자 입력
0
'''

n = int(input('정수를 입력하세요 '))

if n < 0:
    n = n * -1

print(n)

#문제 2
'''
정수만 저장한 리스트가 주어집니다.

리스트 요소의 개수를 출력하세요.

단, len() 함수는 사용하지 마세요

입력 1
number_list = [1, 2, 3, 4, 5]
출력 예시 1
5
입력 2
number_list = []
출력 예시 2
0
'''
number_list = [1, 2, 3, 4, 5]
count = 0
for i in number_list:
    count += 1
    
print(count)

#문제 3
'''
정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수들의 합을 출력하세요.

단, sum() 함수는 사용하지 마세요.

입력 1
number_list = [1, 2, 3, 4, 5]
출력 예시 1
15
입력 2
number_list = [-1, -2, -3, -4, -5]
출력 예시 2
-15
'''
number_list = [1,2,3,4,5]
result = 0
for i in number_list:
    result += i
print(result)

#문제 4
'''
정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수들의 평균을 출력하세요.

단, len() / sum() 함수는 사용하지 마세요.

입력 1
number_list = [2, 4, 6]
출력 예시 1
4.0
입력 2
number_list = [2, 3, 5, 7]
출력 예시 2
4.25
'''
number_list = [1,2,3,4,5]
result = 0
count = 0
for i in number_list:
        result += i
        count += 1

print(count / result)

#문제 5
'''
정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수들의 곱을 출력하세요.

입력 1
number_list = [1, 2, 3, 4, 5]
출력 예시 1
120
입력 2
number_list = [-1, -2, 3]
출력 예시 2
6
'''
number_list = [1,2,3,4,5]
result = 1
for i in number_list:
    result *= i

print(result)

# 문제 6
'''
양의 정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수 중 가장 큰 값을 출력하세요.

단, max() 함수는 사용하지 마세요.

입력 1
number_list = [1, 2, 3, 4, 5]
출력 예시 1
5
입력 2
number_list = [1, 1, 1]
출력 예시 2
1
'''
number_list = [1,2,7,4,5]
max = 0
for num in number_list:
    if(max<num):
        max = num

print(max)

# 문제 7
'''
양의 정수만 저장한 리스트가 주어집니다.

리스트에 저장된 정수 중 가장 작은 값을 출력하세요.

단, min() 함수는 사용하지 마세요.

입력 1
number_list = [1, 2, 3, 4, 5]
출력 예시 1
1
입력 2
number_list = [5, 5, 5, 2]
출력 예시 2
2
'''

number_list = [1,2,7,3,5]
min = 9999
for num in number_list:
    if(num<min):
        min = num

print(min)
