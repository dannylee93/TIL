# Storage Classes, Linkage and Memory management

> 사용 방법에 따라 달라지는 메모리 의 저장공간에 대해 정리하고, 파일 내외로 변수와 함수를 연결해서 사용하는 방법, 동적할당에서 메모리 관리를 정리

### Overview

| 저장공간 분류(Storage-classes)                 | 메모리 위치(Memory Segment) | 지속기간(Duration) | 영역(Scope) | 연결상태(Linkage)            | 선언방법(How Declared)         |
| ---------------------------------------------- | --------------------------- | ------------------ | ----------- | ---------------------------- | ------------------------------ |
| 자동(Automatic)                                | 스택 Stack                  | 자동 결정          | 블록 안     | X                            | 블록 안                        |
| 레지스터(Register)                             | 레지스터 또는 스택          | 자동 결정          | 블록 안     | X                            | `register` 키워드 사용         |
| 고정적, 내부연결(Static with Internal linkage) | 데이터 또는 BSS             | 고정               | 파일 안     | 번역 단위 내부               | 모든 함수 밖에서 `static` 사용 |
| 고정적, 외부연결(Static with External linkage) | 데이터 또는 BSS             | 고정               | 파일 안     | 번역 단위 외부로도 연결 가능 | 모든 함수 밖                   |
| 고정적, 연결없음(Static with No linkage)       | 데이터 또는 BSS             | 고정               | 블록 안     | X                            | 블록 안에서 `static`           |
| 할당 메모리(식별자 없음)                       | 힙 Heap                     | 프로그래머 결정    | NA          | NA                           | OS에 요청                      |

### 객체와 식별자 Object and Identifiers

실제 메모리에 값을 저장하고 공간을 가지고 있는 것을 **객체 Object** 라 표현하며, 변수/함수/매크로/엔터티 등의 이름을 가지고 있는 것을 **식별자 Identifier** 라고 한다.

- 코드 예시 :

  ```c
  int var_name = 3;
  ```

  > 'var_name' 은 변수의 이름으로 식별자 역할을 하며 이 변수의 메모리 공간은 객체라고 한다.

  ```c
  * ptr = 1;
  ```

  > 포인터는 식별자이지만, 포인터를 통해 역참조하는 것은 식별자가 아니며, Object를 지명(Designate) 하는것이라고 표현한다.

  ```c
  arr[0];
  ```

  > 'arr' 배열의 0번 째 공간을 찾는 표현식 Expression 이다.

- 참고사항 :

  - 식별자는 **영역 Scope**를 가진다.
  - Object는 저장공간의 지속기간을 가진다.
  - 변수와 함수는 `Linkage`가 있다.



### 변수의 영역(Scope)와 연결상태(Linkage), 객체의 지속기간(Duration)

- 영역(Scope) : 해당 블록(Indenting) 안에 정의된 영역에서만 사용할 수 있다.

- 연결상태(Linkage) : 여러개의 파일에 대해 작동하는 것이다.

  - 파일 Scope에 있는 변수는 다른 파일에서 `extern` 조건을 부여하며 사용할 수 있다.

    ```c
    extern int var = 0;
    ```

  - 앞에 `static` 조건을 붙이면 해당 Scope 안에서만 사용할 수 있다.

- 객체의 지속기간(Duration) : 메모리의 지속기간을 지칭 한다.

  - Static : 선언 당시 파일의 처음과 끝
  - Automatic : 보통 일반적인 지역변수 지칭
  - Allocated : 동적할당 관련
  - Thred : 멀티쓰레딩 관련



### 변수의 다섯가지 분류

위의 Overview 표에서 저장공간 분류(Storage-classes) 에 대한 정리 내용이다.

- **자동 변수 Automatic Variable**

  - 일반적인 지역변수를 지칭하며, 블록`{ }` 이나 파일 안에서 사용한다. Linkage는 없다.
  - `aut` 조건을 변수 선언 당시 붙일 수 있지만, 생략 가능하다.
  - 선언 당시 **초기값** 을 꼭 선언 해주어야 좋다.
  - 주의사항 : 큰 영역에서 한번 선언 후, 작은 영역에서 똑같은 것을 한번 더 선언하면 **name hidding** 문제가 발생한다.

- **레지스터 변수 Register Variable**

  ```c
  register int r; 
  //int* ptr = &r;  //레지스터 공간에는 주소연산자를 사용할 수 없다.
  ```

  > 자료형 앞에 'register' 명령 추가한다.

  - 레지스터는 메모리 공간이 아닌 CPU구조의 일부이며, 특정 어딘가에 잠시 저장하고 바로 활용할 때 사용하기 때문에 빠른 특징이 있다.
  - 레지스터 공간은 주소연산자를 사용할 수 없다. 레지스터는 메모리와 CPU사이에서 bus 구조를 통해서 데이터를 주고 받기 때문이다.

