# 2576
syn = []

for i in range(7):
    num = int(input())
    if num % 2 == 1:
        syn.append(num)
    
if len(syn) == 0:
    print(-1)
else:
    print(sum(syn))
    print(min(syn))