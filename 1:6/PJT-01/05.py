import json

# 아래 코드 수정 금지
movie_json = open("./PJT-01/data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
key = movie.items()
with open('05.txt','w')as m:
    print(m)
    for i in m:
        m.write(i + '\n')