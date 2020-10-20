## Libft

> Libft 과제 관련 메뉴얼 해석 및 주의사항 기록

### memset

```c
void	*ft_memset(void *b, int c, size_t len);
```

- `len` 길이의 바이트 수 만큼 `c` 로 문자열 `b` 를 채운다.

### bzero

```c
void	*bzero(void *s, size_t n);
```

- `n` 길이의 바이트 수 만큼 `숫자 0` 으로 문자열 `b` 를 채운다.

### memcpy

```c
void	*memcpy(void *restrict dst, const void *restrict src, size_t n);
```

- `n` 길이의 바이트 수 만큼, `src` 에서 `dst` 로 카피한다.
- `dst` 의 포인터를 리턴한다.

### memccpy

```c
void	*memccpy(void *restrict dst, const void *restrict src, int c, size_t n);
```

- `src` 문자열에서 `dst` 로 바이트를 카피한다.
- 만약 `c` 가 `src` 에 있다면, 복사를 중단하고 `c` 가 있는 바로 다음 위치의 `dst` 포인터를 리턴한다. 
- 그렇지 않으면  `n`  바이트 수만 큼 카피하거나, `NULL` 을 리턴한다.

### memmove

```c
void	*ft_memmove(void *dst, const void *src, size_t len);
```

- `len` 길이의 바이트 수 만큼 `src` 문자열에서 `dst` 로 복사 및 이동.
- 두 문자열은 오버랩 되며, 
- `memcpy` 함수와 차이점 :
  - 두 함수 모두 특정 메모리 주소에서 원하는 크기만큼 다른 곳으로 복사해준다. 하지만 `memcpy` 는 메모리의 내용을 직접 복사하고, `memmove` 는 복사할 메모리의 내용을 임시공간에 저장한 후 복사한다.
- 주의할 점 :
  - `src` 주소가 `dst` 보다 큰 값이면, `src` 의 처음부터 `len` 만큼 복사한다.
  - `src` 주소가 `dst` 보다 작은 값이면, `src` 의 마지막 `byte` 부터 `len` 만큼 복사한다.

### memchr

```c

```

- asd

### memcmp

```c
asd
```

- 

### strlcpy

```c
size_t	ft_strlcpy(char *restrict dst, const char *restrict src, size_t dstsize);
```

- `strlcpy()` 함수는 문자열을 복사하고 병합하는 함수이다. `dest` 의 전체 buffer를 받고 
- `dstsize - 1` 의 문자를 `src` 에서 `dst` 로 복사한다.
- 리턴 값 : 
  - 만드려는 문자열의 총 길이를 반환한다.
  - For strlcpy() that means the length of src. (카피함수에서는 그 총 길이가 소스 길이를 의미)
  - If the return value is >= dstsize, the output string has been truncated. (리턴 값이 dstsize 보다 크거나 같으면, 그건 싹둑)

### strchr & strrchr

```c
#include <string.h>
...
char *strchr(const char *s, int c);
char *strrchr(const char *s, int c);
```

- `strchr()` 함수는 문자열에서 특정 문자를 찾을 때 사용하는 함수이다. (The first occurrence of `c`(converted to a char) in the string pointed to by `s`).
- `strrchar()` 함수는 마지막으로 있는 `c` 를 리턴한다.
- 리턴 값 : 문자열에서 찾은 `포인터` 를 리턴한다. 만약 찾지 못했다면 `NULL`을 리턴한다.

### strnstr

```c
#include <string.h>
...
char *strnstr(const char *haystack, const char *needle, size_t len);
```

> Haystack : 건초 더미, needle : 바늘

- `haystack` 에서 `null` 로 끝나는 `needle` 문자열이 있는 **첫번째 위치**를 반환하는 함수이다. 

- 리턴 값 : 
  - `needle` 문자열이 비어있는 문자열이라면, `haystack` 을 리턴한다.
  - `needle` 문자열이  `haystack` 에 없다면, `NULL` 을 리턴한다.
  - `needle` 문자열이  `haystack` 에 있다면, 그 시작 부분의 위치 포인터를 반환한다.
  
- 주의할 점:

  ```c
  const char *largestring = "Foo Bar Baz";
  const char *smallstring = "Bar";
  char *ptr;
  
  ptr = strnstr(largestring, smallstring, 4);
  ```

  > 해당 함수는 `NULL` 을 반환한다. 왜냐하면 `largestring` 의 첫번째 부터 4번째 길이 까지는 `smallstring` 이 발견되지 않기 때문이다.

### strncmp

