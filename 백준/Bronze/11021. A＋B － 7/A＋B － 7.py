T = int(input())
# a,b = 3, 5 #map(int,input().split())
#b = int(input())
for i in range(1,T+1):
    a,b = map(int,input().split())
    s = a + b
    print(f'Case #{i}: {s}')