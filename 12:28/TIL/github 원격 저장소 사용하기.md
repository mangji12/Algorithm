# github 원격 저장소 사용하기

Git 무엇일까?

“Git은 버전을 관리한다”

**원격저장소 활용하기 (1)**

1. push
    - 로컬 저장소의 버전을 원격 저장소로 보낸다.
        
        `git push`
        

1. pull
    - 원격저장소의 버전을 로컬 저장소로 가져온다.
        
        `git pull`
        

## GitHub 기반 원격저장소 활용

**학습 목표**

- GitHub 원격저장소에 로컬 저장소를 올려 관리할 수 있다.
- 원격 저장소 활용 명령어를 이해하고 설명할 수 있다.

1. 초기 원격 저장소 설정하기
    
    예를 들어 git push를 해봤자 push를 할 목적이 없다고 에러 메세지를 띄운다.
    
    1) New Repository
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/10fa7ed9-04a1-41a1-b376-16e90b316f38/Untitled.png)
    

2) 저장소 설정하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32f324de-2428-47e5-9bb8-543c85ac9076/Untitled.png)

3) URL 확인

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b579655e-09b2-4120-8cdd-13adc185f7a9/Untitled.png)

- url에서 패턴을 확인할 수 있다.

4) 로컬 저장소에 원격 저장소 정보 설정하기

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ad0c8fc-81f7-4a6e-9ca9-bb70a8162dec/Untitled.png)

- `git remote add origin https://github.com/kdt-live/test.git`
- origin은 원격 저장소의 이름을 지정하는 부분이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/891fe546-029b-4f4f-83de-fddf40c4dbb0/Untitled.png)

git bash에 붙여넣기.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/987f230c-39ec-4a68-ab27-abe266bd6c30/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/77599031-2da3-435a-876e-933c00c881e9/Untitled.png)

— 한번 하면 할 필요 없음 — (계속 저장돼 있으면)

5) 원격 저장소의 정보를 확인

설정이 되었는지 확인

`git remote -v`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5f6c3603-3095-4eac-8c50-b2aefc7288ab/Untitled.png)

이름의 글로벌 룰 : origin → 원격저장소 기본 이름 많이 쓰는 것 ⇒ like master

`git push <원격저장소이름> <브랜치 이름>`

- 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push)
    - 원격 저장소는 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)을 관리하는 것
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1b4c0b7-07a8-4008-80be-f1b8931dc2ed/Untitled.png)
    
    이 후 로그인 창이 뜨면 확인.
    
    **push 주의사항**
    
    - push할 때는 인증 정보가 필수적
    - 윈도우는 아래의 화면에서 인증을 하여야 한다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1ef3fb9f-549e-4500-a6ff-29be15530e9d/Untitled.png)
        
    - mac 유저
        
        github 설정에 접속 후 값을 가져온다.(token값)
        
        **push 확인**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8212873a-e9bf-4873-abdf-27c61b40de3e/Untitled.png)
        
    

**로컬 저장소의 버전을 원격 저장소로 Pull하기**

- 하다보면 하는 얘기들…
    - GitHub에 파일을 추가하고 싶어요
    - 파일 잘못 올라갔는데 삭제하고 싶어요
    - Github에 올리고 로컬에서 파일을 지우면 사라지나요?
        
        ⇒ 세모에 가까움. → 사라지는 않는다. 삭제 상태를 add,commit 버전으로 기록하면 다음 번에 push 하면서 가져오도록 한다.
        
- 결국엔 깃허브에는 최신 버전의 상태를 보여줄 뿐이다.

`pull`이 아닌 가져오는 행위를 `clone` 을 사용하여 가져온다.

clone을 하여 가져왔을 때 zip 파일과 다른 것은 git이 생기면서 다른 모든 버전 까지 가져오게 된다.

→ 해 온것을 이어서 진행할 때 clone 사용!

**작업의 매커니즘**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fbadcd13-a79c-4703-943f-a2671b1cba91/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ece34af-c835-47e5-a6ee-4f2c01ced0f7/Untitled.png)

해당 작업에서 `push` **는 권한이 없기 때문에 동작이 안된다.**

로컬에서 새로운 프로젝트의 시작

`git init`

원격에 있는 프로젝트 시작?

`git clone`

git clone을 했는데 git init을 할 필요가 없다.

명령어 정리

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/35571097-e730-4890-85ac-577308250d9e/Untitled.png)

# **git 특정버전으로 소스 받기, git pull version**

[git & bitbucket](https://lowell-dev.tistory.com/category/git%20%26%20bitbucket) 2021. 2. 18. 09:28

- **git log로 버전명 보기**

```bash
$ git log --abbrev-commit --pretty=oneline
```

상황 : git을 사용하는 중에 특정 버전까지만 운영에 반영해야하는 상황이라서

특정 버전까지의 소스를 pull 받았다.

방법

$ git checkout {version}

여기서 version은 commit version이다

![https://blog.kakaocdn.net/dn/NLiE1/btqXMezOK5F/HIYskGTWayrb8UHTaeUP80/img.png](https://blog.kakaocdn.net/dn/NLiE1/btqXMezOK5F/HIYskGTWayrb8UHTaeUP80/img.png)

최신으로 돌아오기

$ git checkout HEAD

또는

$ git checkout dev (브런치명)

실습

- 자기소개 프로젝트
- TIL 프로젝트

실습 하기전에…

github 에서 편집행위를 하면 결국엔 commit - 버전이 바뀌게 된다.

협업할 때

PR(pull request) 업무 흐름을 제어하도록 해야 한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3944231-a6ae-4977-8390-298a2c455ebc/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36e56653-9a82-4762-bf04-443dac2d2698/Untitled.png)

해결 방법

1. 원격 저장소의 커밋을 원격저장소로 가져와서(pull)
2. 로컬에서 두 커밋을 병합(추가 커밋 발생)
3. 다시 깃허브로 push

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a01152cf-ae9e-437f-b171-697cfaaa3137/Untitled.png)

**gitigonre**

버전관리랑 상관 없는 파일?

secret.csv같은 커밋 시키면 안되는 파일을 .gitignore 파일에 secret.csv 파일을 작성해 놓으면 무시가 된다.

또 다른 사용법은 무시할 “폴더”를 지정할 수도 있다.

이미 커밋한 경우는?

→ 무시 안함. → 미리 설정하도록 하자. 지웠다가 하면 삭제됐다는 커밋 존재.

commit history : 커밋 역사 

**.gitignore 옵션**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b8dd3c2e-5dbb-4681-8e04-0b7f25ff5779/Untitled.png)

자동으로 목록 만들어 주는 사이트