```c
#include <string.h>
...
char *strncmp(const char *s1, const char *s2, size_t n);
```

- `n` 의 크기만큼 `s1`, `s2` 를 비교하는 함수이다.
- 리턴 값 :
  - `s1 > s2` : 음수 값
  - `s1 = s2` : `0`
  - `s1 < s2` : 양수 값

### calloc

```c
#include <stdlib.h>
...
void	*malloc(size_t size);
void	*calloc(size_t count, size_t size)
```

- `malloc` 함수와 달리 매개변수가 2개이다. `count` 인자는 메모리의 단위 갯수 이다.
- `calloc()` 함수로 동적할당한 메모리는 모든 비트를 0으로 초기화 해준다.

### strdup

```c
#include <string.h>
...
void	*strdup(const char *s1);
```

- `strdup()` 함수는 `s1` 문자열을 동적할당을 받아 카피하여 그 포인터 주소를 리턴하는 함수이다.

### ft_substr

```c
char	char	*ft_substr(char const *s, unsigned int start, size_t len);
```

- `s` 문자열에서 `start` 인덱스 부터 `len` 길이 만큼 새로 만드는 함수.
- 생성된 substring 을 리턴하며, 실패할 시 `NULL` 을 리턴한다.

### ft_strjoin

```c
char	*ft_strjoin(char const *s1, char const *s2);
```

- 두 문자열을 합쳐 새로운 문자열을 만든다. 실패할 시 `NULL` 을 리턴한다.
  - `strlcpy`를 통해서 우선 첫 문자열을 동적할당 메모리에 저장하고 리턴 값인 인덱스를 변수에 저장한다.
  - `strlcat` 함수를 사용하여 `s2` 문자열을 저장한다.

### ft_strtrim

```c
char	*ft_strtrim(char const *s1, char const *set);
```

- `s1` 에서 `set` 과 동일한 부분이 있다면, 앞뒤로 제거한 문자열을 리턴한다.

### ft_split

```c
char	**ft_split(char const *s, char c);
```

- 문자열 `s` 를 받고 `c` 로 문자열을 나눈다.
- 문자열 `c` 의 역할은 구분자(delimeter) 역할이다.

### ft_itoa

```c
char	ft_itoa(int n);
```

- 정수를 문자열로 변환하는 함수이다.

- 예시 :

  ```c
  123 >>> "123"
  1246674 >>> "1246674"
  ```

### ft_strmapi

```c
char	*ft_strmapi(char const *s, char (*f)(unsigned int, char));
```

- 문자열 `s` 를 가지고 새로운 문자열을 만들기 위해 함수 `f` 를 사용한다.
- Return Value :
  - 함수 `f` 가 연속적으로 적용된 문자열을 반환하고, 실패할 시 `NULL` 을 리턴한다.
- Parameter :
  - 반복할 문자열
  - 각 char 타입에 적용할 함수

### ft_putchar_fd

```c
void	ft_putchar_fd(char c, int fd);
```

- **char** 타입의 결과를 출력한다.
- file descriptor on which to 'write'

### ft_putstr_fd

```c
void	ft_putstr_fd(char *s, int fd);
```

- 문자열 `*s` 를 주어진 파일 디스크립터에 출력한다.
- file descriptor on which to 'write'

### ft_putendl_fd

```c
void	ft_putendl_fd(char *s, int fd);
```

- 문자열 `*s` 를 주어진 파일 디스크립터에 출력하고, 새로운 한 줄을 추가한다
- file descriptor on which to 'write'

### ft_putnbr_fd

```c
void	ft_putnbr_fd(int n, int fd)
```

- 주어진 `n` 에 대해 문자열 형태로 파일 디스크립터에 출력한다.



## 구조체 관련 함수

> Asd

- 함수 작성에 적용할 메인 구조체

  ```c
  typedef	struct	s_list
  {
  	void					*content;
  	struct s_list	*next;
  }								t_list;
  ```

  - `content` : 데이터를 저장하는 요소이다. `void` 타입을 적용하여 데이터 타입과 관련없이 저장될 수 있도록 한다.
  - `next` : 다음 요소(element)의 주소이거나 , 마지막 요소일 시 `NULL` 을 갖는다.

### ft_lstnew

```c
t_list	*ft_lstnew(void *content);
```

- 또한, `next` 구조체 변수는 `NULL` 을 리턴한다.
- `malloc` 허용. (동적할당을 통해 )
- Description : 
  - 동적할당을 통해 새로운 요소를 리턴한다. `content` 는 파라미터 값에 의해 초기화 되고, `next` 는 NULL로 초기화 된다.

