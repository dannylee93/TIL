# Git ignore

> Github에 파일을 커밋하다보면 백업 파일등의 다른 파일들이 생성되어 같이 커밋 되는 경우가 있다. 여기에서는 나처럼 git ignore라는 방법을 모르고, 이미 로그 파일 까지 커밋한 상태에서 Gitignore를 적용하는 방법에 대해 정리 했다.



*Gitignore는 어떤 파일들을 커밋할 때 내가 원하지 않는 파일은 무시하고 올릴 수 있도록 도와주는 파일이다.*



## Create [.gitignore]

**(1) <gitignore.io> 라는 사이트에 접속하고, 본인의 환경을 중앙의 검색창에 입력한다.**

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Gitignore01.JPG?raw=true" style="zoom:80%;" />

**(2) `.gitignore`에 넣을 추천 리스트들을 자동으로 생성해준다.**

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Gitignore02.JPG?raw=true" style="zoom:80%;" />

**(3) 그대로 복사해서 본인 IDE 환경에서 `.gitignore` 파일을 생성한다.**

![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Gitignore03.JPG?raw=true)

> Visual Studio Code 에서 `.gitignore`파일을 생성했다.



**(4) 원하는 본인 로컬 저장소 위치로 복사해서 넣어준다.**



**(5) 이미 로그파일들이 커밋 되어 있는 상태에서는 `.gitignore` 파일을 뒤늦게 커밋해도 없어지지 않는 것을 볼 수 있다.**

![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Gitignore04.JPG?raw=true)

**(6)  `5번 순서` 와 같은 문제점이 있을 때, `Git Bash` 에서 직접 명령어를 사용하여 정상적으로 작동 시킨다.**

```shell
# 현재 Repository의 cache를 모두 삭제
git rm -r --cached .

# .gitignore에 넣은 파일 목록들을 제외하고 다른 모든 파일을 다시 track하도록 설정
git add .

# commit 하기
git commit -m "fixed untracked files"

# 최종단계인 Push 로 마무리 하기
git push origin <branch 명>
```

> Git Bash에 사용할 명령어 순서이다.  마지막 `.` 까지 놓치지 말고 입력하자.



![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Gitignore05.JPG?raw=true)

> 먼저 내가 원하는 위치의 로컬 저장소로 이동한다.



![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Gitignore06.JPG?raw=true)

> 상단의 명령어 예시대로 Git Bash에 입력한다.



**(7)  최종적으로  `Push`  명령어 까지 입력하면 아래 이미지와 같이 적용되어 로그파일이  없어진 것을 확인할 수 있다.**

![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Gitignore07.JPG?raw=true)