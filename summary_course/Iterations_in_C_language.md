## Iterations in C language | 반복문 

> 반복문을 선택할 때는 문제를 구현하는 과정에서 '진입조건'이 중요한지(for, while) 혹은 '탈출조건'이 중요한지(dowhile)를 따져서 선택해야한다.

### Loop & scanf()

- while문을 사용하여 반복적으로 scanf()를 통해 입력을 받아 연산할 수 있다.

- 주의사항 : 

  ```c
  int num, status;
  status = scanf("%d", &num);  //여기서 status에 담긴 값은 0 또는 1이다. 
  ```

  > scanf()의 리턴값은 선언한 형식과 동일한 입력의 개수를 출력한다.



### 의사코드 Pseudo code

'진짜와 유사한' 의미를 가진 코드는, 인간의 언어를 사용해서 코드와 비슷한 내용을 이해하기 쉽도록 표현할때 사용하는 코드이다. 주로 의사소통의 수단으로 사용한다.



### While문의 진입조건 유의사항

- while 문의 기본 형태 :

  ```C
  while(진입조건 expression){
  	/*statement*/
  };
  ```

  > while 문 사용 시, Indenting잘하기, 진입조건 맞추기, null statement 줄이기를 해야한다.



### 관계 연산자 Relational Operators

관계 연산자는 데이터의 관계에 대해서 판단하는 연산자이다.

