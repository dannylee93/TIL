# Git reset

> Git 의 CLI 명령어를 통해 add / commit / push 단계에서 reset하는 방법을 알아보자



1. *add reset*
2. *commit reset*
3. *push reset*



## Add reset

> 원하지 않는 파일까지 add 했거나 실수를 했을 때 add 단계에서도 취소할 수 있다. 



### View Codes

- 아래와 같이 모든 파일을 `Staged` 상태로 넣었다면,

  `Staged` : Staging Area(Git 에서 add 명령어를 수행한 후의 상태)

  ```shell
  $ git add .
  ```

- **add** 단계에서 취소하기

  ```shell
  $ git reset HEAD [파일명]
  ```

  > 위와 같이 'HEAD' 까지 명령어를 입력하고 파일명을 입력하면 Unstaged 상태로 롤백



## Commit reset

> 원하지 않는 커밋이라면 Commit 단계에서도 reset이 가능하다.



### View Codes

- 우선 아래 명령어를 통해서 커밋 목록을 확인하자

  ```shell
  $ git log
  ```

  > 'log' 명령어를 사용하면 커밋된 목록이 쭉 나온다.

- 커밋 취소 명령어

  ```shell
  $ git reset HEAD^          # 최종 커밋 취소. 그러나 변경된 파일은 남아있다.
  $ git reset --hard HEAD^   # 최종 커밋 취소하고 파일 까지 복구한다.
  $ git reset HEAD~n         # 마지막 n개의 커밋을 취소 한다. 그러나 변경된 파일은                              남아 있다. ( n : 숫자 )
  $ git reset --hard HEAD~n  # 마지막 n개의 커밋을 취소. 파일 또한 복구된다.
  ```

  > HEAD 명령어 뒤에 [파일명]은 작성하지 않아도 된다.

- 커밋 메세지도 변경할 수 있다.

  ```shell
  $ git commit --amend
  ```



## Push reset

> 심지어 푸쉬 된 상태에서도 reset이 가능하다. 하지만 자신의 로컬 내용을 remote에 강제로 덮어쓰기를 하는 것이기 때문에 주의해야 한다.



1. 되돌아간 commit 이 후 모든 commit 정보 살아진다.
2. 협업프로젝트에서 동기화 문제가 발생할 수 있다.



### View Codes

- 가장 최근의 커밋을 취소하고 되돌린다.

  ```shell
  $ git reset HEAD^
  ```

- 원하는 시점으로 돌리기 위한 목록 확인

  ```shell
  $ git reflog  # reflog == 브랜치와 HEAD가 지난 몇 달 동안에 가리켰던 커밋
  $ git log -g
  ```

  > 두 명령어 중 원하는 것을 작성하면 된다.

- 원하는 시점으로 되돌린다.

  ```shell
  $ git reset HEAD@{number}
  $ git reset [commit id]
  ```

  > 이 명령어 또한 원하는 것을 작성하면 된다.

- 되돌려진 상태에서 다시 커밋 메세지 작성한다.

  ```shell
  $ git commit -m "Write commit messages"
  ```

  

## TIP

> Git reset 명령은 아래의 옵션과 관련해서 주의하여 사용해야 한다.



#### Reset 옵션

- `soft` : index 보존(add한 상태, staged 상태), 워킹 디렉터리의 파일 보존. 즉 모두 보존.
- `mixed` : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 보존 (기본 옵션)
- `hard` : index 취소(add하기 전 상태, unstaged 상태), 워킹 디렉터리의 파일 삭제. 즉 모두 취소.





## References

- https://gmlwjd9405.github.io/2018/05/25/git-add-cancle.html
- http://logonluv.blogspot.com/