### ft_lstadd_front

```c
void	ft_lstadd_front(t_list **lst, t_list *new);
```

- `new` 라는 요소를 시작하는 리스트에 추가하기
- Parameter :
  - 첫번째 `link of a list`의 포인터 주소
  - 리스트에 추가한 요소의 포인터 주소

### ft_lstsize

```c
int		ft_lstsize(t_list *lst);
```

- 사용된 구조체 리스트의 길이를 리턴하는 함수.

### ft_lstlast

```c
t_list	*ft_lstlast(t_list *lst);
```

- 구조체 리스트의 마지막 요소를 리턴하는 함수.

- Parameter :
  - 구조체 리스트의 시작점 포인터 주소

### ft_lstadd_back

```c
void	ft_lstadd_back(t_list **lst,  t_list *new);
```

- 리스트의 마지막에 `new` 를 추가한다.
- Parameter :
  - 첫번째 `link of a list`의 포인터 주소
  - 리스트에 추가한 요소의 포인터 주소

### ft_lstdelone

```c
void	ft_lstdelone(t_list *lst, void (*del)(void *));
```

- `lst` 의 `next` 구조체 부분을 `free` 로 없애주고, `content` 는 `del` 함수 포인터 사용
- Parameter :
  - `free` 를 적용할 요소
  - `content` 를 삭제하기 위한 함수의 주소

### ft_lstclear

```c
void	ft_lstclear(t_list **lst, void (*del)(void *));
```

- 주어진 요소의 연속적인 모든 요소를 삭제하고 `free` 를 적용하며, 리스트의 포인터는 `NULL` 로 변경.
- Parameter :
  - 요소의 포인터 주소
  - `content` 를 삭제하기 위한 함수의 주소

### ft_lstiter

```c
void	ft_lstiter(t_list *lst, void(*f)(void *));
```

- `lst` 를 반복하며, 함수 `f` 를 각 요소의 `content` 에 적용시키는 함수.
- Parameter :
  - 요소의 포인터 주소
  - 리스트를 반복시키기 위한 함수 주소

### ft_lstmap

```c
t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));
```

- `f` 함수를 적용하며`lst` 를 반복하고 그 결과들을 새로운 리스트에 적용한다. `del` 함수는 `content` 를 삭제하는데 사용한다.
- 새로운 리스트를 리턴한다. 실패할 시 `NULL` 리턴
- Parameter :
  - 요소의 포인터 주소
  - 리스트를 반복시키기 위한 함수 주소
  - `content` 를 삭제하기 위한 함수의 주소(필요한 만큼)
- `malloc` `free` 사용

## Makefile

Makefile 이 필요한 가장 큰 이유는 증분 빌드(Incremetal Build) 이다. 규모가 큰 프로젝트를 빌드할 수록, 매번 모든 대상을 빌드할 수 없다.

- 구조 :

  ```
  <target> : <dependency>
  (tab)<Recipe>
  ```

  - 대상 Target : 빌드의 대상에 대한 이름. 명령에 의해 생성되는 결과 파일 
  - 의존 관계 Dependency : 대상을 만들 때 의존되는 파일들.
  - 명령 Recipe : 빌드 대상을 생성하는 명령. 여러 줄로 작성할 수 있으며, 의존 관계에 있는 파일이 변경되었거나 대상 파일이 없을 때 명령이 실행된다. `명령을 쓸 때는 반드시 tab 키로 띄워준 후 사용한다.`

- 변수 사용하기

  - Makefile 내부에서 사용하는 변수 및 확장성을 용이하게 해 주는 `자동변수`가 있다.
  - 자주 사용하는 자동 변수
    - **`$@`:** 현재 Target 이름
    - **`$^`:** 현재 Target이 의존하는 대상들의 전체 목록
    - **`$?`:** 현재 Target이 의존하는 대상들 중 변경된 것들의 목록
    - **`$%` : 대상의 이름 (해당 규칙 대상이 아카이브 인 경우)**

