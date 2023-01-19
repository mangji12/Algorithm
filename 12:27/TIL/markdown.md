# 마크다운 문법 정리
## **마크다운이란?**  


- >2004년 존 그루버가 만든 텍스트 기반의 가벼운 마크업 언어
- >최초 마크다운에 비해 확장된 문법(표 주석 등)이 있지만 본 수업에서는 깃허브에서 사용 가능한 문법을 기준으로 설명  
#

## **마크다운 특징**  


- >워드 프로세서는 다양한 서식과 구조를 지원하지만, 다른 프로그램으로 호환에 제약이 되며 워드프로세스 상의 기능을 활용해야 함
- >마크다운은 최소한의 문법으로 구성되어 있으며 순수 텍스트로 작성 가능  
#

## **마크다운 활용 예시**
- README.md
    - >오픈소스의 공식 문서를 작성하거나 개인 프로젝트의 프로젝트 소개서로 활용
    - >혹은 모든 페이지에 README.md를 넣어 문서를 바로 볼 수 있도록 활용  
#
## **정적 사이트 생성기 기반 블로그**  


- >Jekyll,Gatsby,Hugo,Hexo 등으로 작성된 마크다운을 HTML,CSS,JS 파일 등으로 변환하고, Github pages 기능을 통해 무료 호스팅이 가능함  
#

## **마크다운 기반 SW**  


- >Jupyter notebook에는 별도의 마크다운 셀으로 프로젝트 내용과 분석 결과를 정리 가능함
- >Notion과 같은 메모/노트 필기 SW 역시 마크다운 기반 문서 작성을 기본으로 함  
#
&nbsp;
## **마크다운 문법**

#
### *Heading : 문서의 제목이나 소제목*

- >#의 개수에 따라 대응되는 수준이 있으며 h1 ~ h6까지 표현 가능
- >문서의 구조를 위해 작성되며 글자 크기를 조절하기 위해 사용되어서는 안됨.

 *주의할 점*
- >띄어쓰기, 오타 잘 확인하기
&nbsp;

*예시*

```
# h1
## h2
### h3
#### h4
##### h5
###### h6
```  
#

### *List : 목록*

- >순서가 있는 리스트(ol)와 순서가 없는 리스트(ul)로 구성
&nbsp;

*예시*

```
1.
2. 
3. 
- 햄버거
    - 치즈 2장  
    - 패티 2장
    - 양상추
- 음료
1. 펩시 제로 콜라
2. 코카콜라 재료
```
- >Tab으로 하위 항목으로 구성할 수 있음  
#
### *Fenced Code block : 코드 블록*
- >코드 블록은 backtick 기호 3개를 활용하여 작성(\``` ```)
- >코드 블록에 특정 언어를 명시하면 Syntax Highlighting 적용 가능
&nbsp;

*예시*

```
'''python
print('hello')
# 주석
'''
```  
#

### *Inline Code block : 코드 블록*
- >코드 블록은 backtick 기호 1개를 인라인에 활용하여 작성(\` `)
&nbsp;

*예시*

```
마크다운은 `마크업 언어` 입니다.
```  
#

### *link : 링크*
- >\[문자열](url)을 통해 링크 작성 가능
&nbsp;

*예시*

    - [구글](google.com)
    - [a 파일](a.md)
    - [b 폴더](b\a.txt)
    - [a 파일](./a.md) 상위 폴더 표현은 ( ./ )  
#

### *image : 이미지*
- >\![문자열]\(url)을 통해 이미지를 사용 가능
- >특정 파일들 포함하여 연결 시킬 수도 있음
&nbsp;

*예시*

    -  1.png를 보여주는 문법
        ![보노보노](1.png)
    -  2.png를 보여주는 문법
        ![보노보노2](./b/2.png) (b로 옮긴 후)
#
### *Blockquotes : 인용*

- \>으로 인용문을 작성
&nbsp;

*예시*

        >중요한 것은 꺾이지 않는 마음  
#

### *테이블*
&nbsp;

*예시*

``` 
| Syntax  | Description|
| ------  | -----------|
| Header  | Title      |
|Paragraph| Text       |
```
- 위 처럼 입력하면 된다.
- 지원되지 않는 곳도 있다.
일일이 쳐야하는 번거로움이 있기 때문에 구글에 마크다운 활용을 검색해 사용해 볼 수 있다.  
#
### *텍스트 강조*
- 굵게,기울임을 통해 특정 글자들을 강조.
&nbsp;

*예시*

```
**안녕**
__안녕__
*안녕*
_안녕_
```  
#
### *수평선*

- 3개 이상의 (***), (-),(___)
&nbsp;

*예시*

```
---
- - -
***
* * *
___
_ _ _
```  
#

### *띄어쓰기*

- &nbsp:
#

### *외부 링크*

[Markdown Guide](https://www.markdownguide.org/)

[markdown 문법](https://sirupe.github.io/first-posting/)