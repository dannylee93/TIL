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

### 연산자 우선순위와 표현식 트리

