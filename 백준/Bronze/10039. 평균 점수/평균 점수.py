score = 0

for i in range(5):
    s = int(input())
    if s < 40:
        s = 40
    
    score += s

print(int(score / 5))