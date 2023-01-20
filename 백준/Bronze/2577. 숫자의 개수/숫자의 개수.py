A,B,C = int(input()),int(input()),int(input())
result = list(str(A * B * C))
for i in range(10):
    print(result.count(str(i)))