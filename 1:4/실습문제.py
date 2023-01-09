target_number = 10
n = 0
result = 0

while n <= target_number:
	result += n
	n+=1
print(result)

for i in range(1,n):
    result += i
    print(result)

# map 함수 
# 첫번째 인자로 함수를 받아서
# 두번째 인자인 반복 가능한 객체의 모든 요소에 적용
numbesrs = ['1','2','3']
new_new_numbers = map(int,numbers)
print(new_new_numbers)