- **블록 영역의 정적변수와 지역변수 비교**

  ```c
  //메모리의 스택에 저장
  void count()
  {
  	//지역변수 : 함수 호출마다 초기화 된다.
  	int cnt = 0;  
  	printf("count = %d %lld\n", cnt, (long long)&cnt);
  	cnt++;
  }
  
  //정적메모리를 사용하는 공간에 따로 저장
  void static_count()
  {
  	//정적변수 : 초기화는 한번만 된다.
  	static int cnt = 0;
  	printf("count = %d %lld\n", cnt, (long long)&cnt);
  	cnt++;
  }
  ```

  > 정적변수는 count가 올라가지만 스택에 저장된 지역변수는 매번 초기화 되기 때문에 계속 0을 출력한다.

- **정적변수의 External Linkage**

  번역 단위(같은 프로젝트 내) 파일 외부로도 연결 가능하다.(각 파일들을 컴파일하고, 객체.obj를 형성하면서 링킹하는 순으로 실행한다.)

  - 파일 Scope 안에서, 한곳에서만 초기화 하자.

  - 오해가 없게 프로그래밍 하기 위해서는 초기값 설정하는 Defining declaration 보다는 Referring declaration에서 `extern` 조건을 넣자

  - 정적변수는 초기값을 임의로 항상 넣기

    ```c
    // 정적변수는 알아서 초기값을 넣지만 임의로 넣어주는 것을 추천
    int g_int =0;  
    double g_arr[1000] = {0.0, };
    ```

  - 함수 External Linkage (기본적으로 함수 선언은 extern으로 생각한다.)

    ```c
    extern void fun_sec();
    ```

  - name hiding 방지 하기 위한 extern 조건 부여

    ```c
    extern int g_int;
    extern double g_arr[];
    ```

- **정적변수의 Internal Linkage**

  `static` 조건은 블록영역 혹은 파일 영역 등 변수가 선언된 위치 외에 사용하지 못한다.

### 메모리 동적할당 Dynamic Storage allocation

동적할당 메모리는 포인터만 가져오고 인식자가 없다. 또한 힙 Heap 이라는 공간에 저장된다. 필요한 메모리의 크기를 미리 알 수 없고, 런타임(실제 실행) 때 사용하는 상황에서 사용한다. 이렇게 런 타임에 메모리를 할당받는 것을 메모리의 동적 할당(dynamic allocation)이라고 한다.

> 데이터 영역과 스택 영역에 할당되는 메모리의 크기는 컴파일 타임(compile time)에 미리 결정되지만, 힙 영역의 크기는 프로그램이 실행되는 도중인 런 타임(run time)에 사용자가 직접 결정.

<p align='center'><img src="https://github.com/dannylee93/Images/blob/master/Other/Heap.JPG?raw=true" style="zoom:67%;" /></p>

- **선행조건(헤더) :** 

  ```c
  #include <stdlib.h>	// malloc(), free()
  ```

  - `malloc()` : 메모리에 공간을 할당 해달라고 요청(인자 : 메모리 사이즈)
  - `free()` : 할당된 메모리를 초기화(Deallocate)

- **주의사항 :**

  블록 Scope 안에 있을 때, 해당 영역을 벗어나면 Heap에 메모리는 남아있지만 포인터 변수를 잃어버리는 현상이 발생한다.

- **원형 :**

  ```c
  #include <stdlib.h>
  
  void *malloc(size_t size);  
  ```

- **사용 방식 :**

  ```c
  double* ptr = NULL;
  
  //(double*) 이라는 표현식은 double 자료형 포인터로 캐스팅 하는 역할
  ptr = (double*)malloc(30 * sizeof(double));
  ```

  > 포인터를 정의(NULL로 초기화까지)한 후, `malloc()` 활용.

- **포인터를 사용하면 반납하는 과정을 꼭 하자**

  ```c
  //포인터를 다 사용했으면 반드시 반납하기
  free(ptr);
  ptr = NULL;
  ```

- **메모리 누수(Leak)와 free()의 중요성**

  `free()` 를 사용하지 않으면, 동적할당된 포인터를 복사해서 쓸 수도 있는데, 이 때 `free()`를 쓰면 런타임 에러가 난다.(집주소의 주인이 이사가도 주소만 남는 상황과 유사.)

  또한, 계속 동적할당 받기만 하면 메모리 누수가 심각하게 커진다.

### 동적할당 메모리 배열처럼 사용하기

