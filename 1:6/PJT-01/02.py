with open('./PJT-01/data/fruits.txt','r') as t:
    fruits = t.read()

fruits = fruits.split('\n')
count = len(fruits)

index = open('02.txt','w')
index.write(str(count))
index.close()
