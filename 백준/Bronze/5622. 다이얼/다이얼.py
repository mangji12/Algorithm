d = {"ABC":3,"DEF":4,"GHI":5,"JKL":6,"MNO":7,"PQRS":8,"TUV":9,"WXYZ":10}
cnt=0
num =input()
for n in num:
    for j in d.keys():
        if str(n) in j:
            cnt +=d.get(j)
print(cnt)