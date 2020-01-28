# Git Pull Request 

> Atlassian.com 이 발표한 ‘Getting Git Right’ Tutorial 중 `Forking Workflow`를 본 경험이 있다. Collaborator를 통해 모두가 Push&Pull 권한을 갖지 않고 있다면, Repository를 `Fork` 방식으로 퍼와서 내 공간에서 작업하고, 오리지널 브랜치에 `Pull Request` 요청을 할 수 있다.



## Pull Request

> Github에서 branch를 merge 해보라고 요청하는 기능이다. 프로젝트 협업 도구 중 핵심 기능 중 하나이다.



**(1) 내가 `Fork`할 오리지널 저장소에서 , 나의 Repository로 Fork 해온다.**

![Forking00](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Forking00.jpg?raw=true)

**(2) 내 컴퓨터(로컬 저장소)로 `Clone` 한다.**

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_01.JPG?raw=true" alt="01" style="zoom:80%;" />

```shell
# 내 컴퓨터(로컬 저장소에 Fork된 내 저장소를 Clone)
$git clone [Clone with HTTPS]

# Clone 한 장소로 이동
$git cd [브랜치 명]

# 오리지널 저장소를 upstream으로 저장
$git remote add upstream [Fork했던 오리지널 저장소의 주소]
```



**(4) 개발용 브랜치를 추가 생성**

```shell
# 'develop' 이라는 저장소를 추가로 생성했다.
$ git checkout -b [develop]
```

> 일반적으로 fork된 저장소에서는 master branch에서 개발하지 않는다.



**(5) Pull Request로 코드 리뷰 진행**

![](C:\Users\student\Desktop\00.jpg)

**(6) PR 요청이 받아들여지면 Merge 진행**

```shell
# 내 저장소의 'upstream'에서 pull 요청으로 당겨 받으며 최신화 해야 마무리.
$git pull upstream develop
```