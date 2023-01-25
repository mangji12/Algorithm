import sys
N,X = sys.stdin.readline().split()
N = int(N)
X = int(X)
s = list(map(int,sys.stdin.readline().split()))
for i in s:
    if i < X:
        print(i,end = ' ')