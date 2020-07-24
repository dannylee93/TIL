# String Functions

> `\0`(null character) : 문자열의 끝을 알려주는 Sequence

### 문자열 정의 방법

문자열을 정의하는 방법에는 여러 방법들이 있다. 함수에 직접 리터럴로 넣을 수 있고, 배열로도 넣을 수 있다.

- 코드 예시 : 

  - 문자열 정의

    ```c
    char words[MAXLENGTH] = "A string in an array";
    char* pt1 = "A pointer to a string.";
    ```

  - `puts()` 함수에 리터럴로 넣을 수 있다.

    ```c
    //puts() add '\n' at the end
    puts("Puts() add a new line at the end: ");
    ```

    > puts() 함수는 Escape Sequence가 디폴트로 있다.

  - Symbolic string contant

    ```c
    //#define MESSAGE "A symbolic string contant"
    puts(MESSAGE);
    ```

    > 전처리기를 사용해서 기호적 상수처럼 넣을 수 있다.

  - 변수의 할당된 메모리 만큼 입력하지 초기화 하지 않으면 `Warning`

    ```c
    //#define MAXLENGTH 81
    puts(words);  
    ```

    > 경고 : Maxlength 만큼 데이터가 초기화 되지 않아서.

  - 포인터를 통해 문자열 출력

    ```c
    puts(pt1);
    ```

    > 포인터에 담은 문자열은 해당 문자열 그대로의 주소를 찾아간다.

  - 문자열 고쳐보기

    ```c
    //ok : 문자열을 담은 배열은 인덱스를 활용해서 고칠 수 있다.
    words[3] = 'p';
    
    //Runtime Error : 포인터를 담은 주소는 문자열 그대로를 주소에 저장 >> 오류
    pt1[8] = 'A';  
    ```

    > 포인터라는 읽기 전용 메모리에 저장된 데이터 값을 바꾸려고 하면 운영체제가 오류라고 인식한다.

  - 문자열을 담은 배열을 `int` 로 출력해보기 

    ```c
    //문자열 
    const char m1[15] = "Love you!";
    
    for (int i = 0; i < 15; i++)
    {
        printf("%d ", (int)m1[i]);
    };
    printf("\n");  
    ```

    > null character 까지 숫자가 출력되고 나머지 공간은 0을 출력

  - 문자 하나씩 배열로 저장하기

    ```c
    const char m2[15] = { 'l','o','v','e',' ', 'y','o','u','!' ,'\0' };
    
    for (int i = 0; i < 15; i++)
    {
    	printf("%d ", (int)m2[i]);
    };
    printf("\n");
    ```

    - 주의사항 :
      1. `" "` : 곁 따옴표는 문자 여러개를 저장할 수 있고, `\0` (null character)를 포함한다.
      2. `' '` : 홑 따옴표는 문자 한개씩 저장할 수 있고, 마지막에 `\0` 를 포함해야한다.

  - 배열과 포인터 개념 <> 문자열

    ```c
    //배열, 포인터 개념과 문자열
    char truth[10] = "Truth is ";
    if (truth == &truth[0]) puts("1. true!");
    if (*truth == 'T') puts("2. true!");
    if (*(truth + 1) == truth[1]) puts("3. true!");
    if (truth[1] == 'r') puts("4. true!");
    ```



### 메모리 레이아웃

<img src="http://tcpschool.com/lectures/img_c_memory_structure.png" alt="메모리 구조" style="zoom:67%;" />

