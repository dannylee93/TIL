# Types of Data in C Language

### 데이터와 자료형

<p align='center'><img src='https://github.com/dannylee93/Images/blob/master/Other/size_and_types.JPG?raw=true'></p>

> 데이터가 정수인지 실수인지에 따라 각각 저장공간이 달라진다.



### 변수와 상수 Variable & Constant

```c
int angel = 1004;
```

- 여기서 `int`는 자료형, `angel`은 변수, `1004`는 **리터럴 상수(Literal Constant)**를 의미한다.
- **리터럴 상수(Literal Constant)** : 문자 그대로 의미있는 데이터

```c
const int angel = 1004;
```

- `const` : 한정자 혹은 제한자(Qualifier) 라고 하며, 해당 조건을 부여하면 변수의 값이 변하지 않는 기호적 상수로 변경된다.
- `angel` : 제한자에 의해 **기호적 상수**로 변경
- `1004` : Symbolic Constant 로 변경된다.



### scanf()

콘솔 창으로 부터 사용자 입력을 받는 기능을 담당한다.

```c
//#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int i = 0, j = 0;
	int sum = 0;

	printf("Input two integers\n");

	scanf("%d%d", &i, &j); // & : ampersand

	sum = i + j;

	printf("%d plus %d = %d\n", i, j, sum);

	return 0;
```

> scanf() 는 printf() 기능과 달리 `" "` 내에 띄어쓰기 적용이 안되며, `&`라는 ampersand 기능을 사용해야한다.

- `&` 기호 사용 이유 : 변수의 주소를 받고 입력값을 덮어 씌우기 위해, 변수의 주소를 알려주는 기능으로서 사용

- **콘솔로 입출력 만들기 요약 :** 

  - 콘솔에 `Input` 입력 시, `space bar` 혹은 `Enter` 로 구분할 수 있다.

  - `%d` 또는 `%i` 를 실수형으로 출력하고 싶으면 `%f`로 변경한다. (각각 의미가 있음)

    <p align='center'><img src="https://github.com/dannylee93/Images/blob/master/Other/summary_specifiers.JPG?raw=true";></p>

### 정수와 실수

- 정수 : 음의 정수와 양의정수가 있으며, 내부적으로 이진수로 해석된다.

- 실수 : 부동 소수점(Floationg point)을 사용.

  ```c
  // 다 같은 의미
  3.14 = 3.14E0 = 3.14e0 = 0.314E1 = 31.4E-1
  ```

- **부호없는 정수 unsigned int :**

  - 8 비트 : 94 ~ 0 의 값 
  - 32 비트 : 
  - 메모리 사이즈에 따라 다양하게 가능하다.

- 부호 있는 정수 signed int :

  - 맨 앞 한칸을 부호 표시로 사용한다( 0 : 양수, 1 : 음수)

- float 와 double :

  - 32 비트 single precision 을 `float` 로 사용한다.
  - 64 비트 double precision 을 `double` 로 사용한다.



### 정수의 overflow 현상

자료형이 표현할 수 있는 가장 큰 값을 넘으면 최소 값으로 복귀하고, 가장 작은 값에서 빼기를 실행하면 최대값이 된다. 이러한 현상을 '정수의 오버플로우' 현상이라고 한다. 

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>  //각각이 가질수있는 가장 큰값,작은값 알려줌

