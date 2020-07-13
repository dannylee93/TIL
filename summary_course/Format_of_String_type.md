# Format of String type

### 문자열 입출력하기

- `char` 타입으로 변수선언을 하면, 문자열을 넣어도 한글자만 출력된다.

- 아래와 같이 메모리 크기를 지정하면 scanf()에서 `&` 기호를 넣지 않아도 된다.

  ```c
  char var_name[30]
  ```

  > 메모리 주소를 이미 변수선언하면서 할당했기 때문이다.

- `int` : 주로 4 bytes

- `char` : 1 bytes



### sizeof() 연산자

자료형이 차지하는 메모리의 크기를 알려준다. 값이 주로 **unsigned int** 로 출력된다.(음수는 X)

- `[__]` 와 같이 변수명 뒤에 크기를 할당하는 방식과 **포인터** 방식을 통한 동적할당 방식과 다르기때문에 출력하면 같은 사이즈로 보이지 않는다.(변수에 직접 할당하는 방식은 컴파일 단계에서 해석되고, 포인터 방식은 런타임 단계에서 적용된다.)



### 배열과 문자열이 메모리에 저장되는 구조

| 구분      |      |      |      |      |      |      |      |      |      |      | 비고     |
| --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | -------- |
| 숫자하나  | 1    |      |      |      |      |      |      |      |      |      | 4바이트  |
| 숫자 배열 | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 40바이트 |
| 문자 하나 | ‘a’  |      |      |      |      |      |      |      |      |      |          |
| 문자 배열 | H    | E    | L    | L    | O    | ‘\0’ |      |      |      |      |          |

> '백슬래쉬+숫자0' 이 문자열의 끝을 알려준다.(Null character)

- 문자열 끝에 `'\0'` 라는 null character 를 만나면 뒤에 메모리는 쓰지 않고 출력을 끝낸다.
- 다만, 인덱스 호출 방식(`변수명[인덱스 위치]`) 를 사용하면 강제로 `0` 값은 출력 가능하다.



### 문자열의 길이 확인 strlen()

- 선행조건 : 

  ```c
  #include <string.h>
  ```

- null character를 빼준다.

- 빈칸도 하나의 글자로 인식한다.

- `[  ]` 을 빈칸으로 두면 컴파일러가 알아서 사이즈를 지정해준다.

- `\n`(escape sequence)를 하나의 글자로 인식한다.



### 기호적 상수와 전처리기, 명백한 상수들

- 기호적 상수(Symbolic constants) 와 전처리기 :

  ```c
  #define PI 3.141592f
  #define AI_NAME "Jarvis"
  ...(후략)
  ```

  > #define을 통해서 초반부에 기호적상수를 선언함으로써 더 명확하고 편리하게 프로그래밍할 수 있다.

- 변수 선언부에서 `const` 조건을 부여하여 값 변경을 못하게 할 수 있다.

  ```c
  int main()
  {
  	const unsigned int ui=0;
  	
  	return 0;
  }
  ```

- 명백한 상수들 Manifest constants :

  ```c
  #define <limits.h>
  #define <float.h>
  ```

  위와 같이, 정수 혹은 실수의 범위를 매번 기억할 수 없기 때문에 편리한 도구들을 활용하여 상수로서 활용할 수 있다.

- 기타 : 

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  ```

  > scanf() 사용 시 warning 없이 사용하고자 할 때 쓴다.

### printf()의 변환지정자 Conversion specifier

```c
%[flags][width][.precision][length]specifier
```

> 형식 지정자의 전체적인 형태이다. 출력옵션을 다양하게 변경할 수 있다.

**변환지정자의 수식어(Modifiers)**

- *수식어란, 형식지정자에서 어떤형식으로 출력할지 맞춰주는 기능이다.*

- flags : 왼쪽 혹은 오른쪽으로 고정된 상태에서 출력하는 기능
- width : 예를들어, `[5]`를 지정했는데 `int 123` 이라면 빈공간`__`이 출력된다.
- precision : 숫자를 부여한 만큼 정밀도를 보장한다.
- length

![](https://github.com/dannylee93/Images/blob/master/Other/printf_modifiers00.JPG)

![](https://github.com/dannylee93/Images/blob/master/Other/printf_modifiers01.JPG)

### printf()가 인자(Argument)를 해석하는 과정

메모리공간을 스택 Stack 하는 과정으로 생각했을 때, 메모리 공간을 할당한 만큼 사용하지 않았다면, 출력에 오류가 생긴다.



### scanf() 함수의 사용법