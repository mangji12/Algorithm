with open('./PJT-01/data/fruits.txt','r') as f:
    with open('04.txt','w') as n:
        for n in f:
            n.write(n+'\n')

with open('./PJT-01/data/fruits.txt','w') as n:
    n.write()
    for name in f:
            f.write(name+'\n')

name_fruits = str()
count_fruits = int(0)

for i in fruits:
    for a in fruits:
        if len(i) == len(a):
            count_fruits += 1
            name_fruits = i
            print(count_fruits)
        with open('04.txt','w') as o:
            o.write(f'{name_fruits} {count_fruits}')

with open('04.txt','w') as n:
    for name in f:
        f.write(name+'\n')