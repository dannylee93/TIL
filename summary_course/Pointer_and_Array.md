## Pointer and Array

### 포인터의 작동원리

데이터의 주소값이란, 해당 데이터가 저장된 메모리의 시작 주소를 의미한다. C언어에서는 이러한 주소 값을 **1byte** 크기의 메모리 공간으로 나누어 표현한다. 예를 들어, `int` 형 데이터는 4바이트의 크기를 가지지만, `int` 형 데이터의 주소값은 시작 주소 1바이트만 가리킨다.

- 포인터 Pointer : 

  메모리공간에 주소값을 저장하는 변수. 간접접근(Indirection), 역참조(Dereferencing), 방향 재지정(Redirection)의 특징을 가지고 있다.

![img](http://tcpschool.com/lectures/img_c_address.png)

- 기본 예제 :

  ```c
  int a = 7;          //변수 선언
  int* ptr = &a;      //포인터 선언
  int* p_ptr = &ptr;  //포인터를 참조
  ```

- 포인더와 연관되는 연산자

  - `&` 주소연산자 : 참조 연산자는 포인터의 이름이나 주소 앞에 사용하여, 포인터에 가리키는 주소에 저장된 값을 반환한다.
  - `*` 참조연산자 : 포인터의 선언 시, 메모리 접근 시 사용.
  
- 주의할 코딩 스타일 :

  ```c
  int* a, b;
  ```

  > `*` 기호를 붙이는 위치는 포인터 변수로, `,` 뒤에 오는 변수는 일반 자료형으로 선언된다.

- 포인터 변수의 크기

  - `x86` : 칩 이름에서 유래한 숫자로 4바이트 주소체계를 사용하며 포인터의 `sizeof()` 연산의 결과는 **4바이트** 이다.
  - `x64` : **8바이트** 주소체계를 사용한다.

- 포인터를 함수의 매개변수로 사용할 때 :

  ```c
  int swap(int* a, int* b);
  
  int main() {
  
  	int a = 123;
  	int b = 456;
  	
  	printf("%p %p\n", &a, &b);
  	swap(&a, &b);
  	printf("%d %d\n", a, b);
  
  } 
  
  int swap(int* a, int* b) {
  
  	int temp = *a;
  	 
  	*a = *b;
  	*b = temp;
  
  	printf("%p %p\n", &a, &b);
  	return a, b;
  }
  ```

  - 함수에서 포인터로 사용하지 않고 일반 변수선언을 하면 **'값에 의한 호출 Call by value'** 형식으로 활용되어 데이터 스왑이 적용되지 않는다.
  - **'주소에 의한 호출 Call by address'** 방식인 포인터로 변경하여 호출 해야한다.



### 포인터와 메모리 

- 배열과 메모리 :

  모든 문제에 하드코딩 할 수 없다. 이 때 배열이 문제를 완화시켜준다.

- 배열 선언 기본형태 :

  ```c
  // 최초 선언
  int arr_name[4] = {2,5,11,8};
  
  //위와 동일한 형태 : 인덱스에 직접 할당할 수 있다.
  int arr_name[4];
  
  arr_name[4] = 2;
  arr_name[4] = 5;
  arr_name[4] = 11;
  arr_name[4] = 8;
  ```

  > 선언과 동시에 초기화도 가능하다. 아래 예시처럼 하나하나 인덱스마다 초기화 하는 경우는 많이 없다.

  - 인덱스에는 음수 혹은 실수는 넣을 수 없다.
  - 배열에도 `const` 조건을 부여할 수 있다.
  - 인덱스를 범위를 넘어 데이터를 넣으려 하면 에러가 나지만 컴파일러는 오류를 잡아주지 않는다.

  <img src="https://github.com/dannylee93/Images/blob/master/Other/arr_form.JPG?raw=true" alt="arr_form" style="zoom:67%;" />

  - `&arr_name[i]`를 호출하면 각 메모리의 첫 주소를 찾아간다. 다음 주소는 자료형의 크기만큼 한칸씩 이동한다.

  <img src="https://github.com/dannylee93/Images/blob/master/Other/arr_form01.JPG?raw=true" alt="arr_form01" style="zoom:67%;" />

  > 'double' 자료형을 선언하면 자료형의 크기만큼 한 인덱스가 메모리를 차지한다.

- 포인터의 산술연산

  포인터에 숫자를 더한다는 것은 주소의 값에 더한다기 보다 선언한 자료형에 맞추어서 건너뛰는 의미에 가깝다.

  ```c
  int main() {
  	//포인터를 산술연산할 때
  	long long* ptr = 0;
  
  	printf("%p %lld\n", ptr, (long long)ptr);
  	ptr += 2;
  	printf("%p %lld\n", ptr, (long long)ptr);
  
  	//포인터끼리 빼기연산
  	double arr[10];  //double은 데이터 하나당 8바이트
  	double* ptr1 = &arr[1], * ptr2 = &arr[3];
  
  	//int* ptr3 = ptr1 + ptr2; // not working
  	int i = ptr2 - ptr1;
  	printf("%lld %lld %d\n", (long long)ptr1, (long long)ptr2, i);
  } 
  ```

  - `-ptr` 혹은 `+ptr` 등의 포인터 앞에 산술연산은 붙일 수 없다.
  - 포인터 끼리 빼기 연산하는 것은 몇칸 건너가 있는지 알려준다.(두 주소간의 거리)

  ```c
  //상수를 붙일 수 있다.
  const int low[12] = { -7,-5,1,7,13,18,22,22,16,9,2,-5 };
  //low[0] = -11;
  
  //배열이 초기값이 없을 때 : 컴파일러는 경고하지 않음
  int not_init[4];  //static 조건(storage class)을 넣으면 '0' 값으로 초기화 되어있음
  for (size_t i = 0; i < 4; i++) {
  	printf("%d\n", not_init[i]);
  };
  
  //배열의 값을 일부만 정의할 때 : 나머지 값은 '0'으로 초기화 함.
  int insuff[4] = { 2,4 };
  for (size_t i = 0; i < 4; i++) {
  	printf("%d\n", insuff[i]);
  	
  //omitting size : 배열의 사이즈 지정 없이 초기값 설정할 때
  const int power_of_twos[] = { 1,2,3,4,5,6,7 };  //[사이즈]를 생략할 수 있다.
  
  printf("%d\n", sizeof(power_of_twos));
  printf("%d\n", sizeof(int));
  printf("%d\n", sizeof(power_of_twos[0]));
  //for 반복문 이용하려면 sizeof()를 이용해야함
  for (int i = 0; i < sizeof power_of_twos / sizeof power_of_twos[0]; i++) {
  	printf("%d\n", sizeof(power_of_twos[i]));
  	};
  
  //Designated initializers : 인덱스 위치 값 지정
  int days[MONTHS] = { 31,28,[4] = 31,30,31,[1] = 29 };
  for (size_t i = 0; i < MONTHS; i++) {
  	printf("%d ", days[i]);
  };
  ```

### 포인터와 배열

메모리의 동적할당을 받아 배열처럼 사용하는데, 대부분 경우 내부구조는 배열과 같지만 포인터를 통해 배열로 사용하기 때문에 중요하다.

- 2차원 배열 : 결국 1차원으로 해석된다.

  ![2Darr](https://github.com/dannylee93/Images/blob/master/Other/2Darr.JPG?raw=true)

  ```c
  int arr[2][3] = { {1,2,3},
  				  {4,7,6,} };
  ```

  > 2차원 배열의 기본형태

- 2차원 배열에서 오른쪽을 안쪽루프로 넣는 이유 : 내부적으로 1차원이기 때문에 스캔순서를 고려한 성능차이가 있다.



### 배열을 함수에 전달하는 방법

- 각 함수마다 배열을 만들면 메모리에 부하가 발생한다. 이에 따라 C언어는 정의된 함수에 배열을 전달할 때, 각 **배열 메모리의 첫 주소를 포인터로 받는다.**

- 코드 예시:

  ```c
  //배열을 함수에 전달할 때는 포인터로 사용되기 때문에 개수정보를 따로 처리해야된다.
  double average(double *arr, int n) {
  	printf("Size = %zd in function average\n", sizeof(arr));
  
  	double avg = 0.0;
  	for (int i = 0; i < n; ++i) {
  		avg += arr[i];
  	}
  	avg /= (double)n;
  
  	return avg;
  }
  ```

  > 인덱스 정보를 따로 처리한다. [ ] 는 없어도 상관 없지만 배열임을 알려주는 용도로는 사용할 수 있다. 또한, '*' 기호를 사용하여 알려줄 수도 있다.(둘 다 동시 사용은 못함)

### 포인터 관련 연산 총정리

- Assignment : 

  ```c
  int arr[5] = { 100, 200, 300 , 400 , 500 };
  int* ptr1, * ptr2, * ptr3;
  
  //Assignment
  ptr1 = arr;  //최초 인덱스 외에 주소를 참조하려면 & 붙여야함
  ```

  > 포인터에 배열의 주소를 넣을 수 있다. 일반 변수는 `&var_name` 으로 선언 해야하지만, 배열은 바로 선언할 수 있다.

- Taking a pointer address : 

  ```c
  printf("%p %d %p\n", ptr1, *ptr1, &ptr1);
  ```

  - `*` 기호를 붙이면 **역참조 Dereferencing** 이 되어 해당 값이 나온다.

- Address-of operator `&` :

  ```c
  ptr2 = &arr[2];
  printf("%p %d %p\n", ptr2, *ptr2, &ptr2);
  ```

- Adding an integer from a pointer : 

  ```c
  ptr3 = ptr1 + 4;
  ```

  > 4바이트가 4개 저장될 공간만큼 값을 더한다.

- Differening : 

  ```c
  printf("%td\n", ptr3 - ptr1);
  ```

  > `%td` 는 포인터의 차이 값을 설명할 때 사용한다.

- 증감연산자 사용

  ```c
  ptr1++;  //ptr = ptr + 1
  ptr1--;
  --ptr1;
  ++ptr1;
  ```

- 자료형의 타입이 다른 포인터 끼리 비교연산 : 가능은 하지만 최대한 맞춰주는 것이 좋고, 자료형을 맞추거나 혹은 `(void*)` 를 사용할 수 있다.

### Const 조건과 배열&포인터

- 코드 예시 :

  ```c
  const double PI = 3.14159;  // 일반 변수를 상수로 만듦
  //PI = 123;
  
  const int arr[5] = { 1,2,3,4,5 };
  //arr[1] = 123;
  
  const double arr2[3] = { 1.0, 2.0, 3.0 };
  //arr2[0] = 100.0;
  
  const double* pd = arr2;
  //*pd = 3.0;       // pd[0] = 3.0; arr2[0] = 3.0;
  //pd[2] = 1024.0;  // arr2[2] = 4.0;
  
  printf("%f", pd[2]);
  
  //그래도 포인터의 증감연산자는 가능하다.
  printf("%f %f", pd[2], arr2[2]);
  pd++;
  printf("%f %f", pd[2], arr2[2]);
  ```

  - 포인터에 배열주소를 넣은 후, 역참조 후 값을 넣으면 포인터를 배열처럼 사용할 수 있다.
  - 주의사항 : `const`로 배열 값을 고정한 후, 포인터로 값을 변경할 수 있다.

### 이중 포인터의 작동원리

<p align = 'center'><img src="https://github.com/dannylee93/Images/blob/master/Other/double_pointer.JPG?raw=true" style="zoom:67%;" /></p>

위 사진처럼 **주소값의 주소를 저장**하는 방법을 이중 포인터라고 한다. 

- 1차원 배열 2개를 포인터로 2차원 배열로 변환 :

  ```c
  //definition
  int arr0[3] = { 1,2,3 };
  int arr1[3] = { 4,5,6 };
  
  //포인터를 넣을 수 있는 공간을 두개를 확보하며 2차원 포인터 배열 형성
  int* ptarr[2] = { arr0, arr1 };
  ```

- 2차원 배열처럼 사용하는 이중 포인터

  ```c
  //마치 2차원 배열처럼 사용할 수 있다.
  for (int j = 0; j < 2; j++) 
  {
  	for (int i = 0; i < 3; i++) 
      {
  		//역참조 연산자 사용도 가능, 이중 포인터 처럼도 사용할 수 있다.
  		printf("%d(==%d, %d) \n", ptarr[j][i], 
  								 *(ptarr[j] + i), 
  								 *(*(ptarr + j) + i));
  	};
  };
  ```

- 포인터의 배열과 진짜 배열의 차이, 출력방식

  ```c
  //포인터의 배열과 진짜 배열의 차이
  int arr[2][3] = { {1,2,3},{4,5,6} };
  int* parr[2];  //8바이트 공간에 포인터 공간 할당
  parr[0] = arr[0];
  parr[1] = arr[1];
  
  printf("%p\n", &parr[0]);  //포인터 자체의 주소
  printf("%p\n", parr[0]);  //가리키는 주소
  printf("%p\n", arr);  //가리키는 주소 ..
  printf("%p\n", &arr[0]);
  printf("%p\n", arr[0]);
  printf("%p\n", &arr[0][0]);
  ```

- 이중포인터 관련 참조 사항 : 

  ```c
  //arr2d points to arr2d[0] (not arr2d[0][0])
  printf("%u\n", (unsigned)*arr2d);
  printf("%u\n", (unsigned)&arr2d[0]);
  printf("%u\n", (unsigned)&arr2d[0][0]);
  printf("%f %f\n", arr2d[0][0], **arr2d);  //이중포인터로 역참조 한 값과 같다.
  
  /*Pointers to Multidimesional Arrays*/
  float(*pa)[4]; //4개의 원소를 가진 하나의 싱글 포인터
  float* ap[2];  //두개의 포인터를 가진 하나의 배열
  
  printf("%zu\n", sizeof(pa));  //4
  printf("%zu\n", sizeof(ap));  //8
  printf("\n");
  ```

- 다중 포인터 관련 참조 사항 :

  ```c
  //prototype : sum1,sum2는 함수정의 생략
  int sum2d_1(int ar[ROWS][COLS]);
  int sum2d_2(int ar[ ][COLS], int row);  //가장 왼쪽에 있는 인덱스만 생략가능하고 나머지는 지정해줘야함
  int sum2d_3(int* ar, int row, int col);  //동적할당을 사용하기 위한 방식
  ```

### 포인터와 2차원 배열

```c
int arr[2][3] = {{1,2,3},
				 {4,5,6}};
```

![2Darr](https://github.com/dannylee93/Images/blob/master/Other/2Darr.JPG?raw=true)

- 포인터 주소 표시 방법

  - `arr`  : 

    == `arr[0]` == `&arr[0]` == `&a[0][0]`  !=  `a[0][0]` (마지막은 주소가 아니라 값을 표현)

  - `&arr[0][1]` :

    == `&arr[0][1] + 1`

  - `arr + 1` :

    ==`&arr[1]` == `&arr[0] + 1` == `&a[1][0]` != `a[1][0]`

  - `a[1][2]` :

    == `*(*(arr+1)+2)`

  

## 기타 참고사항

### 복합 리터럴 Compound Literal

```c
// symbolic 하지 않은 리터럴 상수
3;
3.14f;

//배열 과 배열을 복합리터럴로 표현
int b[2] = { 3,4 };
(int[2]) {3, 4};

//배열 정의 없이 함수 파라미터에 적용 가능하다.
printf("%d\n", sum_2d((int[2][COLS]) { {1, 2, 3, 4}, { 5,6,7,8 } }, 2));
```



## References

- [홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)
- [TCP SCHOOL](http://tcpschool.com/c/intro)



