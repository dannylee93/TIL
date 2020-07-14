## Operator, Expression, Statement

### 반복 루프 Loop

고전 방식으로는 `선언 - goto` 방식을 사용했으나 현재는 `while` 문을 주로 사용중한다.

```c
while(true)
{
	exp
}
```



### 연산자와 용어 설명

- 연산자(Operator) 및 피연산자(Operand)

  ```c
  i = i + 1
  ```

  여기서 `i` 와 `i+1`은 연산자라 하며, R-Value 에서 `i` 와 `1`은 피연산자라고 한다.

- 기본 연산자 : 

  - `=`  : 대입 연산자(등호 아님)
  - `+`, `-`, `*`,  `/`  : 덧셈, 뺄셈, 곱셈, 나눗셈

- 관련 용어 :

  - Data object : 데이터가 메모리 안에 있다면, 그것을 **object** 라고 부른다.
  - L-value(Object locator value) : object의 메모리 공간을 대표하는 변수명(임시적으로 R-value 처럼 사용할 수도 있다. 위의 예시 중 `i` 처럼)
  - R-value(Value of an expression) : 표현식의 값을 말하며, 계산이 끝나면 사라진다. (`const` 조건을 부여할 시 수정 불가능해진다.)

- 덧, 뺄셈 연산자 관련 :

  - 이항 연산자 Binary operator

    ```c
    //피연산자가 2개 있으며 값은 1
    3 - 2
    ```

  - 단항 연산자 Unary operator

    ```c
    //피연산자가 1개이며, 값은 -16
    -16
    ```

  - 복합

    ```c
    //예시
    -(12-11)
    ```

- 곱셈 연산자 : *[복리계산 연습 코드 참고]()*

- 나머지 연산자 : `%`

  ```c
  13 % 5 
      // values == 3
  ```

- 증가&감소 연산자 : `++` , `--`

  - 변수 앞,뒤에 붙을 수 있다.(하지만 결과가 달라진다.)

  - 예시 코드 :

    ```c
    	int count = 0;
    	
    	//0123456789
    	while (count < 10)
    	{
    		printf("%d", count);
    		count++;
    	};
    
    	//123456789
    	while (++count < 10)
    	{
    		printf("%d", count);
    		//count++;
    	};
    
    	//012345678910
    	while (count++ < 10)
    	{
    		printf("%d", count);
    		//count++;
    	};
    ```

    > 어디 위치에 붙이느냐에 따라 결과가 달라진다.

### 연산자 우선순위와 표현식 트리

**연산자 우선순위** : 아래 표 외에도 많이 있으나 결합법칙(즉, 어디 위치부터 순서대로 계산하는 지)에 유의 하기

|            연산자            |    결합법칙     |
| :--------------------------: | :-------------: |
|              ()              | 왼쪽에서 오른쪽 |
| + - (단항 <sub>unary</sub>)  | 오른쪽에서 왼쪽 |
|             * /              | 왼쪽에서 오른쪽 |
| + - (이항 <sub>binary</sub>) | 왼쪽에서 오른쪽 |
|              =               | 오른쪽에서 왼쪽 |

**표현식 트리** : 연산자 우선순위에 기반한 계산 순서를 트리형식으로 표현한 도표이다.



### 표현식과 문장 Expressions and Statements

- **표현식**은 연산자를 통해 만들어진 조합이며, **문장**은 표현식으로 만들어진 하나의 실행가능한(Excutable) 독립적인 조합이다.

- 표현식은 연산자를 통한 표현식과 값이 있다.

  | 표현식 |         값          |
  | :----: | :-----------------: |
  | 2 > 1  | 1<sub>(true)</sub>  |
  | 2 < 1  | 0<sub>(false)</sub> |

- 표현식에서 Sequence Point(값을 언제 제안하는가)를 유의해야한다.

- 유의할 예시 : 

  ```c
  y = (4 + x++) + (6 + x++);
  ```

  - 한 문장안에 2가지 증감표현을 쓰는 것은 좋지 않다.
  - 둘다 Full Expression이 아니다.
  - 컴파일러에 따라 값이 달라질 위험이 있다.

### 자료형 변환 Type Conversions

자료형은 프로그래밍을 하면서 유동적으로 데이터의 자료형을 바꾸어 주는 것을 말한다.

1. **형 확장 Promotion in assignment :** 작은집에서 큰 집으로 들어가면 문제가 없는 것과 같다

   ```c
   float f = 1.23f;
   double d = 1.22;
   
   d = f + d;  // double 타입 안에 float와 double을 연산해도 문제 없음
   ```

2. **형 축소 Demotion in assignment :** 반대로 큰집에서 작은집에 들어가려하면 데이터를 손실할 위험이 있다.

   ```c
   float f = 1.23f;
   double d = 1.22;
   
   f = f + d;  // float 타입 안에 float와 double을 연산하려하면 절삭하려 한다.
   ```

3. **Ranking of types in operations :** 자료형 변환은 변환 계급에 따라 순위를 가지고 있다.

   ![conversion rank](http://thumbnail.egloos.net/460x0/http://pds24.egloos.com/pds/201207/19/45/a0077645_5006e812ebb96.png)

   > 주로 bit 를 많이 사용할 수록 높은 계급 값을 가지고 있는 것을 알 수 있다.

4. 자료형의 묵시적 변환과 명시적 변환

   - **묵시적 형변환 Implicit type conversion :** 위의 덧셈 예시와 같이 연산과정에서 자연스럽게 변환 계급 순위에 따라 변경되는 것

   - **명시적 형변환 Explicit type conversion :** 프로그래머가 형 변환자(cast)를 사용하여 강제적으로 형 변환을 하게 하는 경우이다.

     ```c
     (int)myFloat;
     (float)myInt;
     ```

### 함수의 인수와 매개변수

- 인수 Argument : 정의된 함수에서 값(values) 역할을 함
- 매개변수 Parameter : 변수(variables)역할을 함

## References

- [홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)
- http://kjlife.egloos.com/m/2333275

