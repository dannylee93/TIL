# Basics of C Language

### C언어와 함수

- 함수는 `Input - Function - Output`  과정을 거친다.

- 각각의 역할을 하는 함수들의 집합

- `빌드`란, 컴파일+링킹 하는 작업을 말한다. 

- 결과적으로 프로그래밍 작업에서, 함수의 구조를 이해하고 설계하는 것이 가장 중요하다.

- 언어적 측면에서 C언어 :

  <p align='center'><img src='https://github.com/dannylee93/Images/blob/master/Other/Overview_C.JPG?raw=true'></p>

  

### 컴파일러와 링커

<p align='center'>
<img src="https://t1.daumcdn.net/cfile/blog/22549A435270F15629" alt="컴파일러와 링커 실행파일" style="zoom:67%;" />
</p>

- 컴파일러가 모든 일을 할 수 없으니 링커가 서포트 해준다.

- 순서 : 

  ```
  소스코드 - 컴파일러 - 오브젝트코드 - 링커 - 실행파일(.exe)
  ```

  - 여기서 오브젝트는 Debug 폴더에 계속 생성되며, 클린 솔루션을 실행하면 없어진다.

  - 링커에는 `라이브러리 코드`와 `착수(start-up)코드` 가 있다.

    - 라이브러리 코드 : 모든 기능을 다 구현하면서 프로그래밍 할 수 없어, 쉽게 도와주는 기능

    - 착수(Start up)코드 : 프로그램이 시작할 때 공통으로 해야하는 일(예를 들어, 메모리 할당)을 연결해주는 역할을 한다.

      

### 변수가 편리한 이유

- `값 value` 보다`변수 Variable` 가 조금 더 일반적이고 확장하기 좋다.
- 변수 : 메모리의 주소를 직접 다루지 않고도 그 메모리에 데이터가 저장된 공간을 직관적으로 사용하게 해준다.(변수를 설정하면 임의의 값을 가지고 메모리 주소를 가져감)
- 변수 선언 유의사항 :
  - 대소문자를 구분한다.
  - 변수명 앞에 숫자를 넣지 않는다.
  - 빼기 기호`-`를 넣지 않는다.(언더스코어는 가능)
  - 특수문자는 사용하지 않는다.

### printf 기본적 사용

```
#include <stdio.h>
```

를 우선적으로 가져온다.

- `\n` : escape sequence라고 불리는 방법은 printf에서 줄 바꿈을 의미한다.
- `%i` 또는 `%d` : % 뒤에 넣고 싶은 어떤 것을 넣을 수 있다. 여러개 사용하고, 매개변수를 해당 수만큼 반영할 수 있다.

### C언어에서 주석 달기

1. 블럭주석

   ```c
   */가나다 
   마바사*/
   ```

2. 일반 주석

   ```c
   // 아무말이나 뿜뿜
   int main()
   {
   	return 0;
   }
   ```



### 키워드와 예약어

- 키워드 Keywords : 컴파일러에서 그 자체로 유의미한 단어.

  | 구분     |        |          |          |
  | -------- | ------ | -------- | -------- |
  | auto     | double | int      | struct   |
  | break    | else   | long     | switch   |
  | case     | enum   | register | typedef  |
  | char     | extern | return   | union    |
  | const    | float  | short    | unsigned |
  | continue | for    | signed   | void     |
  | default  | goto   | sizeof   | volatile |
  | do       | if     | static   | while    |

- 예약어 Reserved Identifiers : 현재 사용하지 않지만, 컴파일러 업그레이드에 의해 이후에 사용 가능성이 있어 사용자가 해당 단어를 사용하지 못하도록 두는 단어들.



### 함수 만들기

- 예시 :

  ```c
  #include <stdio.h>
  
  void say_hello(void); // prototyping, function declaration
  
  int main()
  {
  	int x, y, z;
  
  	x = 1;
  	y = 20;
  	z = 3;
  
  	z = x + y;
  
  	say_hello();
  	say_hello();
  	say_hello();
  	say_hello();
  
  	return 0;
  }
  
  void say_hello(void)    //함수가 함수를 호출하는 형식
  {
  	int x = 1; // 변수 초기값 설정
  	x = 10;
  	printf("Hello World! \n");
  
  	// void는 return 생략가능
  	return;
  }
  ```

  - 앞에 미리 선언만 하면 main 함수에서 찾아서 함수를 실행한다.
  - `void`는 값을 생략 가능하다는 말.(return 값 혹은 input 값 등)
  - 변수 선언을 하면 초기 임의의 값이 할당 된다. 변수선언과 동시에 초기값 할당 가능.

## Tips

- VS IDE 에서 C 언어는 C++ 패키지와 함께 내장되어있다.
- 파일 생성 시 C++ 로 자동생성 되는 것을 C로 전환 :
  - 솔루션의 속성 Advance 에서 컴파일 옵션을 C로 전환
  - 파일 이름 직접 변경(F2 키를)
- 문제가 있을 것 같은 곳은 `빨간 물결` 이 생긴다.
- 비주얼 스튜디오에서 솔루션안에 프로젝트가 여러개 있는 형태이다.
- Tools 라는 편의기능을 통해 테마, 폰트변경이 가능하다.
- 명령 프롬프트 : X86 Native Tools 에서 해당 실행파일(.exe)로 실행할 수 있다.
- VScode 는 VS 보다 조금 더 가벼운 프로그램이며 컴파일러(mingw64)와 익스텐션을 각각 따로 설치해야하는 단점이 있다.



## References

- *[홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)*