- 자주 사용하는 문법

  - `$(addsuffix 접미사, 문자열)`

    ```null
      $(addsufix  .c, memo  main) => memo.c   main.c 
    ```

  - `$(addprefix 접두어, 문자열)`

    ```null
      $(addprefix src/, memo main) => src/memo   src/main
    ```

  - `$(shell <shell-command>)`

    ```null
      SH = $(shell ls *.c)  => shell 명령에 대한 결과가 변수에 들어감
    ```

  - `$(subst 찾을 문자, 변경할 문자, 대상 문자)`

    "대상문자"에서 "찾을 문자"를 "변경할 문자"로 변경해 준다.

  - `$(patsubst 찾을 패턴, 변경할 패턴, 대상 문자)`

    subst와 기능은 동일하나 확장자를 바꿀때 사용함

  - `$(strip 대상문자)`

    대상문자에서 모든 공백을 1칸으로 줄인다. 여백이 많아도 모두 1칸으로

  - `$(filter 찾을 문자, 대상문자)`

    대상문자에서 찾을 문자를 포함한 문자들을 찾아서 저장한다.

  - `$(filter-out 찾을 문자, 대상문자)`

    filter와 반대로 찾을 문자가 있는 경우를 제외하고 저장한다.

  - `$(join 원본문자, 붙일문자)`

    원본문자와 붙일문자를 붙여서 한 문자로 만든다.

  - `$(dir 대상문자)`

    대상문자에서 파일문자를 제외한 경로명만 추출한다.

  - `$(notdir 대상문자)`

    대상문자에서 파일명만 추출한다.

  - `$(baseanme 대상문자)`

    대상문자에서 확장자를 제외한 문자를 알려준다.
    
  - `.PHONY:` 'PHONY' 는 실제 파일명이 아닌 가상의 이름이라는 것을 나타내며 실제 Makefile 경로에 나열해 놓은 파일이 있을 경우 오동작을 일으킬 가능성이 있으므로, 가상의 이름이라는 것을 지정해주기 위해 사용.

## File Descriptor

> 유닉스 시스템에서 모든 것은 파일이라고 부른다. 일반적인 정규파일 부터, 디렉토리, 소켓, 파이프 등등 모든 객체들은 파일로써 관리된다. 프로세스가 이 파일들을 접근할 때 파일 디스크립터라는 개념을 이용하게 된다. 
>
> 또한 파일 디스크립터는 *Non-negative Integer* 값을 갖는다. 즉 0 이상의 양수인 정수 값을 가진다. 실행을 시작할 때, 기본적으로 할당이 되는 파일 디스크립터들이 있는데, 바로 표준 입력(Standard Input), 표준 출력(Standard Output), 표준 에러(Standard Error)이다. 이 들에게 각각 0, 1, 2 라는 정수가 할당되며, POSIX 표준에서는 STDIN_FILENO, STDOUT_FILENO, STDERR_FILENO로 참조된다. 이 매크로는 <unistd.h> 헤더 파일에서 찾아 볼 수 있다. 
>
> 출처: https://dev-ahn.tistory.com/96 [Developer Ahn]

### 파일 입출력

- 파일 열기

  ```c
  #include <sys/types.h>
  #include <sys/stat.h>
  #include <fcntl.h>
  
  int open(const char *path, int flag);
    // 성공 시 파일 디스크립터 반환, 실패 시 -1 반환
  ```

  - **`Flag` :** 

    | 오픈 모드 |                 설명                  |
    | :-------: | :-----------------------------------: |
    |  O_CREAT  |           필요하면 파일생성           |
    |  O_TRUNC  |           기존 데이터 삭제            |
    | O_APPEND  | 기존에 데이터를 보존하고, 뒤이어 저장 |
    | O_WRONLY  |            쓰기 전용 오픈             |
    | O_RDONLY  |            읽기 전용 오픈             |
    |  O_RDWR   |       읽기, 쓰기 겸용으로 오픈        |

  - 사용 예시 :

    ```c
    fd = open("file1.txt", O_CREAT | O_WRONLY | O_TRUNC);
    
    if(fd== -1)
        //에러 출력
    ```

- 파일 닫기

  ```c
  #include <unistd.h>
  
  int		close(int fd);		//fd = file descriptor
  ```

  > 성공 시 `0`, 실패 시 `-1` 을 반환한다.

- 데이터 출력하기

  ```c
  #include <unistd.h>
  
  int		write(int fd, const void *buf, size_t nbytes);
  ```

  > write(fd, 사용하려는 포인터 주소, 길이)

  - `fd == 1` : 모니터에 출력한다.

## Others

### size_t

자료형 끝에 `_t` 가 붙어 있다. 시스템(운영체제)에서 정의하는 자료형이라는 의미이다. 컴퓨터에 발전에 따라 자료형의 사이즈가 바뀌는 점을 고려하여 정의한 것이다. (예전에는 `int` 가 16비트, 현재는 32비트)

자료형이 변하면 프로그램 코드 수정이 빈번하기 때문에, `typedef` 으로 만든 자료형을 사용하는 편이 좋다.

