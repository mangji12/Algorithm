with open('./PJT-01/data/fruits.txt') as f:
    fruits = f.read().split('\n')

count = 0
result = []
for i in fruits:
    if 'berry' in i:
        count += 1
        result.append(i)

with open('03.txt','w') as c:
    c.write(str(count))
    c.write(str(result))