> [tcpschool.com](http://tcpschool.com/c/c_memory_structure) 참고하기

1. *코드(code) 영역*

2. *데이터(data) 영역*

3. *스택(stack) 영역*

4. *힙(heap) 영역*

프로그램이 실행되기 위해서는 먼저 프로그램이 메모리에 로드 되어야 하며, 사용할 변수들을 저장할 메모리도 필요하다. 이를 위해 운영체제는 다양한 메모리 공간을 제공하고 있으며 위와 같이 4가지의 공간을 부여한다.

### 문자열의 배열

1. 포인터가 여러개 있는 배열 : 해당 문자열의 위치를 저장한다.

   ```c
   const char* mythings[5] = {
   		"Dancing in the rain", "Banana", "Strawberry", "Grape", "Lemon"};
   ```

2. 개별 Stack으로 따로 메모리 저장을 한 배열

   ``` c
   char yourthing[5][40] = {
       "Studying the C++ language",
       "Eating",
       "Watching Netflix",
       "Walking around till dark",
       "Deleting spam emails"
   };
   ```

- 각 문자열의 위치를 포인터로 저장한 배열은 단일 문자열 포인터와 주소값이 같으며, 따로 메모리에 스택한 배열은 문자열 포인터와 주소값이 다르다.

  ```c
  const char* temp1 = "Dancing in the rain";
  const char* temp2 = "Studying the C++ language";
  
  //문자열의 위치를 저장한 포인터 : 같은 주소값
  printf("%s %u %u\n", mythings[0], (unsigned)mythings[0], (unsigned)temp1);
  
  //개별 stack에 메모리 저장한 배열 : 다른 주소값
  printf("%s %u %u\n", yourthing[0], (unsigned)yourthing[0], (unsigned)temp2);
  ```



### 문자열의 다양한 Input 함수

- 주의사항 :

  문자열을 입력 받을 때는 **저장할 공간을 미리** 만들고 받아야 한다. 변수를 저장할 때, **초기화** 과정 또한 필요하다.

- 문자열 정의

  ```c
  //첫 번째 포인터 라인처럼 크기를 할당하지 않으면 Runtime Error 발생
  char* name = "";
  char name[128];
  int result = scanf("%s", name);
  ```

  1. 문자열을 담을 포인터 
  2. 따로 메모리에 스택하는 배열 변수
  3.  문자열을 입력받는 `scanf()` 함수

- `gets()` 함수와 `gets_s()`

  ```c
  char words[5] = "";  //값 초기화 과정
  
  //gets()
  gets(words);  //메모리공간보다 크면 런타임 에러
  //gets_s()
  gets_s(words, sizeof(words));  //메모리공간보다 크면 런타임 에러
  printf("START\n");
  
  //입력받은 문자열 출력해보기
  printf("%s", words);
  puts(words);  //puts()는 \n 이 포함되어 있다.
  
  printf("END\n");
  ```

  > gets()의 인자는 배열의 포인터 대표 주소값이다. gets_s() 함수는 메모리 공간의 크기를 인자로 받는다.

- `fgets()` and `fputs()`

  ```c
  char word2[STRLEN] = "";
  fgets(word2, STRLEN, stdin);  //fgets는 \n을 없애지 않는다.(입력 후 엔터칠 때 생김)
  
  /*fgets 후 생성되는 '\n' 을 '\0' 으로 변경해보기*/
  int i = 0;
  while (word2[i] != '\n' && word2[i] != '\0')
  {
  	i++;
      if (word2[i] != '\n')
      	word2[i] != '\0';
  };
  
  //입력받은 문자열 출력해보기
  fputs(word2, stdout);
  fputs("END", stdout);  //문자 그대로 출력
  ```

  - `fgets()` 의 세 가지 파라미터 : (`배열 포인터`, `최대공간`, `FILE:파일입출력 혹은 stdin(콘솔입력)`)
  - `fgets()` 는 언제 입력이 끝날지 모르는 것을 염두에 두고있다.(파일 관련 입력함수라서)

- `scanf()` 방법

  ```c
  char str1[6], str2[6];
  int count = scanf("%5s %5s", str1, str2);  //null character 고려해서 입력공간 만들기
  
  //메모리 공간 초과하면 런타임 에러
  int count = scanf("%6s %6s", str1, str2);  
  printf("%s | %s \n", str1, str2);
  ```

  > `%5s`는 null character 를 고려한 입력 제한 값이다.



### 문자열의 다양한 Output 함수

- `puts()` : 줄 바꿈(`\n`) 이 디폴트로 있다.

  ```c
  //#define TEST "A string from #define"
  
  char str[60] = "String array initialized";
  const char* ptr = "A pointer initialized";
  
  puts("String without \\n");
  puts("END");
  puts(TEST);  
  puts(TEST + 5);   //해당 인덱스 위치부터 null character 까지 출력된다.
  puts(&str[3]);
  puts(ptr + 3);
  ```

  - 문자열 그대로도 입력 가능하며, 전처리기를 통해 정의한 것들도 함께 출력할 수 있다.
  - `puts(str[3]);` 는 포인터 주소값이 아니기 때문에 에러가 난다.

- string without `\0`

  ```c
  char str2[] = { 'H', 'I', '!' };
  puts(str2);   //null character가 없어서 경고
  ```

- `puts()` and `fputs()`

  ```c
  char line[6];
  while (fgets(line, 6, stdin)) {
  	puts(line);
  };
  ```

  > fgets() 함수는 배열의 메모리공간과 입출력 방식을 인자로 받는다.  해당 크기보다 초과되는 것은 버퍼에서 따로 출력하며, `ctrl + z` 를 누르면 종료된다.

- `printf()` 

  ```c
  char input[100] = "";
  int ret = scanf("%10s", input);
  printf("%s\n", input);
  ret = scanf("%10s", input);
  printf("%s\n", input);
  ```

  > 10글자 제한을 초과하는 글자는 버퍼 공간에 있다가 다음에 출력된다.



### 문자열 관련 함수

- 문자열의 길이 `strlen()`

  ```c
  char msg[] = "Just,"" Do It!";
  puts(msg);
  printf("Length : %d\n", strlen(msg));
  
  fit_str(msg, 4);
  ```

  > 문자열의 끝을 알리는`\0`은 strlen 함수에서 포함하지 않는다. `fit_str` 함수는 해당 개수 만큼 문자를 출력한다.  

- Concatenation : `strcat()` and `strncat()`

  ```c
  char str1[100] = "First string";
  char str2[] = "Second string";
  
  strcat(str1, ", ");
  strcat(str1, str2);
  strncat(str1, str2, 2);  //두번째 문자열을 n개 concat
  ```

  > 결과값이 누적이 되는 이유는 모름 ㅠ.  `strncat()` 함수는 개수 제한이 가능하다.

- Compare : `strcmp()` and `strncmp()`

  ```c
  printf("%d\n", strcmp("A", "A"));                     //0
  	printf("%d\n", strcmp("A", "B"));				  //-1
  	printf("%d\n", strcmp("B", "A"));				  //1
  	printf("%d\n", strcmp("HELLO", "HELLO"));         //0
  	printf("%d\n", strcmp("Banana", "Bananas"));      //-1
  	printf("%d\n", strcmp("Bananas", "Banana"));      //1
  	printf("%d\n", strncmp("Bananas", "Banana", 6));  //0
  ```

  > 아스키 코드 기준에 따라 같으면 `0`,앞 글자가 더 빠르면 `음수`, 뒷 글자가 더 빠르면 `양수`

- Copy : `strcpy()` and `strncpy()`

  ```
  char dst[100] = "";
  char source[] = "Start programming!";
  
  //전체 복사
  strcpy(dst, source);
  
  //해당 글자수까지 복사
  strncpy(dst, source, 5); // '\0' 기호는 복사되지 않는다.
  
  //배열의 대표 포인터 주소 보다 +6 뒤부터 복사
  strcpy(dst, source + 6);
  
  //dst의 6번째 글자부터 덮어씌워진다.
  strcpy(dst, source);
  strcpy(dst + 6, "Coding!");  
  
  //문자열 출력해보기
  puts(dst);
  ```

- `sprintf()`

  ```c
  char str[100] = "";
  int i = 123;
  double d = 3.14;
  sprintf(str, "%0 5d.png %f", i, d);
  puts(str);
  ```

  > 문자열 앞 뒤로 무언가를 추가해서 출력할 수 있다.

### 선택정렬 Selection Sort

<img src="https://gmlwjd9405.github.io/images/algorithm-selection-sort/selection-sort.png" style="zoom: 25%;" />

> 첫 번째 자료를 두 번째 자료부터 마지막 자료까지 차례대로 비교하여 가장 작은 값을 찾아 첫 번째에 놓고, 두 번째 자료를 세 번째 자료부터 마지막 자료까지와 차례대로 비교하여 그 중 가장 작은 값을 찾아 두 번째 위치에 놓는 과정을 반복하며 정렬을 수행한다.

- 코드 예시 :

  ```C
  void selectionSort(int arr[], int n) {
  	int min_idx;
  	for (int i = 0; i < n - 1; i++) {    //Note : n - 1
  		min_idx = i;
  		for (int j = i + 1; j < n; j++) { //Note : n + 1
  			if (arr[j] < arr[min_idx]) {
  				min_idx = j;
  			};
  		};
  		//swap : 각각의 메모리 주소 위치를 바꾸는 것!
  		swap(&arr[min_idx], &arr[i]);
  	}
  }
  ```

- 포인터를 사용해서도 바꿀 수 있다.

  ```c
  void selectionSort(char* arr[], int n) {
  	int min_idx;
  	for (int i = 0; i < n - 1; i++) {    //Note : n - 1
  		min_idx = i;
  		for (int j = i + 1; j < n; j++) { //Note : n + 1
  			/*if (*arr[j] < *arr[min_idx]) {
  				min_idx = j;*/
  
  			//strcmp()를 통해서 각 문자열의 첫 알파벳 비교하기
  			if (strcmp(arr[j], arr[min_idx]) < 0) {
  				min_idx = j;
  			};
  		};
  		//swap : 각각의 메모리 주소 위치를 바꾸는 것!
  		swap(&arr[min_idx], &arr[i]);
  	}
  }
  ```

- 문자함수 `#include <ctype.h>`를 문자열에 사용하기

  ```c
  #include <ctype.h>  //toupper(), ispunct()
  ```

  - 코드 예시 :

    ```c
    void ToUpper(char* str) {
    	//끝 조건을 두는 함수가 아니기 때문에 while 반복문 활용
    	while (*str) {
    		*str = toupper(*str);
    		//포인터 인덱스를 계속 증가
    		str++;
    	}
    }
    
    //기호가 몇개인지 세는 코드
    int PunctCount(const char* str) {
    	int cnt = 0;
    
    	while (*str)
    	{
    		if (ispunct(*str))
    		{
    			cnt++;
    		};
    		str++;
    	};
    	return cnt;
    }
    ```

    



## References

- [홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)
- [TCP SCHOOL](http://tcpschool.com/c/intro)