int main()
{
	unsigned int i = 0b11111111111111111111111111111111; //0b는 2진수라는 의미
	unsigned int u = UINT_MAX;
	signed int su = INT_MAX;

	printf("%u\n", u);
	printf("%u\n", su);

	printf("%u\n", i);
	printf("%u\n", sizeof(unsigned int));
	//4라고 나오는데, 이건 4바이트 타입이라는 말 == 32비트
	printf("%u", sizeof(i)); 

	return 0;
```

> unsigned int == 4바이트 == 32비트. 값을 11111... 과 같이 풀로 채우고 printf()를 실행하면 최대 값인 2<sup>32</sup> 에서 -1한 값이 나온다. 그 이유는 최소 숫자가 0에서 시작하기 때문이다.



### 다양한 정수형들

<p align='center'><img src="https://github.com/dannylee93/Images/blob/master/Other/types_of_int.JPG?raw=true";></p>

> 정수 자료형에 따라 메모리의 값이 달라지며, 형식지장자(%_)도 알맞게 써야한다.

```c
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>  //각각이 가질수있는 가장 큰값,작은값 알려줌

int main()
{
	char c = 65;
	short s = 200;
	unsigned int ui = 3000000000U;
	long l = 65537L;
	long long ll = 123456789086422LL;

	printf("char = %hhd, %d, %c\n", c, c, c);
	printf("short = %hhd, %hd, %d\n", s, s, s);
	printf("unsigned int = %u, $d\n", ui, ui);
	printf("long long = %lld, %ld\n", ll, ll);
	
	return 0;
```

<p align='center'><img src="https://github.com/dannylee93/Images/blob/master/Other/captured_results.JPG?raw=true";></p>

> 각 정수형에 따라 출력되는 값이 변한다. 'A' 는 65가 문자로서의 의미이다.

 ### 8진수와 16진수

- 코드 예시 :

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  
  int main()
  {
  	unsigned int decimal = 4294697295;
  	unsigned int binary = 0b11111111111111111111111111111111;
  	unsigned int oct = 037777777777;
  	unsigned int hex = 0xffffffff;
  
  	printf("%u\n", decimal);
  	printf("%u\n", binary);
  	printf("%u\n", oct);
  	printf("%u\n", hex);
  
  	printf("%o, %x, %#o, %#x, %#X", decimal, decimal, decimal, decimal, decimal);
  
  	return 0;
  }
  ```

  - `0b` : 2진수라는 의미
  - `0` : 앞에 숫자 0을 붙이면 8진수라는 의미
  - `x` : 16진수라는 의미
  - 참고사항 : 16진수로 변환된 값을 직접 넣고 싶으면 `some value to hex`라고 검색
  - `%#o` : `%` 와 `_` 사이에 `#`라는 prefix 기호를 넣으면 정확히 출력을 도와준다.

### 고정 너비 정수형 Fixed width Integers

자료형의 사이즈가 제각각이라면 어떤 특정한 시스템에서는 작동하지 않을 수 있다. 이럴 때 변수의 사이즈를 명확하게 지정해주어 이식성이 좋은 코드를 생성할 수 있다.

- 코드 예시 : 

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  #include <inttypes.h>  //아래 int 타입을 고정하는 기능을 사용할 수 있음
  
  int main()
  {
  	int i;  //4바이트 정수가 만약 int가 2바이트로 설정되어있으면 overflow문제 발생
  	int32_t i32;  //메모리의 넓이를 32bit로 고정
  	int_least8_t i8;  //가장 작은
  	int_fast8_t f8;  //8비트 중에서 가장 빠른 것
  	intmax_t imax;  //int에서 가장 메모리를 많이 사용하는 사이즈
  	uintmax_t uimax;  //uint에서 가장 메모리를 많이 사용하는 사이즈
  
  	i32 = 1004;
  
  	printf("me32 = %d\n", i32);
  	printf("me32 = %" "d" "\n", i32);
  	printf("me32 = %" PRId32 "\n", i2);
  		
  	return 0;
  ```

### 문자형

컴퓨터는 내부적으로 모두 숫자로 바꾼다. 문자는 `char` 타입으로 바꾸어 활용한다. 아래와 같은 아스키 차트를 통해 각 문자 혹은 행위가 숫자로 표현되는 지 보여준다.

<p align='center'><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/ASCII-Table.svg/1200px-ASCII-Table.svg.png"></p>

- 코드 예시 :

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  
  int main()
  {
  	char c = 'A';
  	char d = 65;  //d='A' 와 같다.
  	
  	printf("%c, %hhd\n", c, c);
  	printf("%c, %hhd\n", d, d);
  	printf("%c\n", c+1); //1을 더하면 B가 된다.
  
  	// 컴퓨터에서 띵동소리 내기
  	char a = '\a';  //아스키 코드에서 BELL을 char 타입에서 표현한 예시
  	printf("%c", a);
  	printf("\07");  //BELL을 8진수로 직접 입력할 때
  	printf("\x7");  //BELL을 16진수로 직접 입력할 때
  
  	//백슬래쉬로 밑줄입력 구현
  	float salary;
  	//print("$______");
  	printf("$______\b\b\b\b\b\b");
  	scanf("%f", &salary);
  
  	return 0;
  }
  ```




### 부동소수점 Floating System

부동소수점은 점의 위치가 고정되지 않고 둥둥 떠다니는 것 같이 보여 부동소수점이라고 한다.

과학적표기법(Scientific notations)에 의해 표기되는 `m * 10`<sup>n</sup> 에서 같은 숫자도 m과 n을 바꾸면서 다양하게 표기할 수 있다.

-  `m * 10`<sup>n</sup>  : `m`은 유효숫자, `n`은 지수(exponent)를 의미
- 부동소수 표현 방법이 메모리를 쪼개서 쓰는 방식이기 때문에 이 점에 유의할 필요가 있다.

- 부동 소수점 사용 중 만나게 되는 한계점 :
  1. 너무 큰 숫자 + 아주 작은 숫자 : 숫자가 사라져 버린다(내부구조의 한계)
  2. `0.01f`를 100번 더해도 1이 안된다.(비트 메모리 사용하는 구조 상)
  3. Overflow와 Underflow 이슈

- 예시 코드 :

  ```c
  #include <stdio.h>
  #include <float.h>
  
  int main()
  {
  	printf("%u\n", sizeof(float));
  	printf("%u\n", sizeof(double));  //float보다 메모리를 두배 더 써서
  	printf("%u\n", sizeof(long double));  //커서를 가져다 대면 메모리 사용량을 볼 수 있다.
  
  	float f = 123.456f;  //일반적으로 float는 리터럴상수 끝에 f를 붙여주는게 좋다.
  	double d = 123.456;
  
  	float f2 = 123.456;  //f를 붙이지 않으면 경고가 뜬다. truncate 절삭으로 인한 정밀도 저하
  	double d2 = 123.456f;  //float를 double에 넣는건 문제 없음
  	
  	int i = 3;
  	float f3 = 3.f;  // 3.0f '.0'점을 넣어주는 것이 가독성에 좋음
  	double d3 = 3.;  // 3.0
  	
  	float f4 = 1.234e10f;  //과학적표기법도 사용가능하다.
  
  	float f5 = 0xb.ap1;  //0x == 16진수, e대신 p를 적었다.
  	double d
  
  	return 0;
  }
  ```

  

### 불리언 타입 Boolean

보통 '참 거짓' 이라 불리는 아래 타입은 내부적으로 0 또는 1로 해석되어 사용된다.

- 예제 코드 :

  ```c
  #include <stdio.h>
  #include <stdbool.h>  //표준에 해당 include가 추가됨.
  
  int main()
  {
  	printf("%u\n", sizeof(_Bool)); //1 byte
  
  	//고전C에서는 boolean type이 없었는데 _Bool 이 추가됨
  	_Bool b1;
  	b1 = 0;  //false
  	b1 = 1;  //true
  
  	print("%d\n", b1);  //별다른 형식지정자가 없어 d로 출력한다.
  
  	//include를 통해 bool을 선언할 수 있다.
  	bool b2, b3;
  	b2 = true;
  	b3 = false;
  
  	printf("%d %d\n", b2, b3);
  
  
  	return 0;
  ```

  

## References

- *[홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)*