![연산자 우선순위](https://lh3.googleusercontent.com/proxy/4AqFEhIF6CLApzHZxD0PNTcJJk2cT-K0xOpkNBDTESK7-9surN7UfJ-P3g8fWMGPnxfK2Lmo4AIUJVDalXWS1VmAxWDId6VH7M_35UQW4SuclRVdsHAxlAiVAGEwHwMLeY8Pvji86WkdWwrQ8EL_gtLB)

- 실수 끼리 비교할 때는 주로 `!=`는 쓰지 않는다(값이 정확할 때 까지 `False`출력)

  ```c
  const double PI = 3.141592653589793238462643383279502884197;
  double guess = 0.0;
  ...(후략)
  ```

  > 만약 위의 조건을 가지고 while문을 Loop하면 값이 정확하게 맞을 때까지 조건반복 하기 때문에 관계연산자를 최대한 활용하여 연산하는게 좋다.



### 사실과 거짓 True and False

- 표현식에 **True value**를 넣으면 `1`, **False value**를 넣으면 `0`이 출력된다. 

  ```c
  int t_v, f_v;
  t_v = (1 < 2);  // t_v==1
  f_v = (1 > 2);  // f_v==0
  ```

- C언어는 `0` 은 **false**이고, `0` 이외는 **True**로 인식한다.

- `_Bool` 자료형 :

  - 고전 C에서는 정수형(0,1)을 통해 사실 및 거짓을 분류해왔다.

  - 일반적으로 사람들이 `bool` 을 `#define` 하고 있었기 때문에 이것을 표준화 해주었다.

    ```c
    #include <stdbool.h>  //ex.3
    (중략)
    	//ex.3 불리언타입의 표준 include 했을 때
    	bool bt = true;
    	bool bf = false;
    
    	printf("True is %d\n", bt);
    	printf("False is %d\n", bf);
    (후략)
    ```



### for Loop | for 반복문

`while` 문은 진입조건은 있지만 나가는 조건은 모른다. 그래서 **Counting Loop**를 편하게 하기 위해 아래와 같은 값이 필요하다.

1. *Counting Initialization*
2. *Counting check*
3. *Counting change*

- 표준 for 반복문 :

  ```c
  for (size_t i = 0;  //반복할 값 선언 : initialize
       i < length;    //끝 조건 : test
       i++){          //변화방식 선언 : update
      /*statement*/
  };
  ```

  > 원래 한 줄로 선언하는데, 가독성을 위해서 임의로 띄어쓰기를 했다.

- 유의사항 :
  - for문을 카운팅하는 변수는 for문 안에서 변수선언 가능하다.
  - 두 번째 반복문 부터 `change - check` 순으로 계산한다.
  - 1이 아닌것도 더할 수 있다.
  - 문자 타입또한 변경할 수 있다.
  - test 구간에서 다양한 비교연산을 할 수 있다.
  - initialize 구간에서 여러개 변수를 취할 수 있다.
  - 변화방식 선언 구간을 빈칸으로 두고 for문 안에 사용할 수 있다.
  - for문 안에 조건을 전체 생략할 수도 있다.(==while 문과 같아진다.)

### 다양한 대입연산자들

`+=` , `++` 등 다양한 대입연산자들이 있는데 여기서 퍼포먼스 차이를 보기 위해서는 

1. 시간체크
2. 어셈블리어 코드확인 (`debug - disassembly`)

### 콤마 연산자

- 역할 :

  - 여러 개로 구분해주는 Seperator 역할

    ```c
    printf("%d %d\n", n, nsqr)
    ```

  - `;` 와 같은 Sequence point 역할(한 표현식을 끝내는 역할)

    ```c
    int i, j;
    
    i = 1;
    i++, j = i;  //여기서 콤마는 ; 역할을 한다.
    printf("%d %d\n", i, j)
    ```

  - 콤마 연산자로 여러개 값이 있는 경우, 가장 오른쪽 값이 진짜 값이다.

    ```c
    z = ((x = 1), (y = 2));
    ```

    > 여기서 z 표현식의 값은 `2` 이다.



### 탈출조건을 부여하는 루프 | dowhile문

- 비교를 통해 보는 **do-while문** :

  ```c
  int main() {
  	
  	const int password = 337;
  	int i;
  	
  	//기존 코드
  	printf("Enter secret code : ");
  	scanf("%d", &i);
  
  	while (i != password) {
  		printf("Enter secret code : ");
  		scanf("%d", &i);
  	};
  	printf("Good!");
  
  	//종료조건을 체크하는 do-while 문. 무조건 한번은 수행하고 시작하는 형태
  	do
  	{
  		printf("Enter secret code : ");
  		scanf("%d", &i);
  	} while (i != password);
  	printf("Good!");
  
  	return 0;
  }
  ```

  > do를 먼저 선언한 후, while(탈출 조건)을 작성한다. 유의할 점은, do 선언 시 위의 기존코드와 같이 한번 실행한 후 while문이 발동된다는 것이다.



### 중첩반복문 Nested Loop

- 반복문이 여러개 겹친 형태를 말한다.

- C언어에서는 `#define` 형태를 통해 핵심정보 혹은 주의해서 바꿀 정보를 따로 전처리한다.

- 코드 예시 :

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  
  // 핵심 정보 및 자주 바꿀 수도 있는 정보는 따로 #define 가능하다.
  #define NUM_ROWS 5
  #define	FIRST_CHAR 'A'
  #define LAST_CHAR 'K'
  
  int main() {
  	int r;
  	int c;
  
  	for (r = 0; r < NUM_ROWS; ++r) {
  		for (c = FIRST_CHAR; c <= LAST_CHAR; ++c) {
  			printf("%c", c);
  			printf("\n");
  		};
  	};
  
  	return 0;
  ```



### 배열과 런타임 에러 Array and Runtime Error

- 배열 Array : 같은 데이터 형을 여러개 사용할 때, 연결된 메모리를 덩어리로 가져온다면 훨씬 수월하게 사용할 수 있다.

- 런타임 에러 Runtime Error :

  ```c
  //배열 예시
  var_name[메모리크기];
  
  //Out of bound
  printf("%d", var_name[메모리크기+1]);
      
  //compile error
  var_name = 7;
  ```

  > 위의 예시는 공부하면서 기억하기위해 임의로 정리한 예시

  - 메모리 크기보다 큰 인덱스를 넣으면 `Out of bound`
  - 변수만 따와서 임의의 리터럴 상수같은 값을 대입하면 `compile error` 발생한다.(왜나면, 변수명이 주소명 역할을 하기 때문. *나는 파이썬에서 리스트를 담은 변수느낌과 비슷하게 느꼈다.*)



## References

- [홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)
