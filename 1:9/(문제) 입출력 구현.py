# #문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.

#만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

# 단, index() / find() 메서드는 사용하지마세요.
index = {}
char = 'hEllo hypergrowth'# input('문자열을 입력하세요 > ')
for i, ch in enumerate(char): # 인덱스 값 받기
    if ch == 'e': # 반복되는 char의 문자가 e와 같으면
        index[ch] = i # index 딕셔너리의 ch 키값에 i(입력받은 문자열속 e의 인덱스값)
        print(index[ch]) # 딕셔너리에 저장된 e의 위치 출력

# e가 없으면 -1출력 아직  못만듬
    elif char != 'e':
        break
    print(-1)



'''
출력 예시 1
문자열을 입력하세요 > hello # 사용자 입력
1
출력 예시 2
문자열을 입력하세요 > hEllo hypergrowth # 사용자 입력
9
# 출력 예시 3
문자열을 입력하세요 > java # 사용자 입력
-1
'''

'''
문제 2
문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

단, count() 메서드는 사용하지마세요.

출력 예시 1
문자열을 입력하세요 > hello # 사용자 입력
hello 1
출력 예시 2
문자열을 입력하세요 > hello hypergrowth # 사용자 입력
hello 1
hypergrowth 1
출력 예시 3
문자열을 입력하세요 > apple apple banana grape # 사용자 입력
apple 2
banana 1
grape 1


'''
char = input('문자열을 입력하세요 > ')
cnt = 0
ov_dict = {}
for charac in char.split(' '): # 첫 문장 반복
    for ov in char.split(' '): # 첫 문장의 반복 안에서 반복(비교위함)
        if ov == charac:
            ov_dict.update({f'{charac}' : cnt + 1}) # 반복된 값을 key로 추가시키면서 카운트 +1 추가
            pass # char가 끝날때 까지 반복

print(ov_dict)

'''
문제 3
문자열을 입력받고, e 를 제거한 결과를 출력하세요.

단, replace() 메서드는 사용하지 마세요.

출력 예시 1
문자열을 입력하세요 > apple # 사용자 입력
appl
출력 예시 2
문자열을 입력하세요 > hello # 사용자 입력
hllo
출력 예시 3
문자열을 입력하세요 > hEllo # 사용자 입력
hEllo
'''

char = input('문자열을 입력하세요 > ')
det = char.split('e')
print(''.join(det))


'''
문제 4
문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한 알파벳의 개수를 출력하세요.

단, count() 메서드는 사용하지마세요.

출력 예시 1
문자열을 입력하세요 > apple p # 사용자 입력
2
출력 예시 2
문자열을 입력하세요 > hello o # 사용자 입력
1
출력 예시 3
문자열을 입력하세요 > hEllo a # 사용자 입력
0
'''

str, char = input('문자열을 두개 입력하세요 > ').split() # 입력받은 값을 공백 기준으로 분리
count = 0
for i in char:
    if i == str:
        count += 1

print(str, char,end= ' ')
print(count)

# att = char.split('e')

'''
문제 5
양의 정수 3개를 입력받고, 3개의 양수를 - 로 연결해서 출력하세요.

단, join() 메서드는 사용하지마세요.

출력 예시
문자열을 입력하세요 > 010 1234 5678 # 사용자 입력
010-1234-5678
'''

pos = input('양수 세개를 입력하세요 > ').split()
attach = '-'.join(map(str, pos))

print(attach)

'''
문제 6
양의 정수를 입력받고, 자리수의 합을 출력하세요.

만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.

단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

출력 예시 1
양의 정수를 입력하세요 > 244 # 사용자 입력
10
출력 예시 2
양의 정수를 입력하세요 > 1 # 사용자 입력
1
출력 예시 3
양의 정수를 입력하세요 > -10 # 사용자 입력
-1
'''

pos = input('양수를 입력하세요 > ').split()
if pos < 0:
    print('-1')

p = ' '.join(pos)
s = []
for i in p:
    s.append(i)