- 코드 예시 :

  - 1차원 배열

    ```c
    int n = 3;
    int* ptr = (int*)malloc(sizeof(int) * n);
    if (!ptr) exit(1);
    
    ptr[0] = 123;
    *(ptr + 1) = 456;
    *(ptr + 2) = 789;
    printf("%d\n", *ptr);
    
    free(ptr);
    ptr = NULL;
    ```

    > 1차원 배열을 사용했을 때는 일반적으로 포인터 사용하는 방법과 유사하다.

  - 2차원 배열

    ```c
    int row = 3, col = 2;
    int(*ptr2d)[2] = (int(*)[2])malloc(sizeof(int) * row * col);
    //int(*ptr2d)[cols] = (int(*)[cols])malloc(sizeof(int) * row * cols);  //VLA 지원 안해줌
    if (!ptr2d) exit(1);
    
    for (int r = 0; r < row; r++) {
        for (int c = 0; c < col; c++)
            ptr2d[r][c] = c + col * r;
    };
    
    for (int r = 0; r < row; r++) {
        for (int c = 0; c < col; c++)
            printf("%d ", ptr2d[r][c]);
        printf("\n");
    };
    printf("\n");
    ```

    > 2차원 배열 포인터를 동적할당으로 부여할 때는 맨 뒤 칼럼을 명시해주어야 하는데, 컴파일러는 심볼릭 상수를 받지 않는다. 그래서 상수를 넣어야하는데 그렇게 되면 동적할당을 사용하는 의미가 퇴색된다.

  - 3차원 배열(n차원) : 핵심은 1차원화 하는 것이다.

    ```c
    // 2차원을 1차원으로 생각할 때 인덱스 계산 패턴
    row = 3, col = 2
    
    (r, c)
    
    2D
    (0, 0) (0, 1)
    (1, 0) (1, 1)
    (2, 0) (2, 1)
    
    1D
    (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1)
    0      1      2      3      4      5      = c + col * r
        
    // 
    row = 3, col = 2, depth = 2
    
    (r, c, d)
    
        3D 
        -------------------
        (0, 0, 0) (0, 1, 0)
        (1, 0, 0) (1, 1, 0)
        (2, 0, 0) (2, 1, 0)
        -------------------
        (0, 0, 1) (0, 1, 1)
        (1, 0, 1) (1, 1, 1)
        (2, 0, 1) (2, 1, 1)
        -------------------
    
    1D
    (0, 0, 0) (0, 1, 0) (1, 0, 0) (1, 1, 0) (2, 0, 0) (2, 1, 0) (0, 0, 1) (0, 1, 1)	(1, 0, 1) (1, 1, 1) (2, 0, 1) (2, 1, 1)
    0         1         2         3         4         5         6         7         8         9         10        11
        = c + col * r + (col*row) * d
        = 1 + 2 * 1 + (3*2) * 1 = 1 + 2 + 6 = 9
    
    3D
    row, col, depth, height
    (r, c, d, h)
    index = c + col * r + (col*row) * d + (row * col * depth) * h
    ```

    ```c
    //3차원 배열과 동적할당 활용해보기
    	int rows = 3, cols = 2, depth = 2;
    	int* ptr = (int*)malloc(sizeof(int) * (rows * cols * depth));
    	if (!ptr) exit(1);
    	
    	for (int d = 0; d < depth; d++) {
    		for (int r = 0; r < rows; r++)
    			for (int c = 0; c < cols; c++)
    				ptr[c + (cols * r) + (cols * rows) * d] = c + (cols * r) + (cols * rows) * d;
    	};
    
    	//값 
    	for (int d = 0; d < depth; d++) {
    		for (int r = 0; r < rows; r++) {
    			for (int c = 0; c < cols; c++)
    				printf("%d ", *(ptr + c + (cols * r) + (cols * rows) * d));
    			printf("\n");
    		};
    	};
    ```

### calloc() 과 realloc()

`calloc()` 과 `malloc()` 은 실제 실행결과에 있어서 큰 차이가 없으나, `calloc()` 은 값을 0 으로 전부 초기화까지 해준다.

`realloc()` 동적할당으로 메모리를 한번 받아왔는데, 추후에 사이즈를 증/감 하고싶을 때 사용한다.

- realloc() 원형

  ```c
  void *__cdecl realloc(void *_Block, size_t _Size)
  ```

  - `_Block` : 메모리 블럭(이전에 받은 주소명)을 의미한다.
  - `_size` : 새로 할당 받고 싶은 사이즈

  ```c
  int* ptr2 = NULL;
  ptr2 = (int*)realloc(ptr, n * sizeof(int));
  
  printf("%p %p\n", ptr, ptr2);
  printf("%d\n", ptr[0]);
  ```

## 기타

- 타입한정자 Type Qualifiers
- 멀티 쓰레드

## References

- [홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)
- [TCP SCHOOL](http://tcpschool.com/c/intro)

