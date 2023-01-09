# 예제1
a = 1
b = 1
print(a < b) # 0
# 불련 값으로 결과가 나옴

# 예제2
a = bool("")
b = False
print(a == b) # True
# 불련값 아무것도 없음(a -> 0) b는 False 이기 때문

# 예제3
a = 1
result = ""

if a == 1:
    result = True
else:
    result = False
    
print(result) # True
# a -> True result -> 0, a가 조건이 맞기 때문에 result에 True 값 저장되고 나서 탈출.

# 예제4
a = 90 

if a == 90:
    a = a + 10
    
elif a == 100:
    a = a + 10
    
elif a == 110:
    a = a + 10

else:
    a = a + 10

a = a + 10
    
print(a) # 110
# a는 90부터 시작. 첫번째 -> 실행 a -> 100됨 탈출. 100(a) + 10 -> 110

# 예제5
string = "hello world!"

for element in string:
    print(element)
    
"""
예측을 작성하세요.
h
e
l
l
o

w
o
r
l
d
!
"""
# 반복문에 의해 element는 string의 값이 반복되어 저장됨. -> 줄바꿈

# 예제6
list_variable = [0, 1, 2, 3, 4, 5, 6]

for element in list_variable:
    print(element, end=" ")

"""
예측을 작성하세요.
0 1 2 3 4 5 6
"""
# element에 list_var이 저장됨. 하지만 end옵션 -> " "를 설정 했으므로 줄바꿈X

# 예제7
n = 10

for element in range(-n, n):
    print(element, end=" ")
    
"""
예측을 작성하세요.
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
"""
# element에 range(-10,10), 스텝 설정을 안했기 때문에 +1임

# 예제8
n = 10

for element in range(1, n + 1, 3):
    print(element, end=" ")
    
"""
예측을 작성하세요.
1 4 7 10
"""
# element에 1부터 10까지 3계단씩. -> 1 4 7 10

# 예제9
list_variable = [6, 5, 4, 3, 2, 1, 0] 

# enumerate가 무엇인지 검색해보세요!
for index, element in enumerate(list_variable):
    print(index, element)

"""
예측을 작성하세요.
0 6
1 5
2 4
3 3
4 2
5 1 
6 0
"""
# enumerate : 인덱스(순서)와 원소를 동시에 접근하면서 루프를 동시에 돌릴 수 있다.
# index와 element 둘 다에 enumerate 함수가 저장을 시켜준다. 예를 들어 첫번 째 루프에는 list_vard의 1 원소는 인덱스 1 값을 가진다.
# 튜플 값이 아닌 리스트 형식을 원한다면 두 개를 선언하도록 한다.
# 순서대로 출력이 된다.(sort)

# 예제10
n = 10

for element in range(n, -n, -1):
    print(element, end=" ")
    if n < 0:
        break
"""
예측을 작성하세요.
10 9 8 7 6 5 4 3 2 1 
"""
# 10부터 시작 -1 깎임, n이 0보다 작다면 루프는 종료.

# 예제11
list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

for element in list_variable:
    if element < 0:
        continue
    
    print(element, end=" ")
    
"""
예측을 작성하세요.
3 5 1 9 21
"""
# element 안에 list_var 저장. continue 으로 인해 0보다 작으면 스킵.

# 예제12
N = 3
M = 4

for n in range(N): # 0 1 2
    for m in range(M): # 0 1 2 3
        print(f"{n}, {m}") 
"""
예측을 작성하세요.
0, 0
0, 1
0, 2
1, 0
0, 1
.
.
.
"""