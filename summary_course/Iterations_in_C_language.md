## Iterations in C language | 반복문 

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



