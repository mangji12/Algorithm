score = int(input())
if score <= 100 and 90 <= score:
    print('A')
elif score < 90 and 80 <= score:
    print('B')
elif score < 80 and 70 <= score:
    print('C')
elif score < 70 and 60 <= score:
    print('D')
else:
    print('F')