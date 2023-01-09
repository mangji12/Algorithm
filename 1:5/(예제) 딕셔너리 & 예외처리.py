'''
학습 목표
딕셔너리 활용 코드를 읽고, 출력 결과를 예측할 수 있다.
딕셔너리 순회 작동 방식을 이해하고, 순회 결과를 예측할 수 있다.
에러가 발생했을 때 에러의 원인을 설명할 수 있다.
진행 방법
코드 작성 후 코드를 읽고, 파일을 실행했을 때 출력되는 값을 예측해서 ? 대신 작성하세요.
'''

#예제 1
#선행 학습
#딕셔너리
#코드
dict_variable = {}
dict_variable["이름"] = "정우영"
dict_variable["생년월일"] = "19000101"
dict_variable["회사"] = "하이퍼그로스"

print(dict_variable["이름"]) # 정우영
print(dict_variable["생년월일"]) # 19000101
print(dict_variable["회사"]) # 하이퍼그로스

# 예제 2
# 선행 학습
# 딕셔너리
# 코드
dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"


print(dict_variable["a"]) # A
print(dict_variable["D"]) # d 
print(dict_variable["b"]) # 에러

# 예제 3
# 선행 학습
# 딕셔너리
# 코드
dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000
dict_variable["banana"] = dict_variable["banana"] + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # 6000

# 예제 4
# 선행 학습
# 딕셔너리
# 반복문
# 코드
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key in dict_variable:
    print(key, dict_variable[key])

"""
예측을 작성하세요. 
1 이름 정우영
2 생년월일 19000101 
3 회사 하이퍼그로스
# 반복문에서는 key값으로 받는다(반환).
"""

# 예제 5
# 선행 학습
# 딕셔너리
# 반복문
# 코드
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

for key, value in dict_variable.items():
    print(key, value)

"""
예측을 작성하세요.
1 이름 정우영
2 생년월일 19000101
3 회사 하이퍼그로스
"""

# 예제 6
# 선행 학습
# 딕셔너리
# 코드
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

print("나이" in dict_variable) # False

# 예제 7
# 선행 학습
# 딕셔너리
# 조건문
# 코드
dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

if "거주지" not in dict_variable:
    dict_variable["거주지"] = "서울특별시"
    # 위 조건문의 조건식이 무엇을 의미하는지 작성하세요.
    # dict_var에 거주지(key)가 포함되어있지 않으면 True를 반환. 
    # -> dict_var에 거주지(key)를 추가하고 value 값은 서울특별시로 지정.
    
print(dict_variable) # {'이름': '정우영', '생년월일': '19000101', '회사': '하이퍼그로스',\
'거주지': '서울특별시'}

# 예제 8
# 에러가 발생한 원인을 작성하세요.

# 선행 학습
# 리스트
# 예외처리
# 코드
list_variable = []

try:
    list_variable.append(0) # 0
    list_variable.append(1) # 1
    list_variable.append(2) # 2
    print(list_variable[3]) # -
    
except:
    print("에러가 발생했습니다.") 
    print("에러의 원인은 무엇인가요?")

"""
출력 결과를 예측해서 작성하세요.
3번째의 인덱스 값이 존재하지 않기 때문에 출력을 할 수 없다.
"""

# 예제 9
# 에러가 발생한 원인을 작성하세요.

# 코드
try:
    number = 1
    if number == 1
        print(number)
    
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
에러 원인
if 구문 끝에는 : 을 적어주어야 한다.
""" 
# 예제 10
# 선행 학습
# 리스트
# 조건문
# 코드
n = 10
total = 0

for number in range(0, n + 1):
    if number % 2 == 0: # 짝수?
        total += number * 2 # 짝수면 짝수 곱하기 2
    elif number % 2 == 1: # 홀수?
        total += number + 1 * 3 # 홀수면 3곱하기 1 하고 더하기

print(total) # 100