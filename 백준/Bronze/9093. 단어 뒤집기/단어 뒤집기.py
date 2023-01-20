T = int(input())
for i in range(T):
    string = input().split()
    for i in string:
        print(i[::-1],end = ' ')