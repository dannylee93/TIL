# Basics of Computer Structure

> 홍정모 교수님의 따라하며 배우는 C언어를 수강하며 정리한 컴퓨터 구조 관련 정리 내용 입니다.



### Overview

컴퓨터의 구조를 알아보고  C 언어를 구현할 때 조금 더 깊게 이해하고 프로그래밍 할 수 있도록 기초적인 지식을 학습합니다.



### 구성요소

- 기억장치
  - 중앙처리장치 CPU : 컴퓨터의 모든 연산 담당
  - 주기억장치 RAM : 전원 끄면 데이터가 사라짐
  - 보조기억장치 :  HDD(물리적으로 돌아가는 디스크가 있어서 속도 느림),  SSD(속도 훨씬 빠름)

### 컴퓨터 작동과정

- 부팅절차 :

  ```
  전원공급 - 부트프로그램 실행 - 하드웨어 검사 - 운영체제 로드 및 실행
  ```

  > '운영체제 로드' 과정에서 보조기억장치에 있는 운영체제, 보조프로그램을 CPU로 가져오면서 실행하는 것임

- 결과적으로 부팅과정은 보조기억장치에 저장된 운영체제를 로딩하는 과정이다.

### 운영체제

- 사용자가 하드웨어에 각각 접근해서 운용하는 것이 아니라 운영체제가 통합해서 사용성을 쉽게 해준다.

### 컴퓨터는 왜 이진수를 사용할까

- 진공관 - 트랜지스터 - .... 로 발전하면서 초기에 껐다 켰다 하는 과정들의 개념이 발전된 것

### 현대 컴퓨터의 기본구조

- 옛날 방식의 프로그래밍 : 
  - Plugboard, Punched card, Enigma, ...
- 현대적 구조의 시작 :
  - 폰 노이만 구조(Input device - CPU&Memory - Output device)
- Single system computer bus
  - 여기에서 버스란 `옴니버스`라는 단어에서 온 용어 이며, 사람이 버스에 타는 것 처럼 컴퓨터는 이진수 정보를 `버스`에 담아 옮긴다.
  - CPU와 Memory 사이의 연결고리인 싱글버스 구조는 Control, Address, Data 의 3가지 구조를 가지고 있다.

### 메모리 기본 구조

- CPU << `Cache` >> Memory : 두 구조 사이에 캐시메모리가 자주 사용하는 데이터를 바로 작업할 수 있도록 도와줘서 속도를 향상 시킴
- ACCESS 구조
  - 순차접근 Sequential Access : 예를 들어, 1에서 5위치를 가려면 12345 과정을 거쳐야함.
  - 임의접근 Random Access : 어디 위치이든 바로 접근할 수 있다.
- CPU와 RAM이 정보를 주고 받는 방식
  - 메모리가 하는 일 : CPU에 데이터를 제공하고, 받는다.
  - CPU가 하는 일 : 각각 Address, Control, Data 버스 에 나눠 정보를 요청(여기에서, Address 버스 구조 때문에 C언어에 포인터 방식이 있음)

### CPU 기본구조

- 프로그램이 시작되는 과정 :

  - 보조기억장치 >> 주기억장치 >> CPU

- 프로그래밍 언어들 :

  - 기계어 >> 어셈블리 >> High Level Language

- CPU 명령어 집합 :

  <p align='center'><img src="https://slidesplayer.org/slide/15492736/93/images/50/%EB%AA%85%EB%A0%B9%EC%96%B4+%EC%84%B8%ED%8A%B8+%EB%AA%85%EB%A0%B9%EC%96%B4+%EC%84%B8%ED%8A%B8+%ED%8A%B9%EC%A0%95+CPU%EB%A5%BC+%EC%9C%84%ED%95%B4+%EC%A0%95%EC%9D%98%EB%90%98%EB%8A%94+%EB%AA%85%EB%A0%B9%EC%96%B4%EB%93%A4+%EB%A6%AC%EC%8A%A4%ED%8A%B8%EB%82%98+%EC%A7%91%ED%95%A9.jpg" alt="제3장 중앙처리장치. - ppt download" style="zoom:50%;" /></p>

- CPU 구성요소 :

  - 제어장치 Control Unit  
  - 산술논리장치 ALU : 연산할 때 작동된다.
  - Registers : 레지스터에는 여러 종류가 있다. 인명부 혹은 등록부 같은 특징을 가지고 있고 작업공간과 같이 기능에 따라 여러가지가 있다.

### CPU 작동 원리

(1) 메모리 예시

| 주소 |  메모리   |
| :--: | :-------: |
|  8   |     0     |
|  9   |     0     |
|  10  |     3     |
|  11  |     4     |
|  12  |     0     |
|  13  |    ...    |
| 100  | LOAD[10]  |
| 101  |  ADD[11]  |
| 102  | STORE[12] |

> 주소(명령 저장)와 메모리(실제 데이터가 할당)가 있다. A와 B의 메모리 및 명령 요청이 각각 주소에 할당 된 것을 볼 수 있다.

(2) 프로그래밍 예시

|    주소     |             구분             |
| :---------: | :--------------------------: |
| 고수준 언어 |       A=3  B=4  C=A+B        |
|  어셈블리   | LOAD[10]  ADD[11]  STORE[12] |
|   기계어    |         0101010 ...          |

- 순서 :
  1. 프로그램 카운터[주소] : CPU가 실행시키면 다음번 명령어를 주소로 INPUT(시작점이 필요하고, 프로그램 카운터가 그 역할을 한다고 생각하면 됨)
  2. 메모리 주소 레지스터[주소]
  3. 메모리 데이터 레지스터 [처음 실행할 명령]
  4. 명령어 레지스터[명령]
  5. 1번으로 가서 다음 실행 주소 INPUT, 이전 명령어는 제어장치(Control Unit)으로
  6. 메모리 주소 레지스터가 제어장치를 확인하고 데이터가 있는 주소를 LOAD
  7. 어큐뮬레이터로 데이터 진입
  8. 산술논리장치에서 데이터를 연산
  9. 어큐뮬레이터에 저장 되어있는 최종 데이터를 메모리에 저장



### 정보의 기본단위

- 비트 Binary digit : 정보의 기본단위
- 바이트 Byte(==8bit) : 메모리 주소의 기본 단위
- 워드 Word : CPU가 데이터를 다루는 기본 단위(레지스터의 크기)
  - 16비트, 32비트, 64비트 등 컴퓨터 시스템에 따라 각각 다르다.



### 이진수



## 기타

- CPU 작동원리 리마인드

- 

## References

- *[홍정모 교수님의 따라하며 배우는 C언어](https://www.inflearn.com/course/following-c)*

