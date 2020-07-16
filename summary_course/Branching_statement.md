# Branching statement | 분기문

### 분기문의 대표급 if문

```c
//분기문 if 
if (number % 2 == 0) {
    printf("Even");
};
if (number % 2 != 0) {
    printf("Odd");
};  //if를 두번 하면 나눗셈 연산을 반복하기 때문에 비효율적

//분기문 if-else
if (number % 2 == 0) {
    printf("Even");
};
else {
    printf("Odd");
};
```

> if를 계속 나열하면서 조건을 부여하면 연산이 계속 늘어난다. 이 때, else를 붙이면 연산량을 줄일 수 있다.



### 문자의 입출력 getchar and putchar

- `getchar()` : 문자 하나의 입력을 받는다.

- `putchar()` : 문자 하나의 출력을 한다.

- 선행 과정 : `#include <stdio.h>`

- 주의사항은, 각각이 한 글자씩 출력한다는 점이며 `scanf()` 외에 다양한 함수들이 있다는 점이다.

- 코드 예시 : 

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>  //getchar(), putchar() 둘 다 있음.
  
  int main(void) {
  	char ch;
  
  	while ((ch = getchar()) != '\n') {
  
  		if (ch >='0' && ch <='9') {
  			ch = '*';
  		}
  		else {
  			ch = 'w';
  		};
  
  		putchar(ch);
  	};
  }
  ```



### 문자관련 함수들

- `#include <ctype.h>` : C 문자 분류는 C언어에서 ANSI 표준 라이브러리의 명령 중 하나로, 문자들을 조건에 맞는지 검사하고 변환하는 함수이다.

  <p align = 'center'><img src="https://github.com/dannylee93/Images/blob/master/Other/ctypeh.JPG?raw=true" alt="ctype.h" style="zoom:67%;" /></p>

  

### else if

`if`의 조건을 만족하지 않는 구간에서 또 다른 분기문을 설정할 때 사용한다.

### else와 if 맞추기

```c
//else문 사용시 잘못된 사용 사례
if (number > 5)
	if (number < 10)
		printf("Larger than 5 smaller than 10\n");
	else
		printf("Less than or equal to 5");
```

> else 문을 최초 if문과 매칭하고 싶지만 컴파일러는 indenting을 무시하기 때문에 가장 가까이에 있는 if문과 엮으려고 한다.



### 논리 연산자 Logical Operators

주어진 논리식을 판단하여, 참(true)과 거짓(false)을 결정하는 연산자이다. `AND` 와 `OR` 연산자는 두개의 피연산자 Operand 를 가지는 이항 연산자 이며, 피연산자들의 결합 방향은 왼쪽에서 오른쪽 이다.

| 논리 연산자 |                             설명                             |
| :---------: | :----------------------------------------------------------: |
|     &&      |      논리식이 모두 참이면 참을 반환함. (논리 AND 연산)       |
|    \|\|     |  논리식 중에서 하나라도 참이면 참을 반환함. (논리 OR 연산)   |
|      !      | 논리식의 결과가 참이면 거짓을, 거짓이면 참을 반환함. (논리 NOT 연산) |

- 진리표 Truth table : 

  |   A   |   B   | A && B | A \|\| B |  !A   |
  | :---: | :---: | :----: | :------: | :---: |
  | true  | true  |  true  |   true   | false |
  | true  | false | false  |   true   | false |
  | false | true  | false  |   true   | true  |
  | false | false | false  |  false   | true  |



### 조건 연산자 Conditional Operators

주로 3항 연산자(ternary) 라고도 하며, 간단한 조건문 구현 시 `if-else` 문 대신 사용할 수 있다.

- 기본 형태 :

  ```
  변수 = true ? 왼쪽값 : 오른쪽 값    //true이면 왼쪽
  변수 = false ? 왼쪽값 : 오른쪽 값  //false이면 오른쪽
  ```

  > 가장 왼쪽은 조건식을 두고, `:` 사이에 두개의 값을 둔다.

- 코드 예시 : 

  ```c
  //ex.2
  int number;
  scanf("%d", &number);
  
  bool is_even;
  
  //일반적으로 if-else를 썼을 때 나오는 코딩 형태
  if (number % 2 == 0)
  is_even = true;
  else
  is_even = false;
  
  //조건 연산자를 통해 위와 동일한 기능 구현했을 때
  is_even = (number % 2 == 0) ? true : false;
  
  //0,1 을 사용해도 동일한 결과 얻을 수 있다.
  temp = 1 ? 1024 : 7;
  printf("%d\n", temp);
  
  temp = 0 ? 1024 : 7;
  printf("%d\n", temp);
  ```

### Continue and break

- `continue` : 해당 위치에서 다시 for 조건으로 올라간다.

- `break` : 해당 위치에서 정지 후 탈출한다.

- 코드 예시 :

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  
  int main(void) {
  
  	for (size_t i = 0; i < 10; i++) {
  		if (i == 5) {
  			break;  //continue를 하면 해당 조건만 출력하지 않고 건너 뛴다,
  		};
  		printf("%d", i);
  	};
  }
  ```



### 다중선택 Switch and case

`switch` 구문은 해당 조건을 통해 연산 후, `case` 위치와 맞는 위치로 이동하여 계산하는 방식이다.

```c
int main(void) {

	char c;
	
	while ((c = getchar()) != '.') {
		printf("You love ");

		switch (tolower(c)){
		case 'a':
			printf("apple");
			break;
		case 'b':
			printf("banana");
			break;
		case 'c':
			printf("cake");
			break;
		default:
			printf("nothing");
		};
		printf(".\n");
		
		//뒤에 글자들을 줄바꿈이 나올때까지 전부 무시한다는 의미
		while (getchar() !='\n'){
			continue;
		};

	};
}
```



## References

- [홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)