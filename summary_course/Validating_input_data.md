# Validating input data

> 문자 입출력 프로그램에서, 입력 유효성을 검증해보기



### 입출력과 버퍼 Buffer

- 기본적인 입출력 :

  C언어에서는 `#include <stdid.h>` 의 `stdin` 표준 스트림을 통해 입력장치를 다루고, `stdout` **스트림**을 통해 출력장치를 다룬다.

- 스트림 Stream : 

  C 프로그램은 파일아니 콘솔의 입출력을 직접 다루지 않고, 스트림을 통해 다룬다. 여기서 스트림(Stream)이란 **데이터의 실제 입력이나 출력이 표현된 데이터의 이상화된 흐름**을 의미한다. 즉, 운영체제에 의해 생성되는 가상의 연결고리.

  <img src="http://tcpschool.com/lectures/img_c_stream_input_output.png" alt="표준 스트림" style="zoom:67%;" />

- 버퍼 Buffer : 

  <img src="http://tcpschool.com/lectures/img_c_buffer_vs_nobuffer.png" style="zoom:67%;" />

  입출력 프로그래밍을 하면서, 사용한 함수들은 버퍼(Buffer) 라는 임시 메모리 공간을 사용한다. 버퍼를 사용하며, 어떤 임의의 크기 공간 안에 문자를 넣고 한번에 전달하며 전송시간을 줄일 수 있다.

### 파일의 끝 EOF : End Of File

C언어는 운영체제와 상관없이, 파일의 끝에 도착했을 때 언제나 특별한 값을 반환하도록 하며 이것을 `EOF(End of file)`라 칭하고 이 값은 `-1` 을 나타낸다. 윈도우에서는 `ctrl + Z` 를 누르면 EOF를 발생시킬 수 있다.

- 프로그래밍에서는 `.`, `#`  등 다양한 방식으로 입력의 끝을 표현하는데, 입력 중간에 동일한 기호를 넣고 싶을 때는 난감한 상황이 발생한다.

- `#include <stdio.h>` 에 `EOF` 가 있으며 `ctrl + Z` 를 입력하면 종료된다.

  ```c
  //stream 현상
  while (1){
  
  	c = getchar();
  	printf("%d\n", c);
  	
  	if (c == EOF)
  		break;
  }
  ```

  > EOF 활용 코드 예시
  
- 텍스트 파일 읽기 :

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  #include <stdbool.h>
  #include <stdlib.h>  //exit()
  
  void main(void) {
  
  	int c;
  	FILE *file = NULL;  //file 이라는 변수 앞에 *기호는 포인터라는 의미. 주소가 저장됨.
  	char file_name[] = "my_file.txt";
  
  	file = fopen(file_name, "r");
  	if (file == NULL)
  	{
  		printf("Failed to open file.\n");
  		exit(1);  //오류코드 같이 알려주면서 프로그램을 강제종료한다.
  	}
  
  	while ((c=getc(file)) != EOF)
  	{
  		putchar(c);
  	}
  	fclose(file);
  
  }
  ```

  - `FILE` : 파일 스트림을 다룰 수 있는 어떤 정보가 저장된다. (`*` 기호는 포인터를 의미)
  - `exit()` : `(임의의 오류코드)` 를 넣으면 해당 조건일 때 오류코드를 알려주며 프로그램을 강제 종료한다.
  - `fopen(변수 , __)` : `__` 에는 `r` (읽기) 또는 `w` (저장)이 들어갈 수 있다.
  - `fclose()` : 프로그램이 파일을 다 사용했다고 깔끔하게 명시하기 위해.



### 입출력의 방향 재지정 Redirection

`프로그램.exe` 의 입력 또는 출력 방향을 재지정하여 활용할 수 있다.

- 예시에 활용할 코드 :  명령프롬프트 창과 함께 활용한다.

  ```c
  #define _CRT_SECURE_NO_WARNINGS
  #include <stdio.h>
  
  int main(void) {
  	
      //출력 
  	printf("Programming.\n");
  	//입출력 
  	char str[100];
  	scanf("%s", str);
  	printf("I love %s\n", str);
  
  }
  ```

1. 명령프롬프트에서 빌드된 프로그래밍 실행해보기 `.exe`

   ```c
   C:\...\TBC-workbook\MyFirstSolution\Debug>RedirectionFiles.exe
   I love apple.
   ```

   > 해당 파일 이름을 입력하고 `Enter`

2. 출력된 결과를 `output.txt` 로 저장시켜보기

   ```c
   C:\...\TBC-workbook\MyFirstSolution\Debug>RedirectionFiles.exe > output.txt
   ```

   > `>` 기호와 `파일명.txt` 를 사용하면 새로 파일이 생성되며 출력이 저장된다.

3. 입출력 버전을 활용하여 빌드후, 커맨드 창에서 입력과 출력을 활용할 수도 있다.

   ```c
   C:\...\TBC-workbook\MyFirstSolution\Debug>RedirectionFiles.exe
   banana
   I love banana
   ```

4. 임의의 input을 저장할 파일을 생성 후, 입력에 사용할 수 있다.

   ```c
   C:\...\TBC-workbook\MyFirstSolution\Debug>RedirectionFiles.exe < input.txt
   I love Melon
   ```

   > Melon 이라는 임의의 문자열을 input 데이터에 저장 후, 프로그램의 입력에 추가했다.

5. 입출력 관련 파일을 동시에 활용할 수 있다.(하기 전 빌드과정 필히 확인)

   ```
   C:\Users\bruce0809\TBC-workbook\MyFirstSolution\Debug>RedirectionFiles.exe < input.txt > output.txt
   ```

6. 출력 빌드 후 카피하고 입력에 사용할 수 있다.

   ```c
   C:\...\TBC-workbook\MyFirstSolution\Debug>copy RedirectionFiles.exe test.exe
           1개 파일이 복사되었습니다.
   
   C:\...\TBC-workbook\MyFirstSolution\Debug>test.exe | RedirectionFiles.exe
   I love Programming.
   
   C:\...\TBC-workbook\MyFirstSolution\Debug>
   ```







## References

- [홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)
- [TCP SCHOOL](http://tcpschool.com/c/intro)

