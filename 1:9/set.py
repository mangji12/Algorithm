my_list = ['서울', '서울', '대전', '광주',
            '서울', '대전','부산','부산']

li = []

for i in my_list:
    if my_list not in li:
        li.append(i)

print(li)