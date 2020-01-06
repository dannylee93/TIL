# 마크다운(Markdown)

> 일반 텍스트 형식 구문을 사용하는 마크업 언어의 일종으로 사용법이 쉽고 간결하여 빠르게 문서 정리를 할  수 있습니다. 단, 모든 HTML 마크업을 대체하지는 않습니다.



## 1. 문법

### 1.1 Header

>  헤더는 제목을 표현할 때 사용합니다. 단순히 글자의 크기를 표현하는 것이 아닌 의미론적인 중요도를 나타냅니다.

- `<h1>` 부터 `<h6>`까지 표현 가능합니다.
- `#` 의 개수로 표현하거나 `<h1>``<h1>`의 형태로 표현 가능합니다.



# h1 태그입니다.

## h2 태그입니다.

### h3 태그입니다.

#### h4 태그입니다.

##### h5 태그입니다.

###### h6 태그입니다.



### 1.2 List

> 목록을 나열할 때 사용합니다. 순서가 필요한 항목과 그렇지 않은 항목으로 구분할 수 있습니다. 순서가 있는 항목 아래 순서가 없는 항목을 지정할 수 있으며 그 반대로 가능합니다.

- 순서가 없는 목록
  * `1.`을 누르고 스페이스바를 누르면 생성할 수 있습니다.
  * `tab`키를 눌러서 하위 항목을 생성할 수 있고 `shift + tab`키를 눌러서 상위 항목으로 이동 할 수 있습니다.
- 순서가 있는 목록
  * `-`(하이픈)을 쓰고 스페이스바를 누르면 생성할 수 있습니다.
  * `tab` 키를 눌러서 하위항목을 생성할 수 있고 `shift + tab`키를 눌러서 상위 항목으로 이동 할 수 있습니다.



1. 순서가 있는 항목

2. 순서가 있는 항목

   1. 순서가 있는 하위 항목1

   2. 순서가 있는 하위 항목2

      

- 순서가 없는 항목
- 순서가 없는 항목
  - 순서가 없는 하위 항목1
  - 순서가 없는 하위 항목2



### 1.3 Code Block

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼 때 사용합니다. 인라인과 블럭 단위로 구분할 수 있습니다. 

- Inline
  - 인라인 블럭으로 처리하고 싶은 부분을 `(백틱)으로 감싸줍니다.
- Block
  - `(백틱)을 3번 입력하고 `` Enter`` 를 눌러 생성합니다.



`add`한 요소를 remote 저장소에 올리려면 `$ git push origin master`를 터미널에 입력합니다.

```python
$ git add .
$ git commit -m "first commit"
$ git push origin master
```



### 1.4 Image

> 로컬에 있는 이미지를 삽입하거나 이미지 링크를 활용하여 이미지를 나타낼 때 사용합니다.

- `![]()` 을 작성하고 `()` 안에 이미지 주소를 입력합니다. `[]`안에는 이미지 파일의 이름을 작성합니다.
- 로컬에 이미 파일을 저장한 경우 절대 경로가 아닌 상대 경로를 사용하여 이미지를 저장합니다.

<img src="data:image/png;base64,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" style="zoom:150%;" />



### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.

- `[]()` 을 작성하고 `()` 안에 링크 주소를 작성하고 `[]`안에 어떤 링크 주소인지 작성합니다.



​	[git 공식문서]()
​	[github 공식문서]()



### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

- `|`(파이프) 사이에 컬럼을 작성하고 `enter`를 입력합니다.
- 마지막 컬럼을 작성하고 뒤에 `|` 를 붙여줍니다.



| working directory | statging area | remoe repo |
| ----------------- | ------------- | ---------- |
| working tree      | index         | history    |
| working copy      | cache         | tree       |



### 1.7 기타

##### 인용문

- `>`을 입력하고 `enter`키를 누릅니다.

  > git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다.

- 인용문 안에 인용물을 작성하면 중첩해서 사용할 수 있습니다.

> $ git add.
>
> > $ git commit -m "first comit"
> >
> > > $ git push origin master



##### 수평선

- `---` , `***` , `___`을 입력하여 작성합니다.

Working Directory

___

Staging Area

___

Remote Repository

___



##### 강조

- 이탤릭체는 해당 부분을 `*`혹은 `_`(언더바) 로 감싸줍니다.
- 보드체는 해당 부분을 `**`혹은 `__`(언더바 2개) 로 감싸줍니다.
- 취소선은 `~~`표시를 사용합니다.

이것은 *이탤릭체*입니다.

이것은 **보드체**입니다.

이것은 ~~취소선~~입니다.





## 2. 과제

> 현재의 pdf 문서를 마크다운 문법을 활용하여 `00_markdown_basic.md`로 만들어 보세요.