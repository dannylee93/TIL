# Start Project using Github 01

> Github의 협업 시스템을 활용해서 효율적으로 프로젝트를 진행할 수 있다. 이 파일은 프로젝트 과정 중에서도 처음 환경 세팅에 대해 정리하는 파일이다.



#### **Contributor vs Collaborator ?**

- 뜻을 그대로 해석하면 기부자와 협력자. `Contributor`는 프로젝트의 관리자는 아니지만 한 프로젝트에
**커밋하고 있는 모든 사람** 지칭
- `Contributor`이라면, 
`Push` 권한은 프로젝트 관리자와 `Collaborator`만이 가지고 있으므로, `Fork`하여 프로젝트를 통째로 복사해온다.
- `Fork`해온 프로젝트에서 `Push`하고 관리한다음, 원래 오리지날 저장소로 `Push`한 내용들 보낼 수 있는데,` Pull request` 통해서 한다.
- `Collaborator`는 프로젝트의 공동 책임자이다. 즉, GitHub의 **push, pull 권한을 모두 가지고 있는 사람**을 뜻한다. 
`Contributor`는 `Pull Request`를 통해 누구나 시도할 수 있지만,`Collaborator`는 프로젝트 관리자가 직접 추가해줘야 얻을 수 있는 권한이다.



## Github Project with Collaborator

> 상단에 설명과 같이 Collaborator 지정해서 팀원들과 같이 프로젝트 진행

#### (1) 프로젝트 관리자가 프로젝트를 생성(repository) 

![]()

#### (2) 프로젝트 관리자가 Settings로 들어가서 Collaborators를 선택

![https://hyoje420.tistory.com/41]()

####

#### (3) 가운데 검색창에  추가할 Collaborator의 GitHub 아이디를 입력

- 검색창으로 검색 혹은 아이디 입력하고 `[Add collaborator]`버튼을 클릭해서 추가한다.

![04]()

#### (4) Github 아이디와 연동된 이메일로 초대장 전송

- 버튼을 클릭하면 초대장을 보낼 수 있고, 그 초대장은 각자 계정과 연동된 이메일로 발송 된다.

 ![02]()

#### (5) 초대된 사람은 클릭하거나, 관리자가 보낸 주소로 직접 들어와서 수락

![05]()

#### (6) 다음은 레포지토리의 메인화면, master branch의 깃허브 주소를 각자 Clone

![01]()

#### (7) `git bash` 에서 내 컴퓨터로 master branch를 Clone

![06]()

#### (8) 내 컴퓨터에 Cloning이 되면서 master branch 생성
![07]()

#### (9) 아래와 같은 명령어로  master에서 내가 생성한 임의 branch 명인 [brchB] 로 변경

```shell
$ git checkout -b [branch name]

# 위의 명령어는 아래의 두 명령어를 합한 것
$ git branch [branch name]
$ git checkout [branch name]
```

![08]()

![09]()

> 명령어를 사용해서 나만의 브랜치를 만들면, 오른쪽과 같이 `[brchB]`로 변경된 것을 확인할 수 있다.
> `git checkout`으로 master와 나의 branch를 이동할 수 있다.

#### (10) 다음과 같이 master branch 아래에 각자의 branch가 생성된 것을 확인

![10]()

#### (11) 작업을 하고나서 다음 명령어를 통해서 Commit

```shell
git push origin [내가 만든 브랜치명]
```



## 참고한 자료

- 개인 홈페이지
  - https://hyoje420.tistory.com/41
  - https://victorydntmd.tistory.com/91