# Anaconda로 파이썬 개발 환경 셋팅

> Anaconda는 파이썬과 그와 관련된 파이썬의 라이브러리들을 하나로 묶어 둔 일종의 배포판이다. Pandas, Scikit-Learn 등의 라이브러리를 기본적으로 포함한다.

- Anaconda에 포함된 주요 Library - List
  - `Python` : 말 그대로 파이썬의 실행 파일
  - `jupyter notebook` : 주피터 노트북은 대화형의 개발 도구(IDE 중의 하나)
  - `numpy` : 빠른 수치계산과 각종연산을 도와주는 라이브러리(배열 등)
  - `pandas` : 정형 데이터 전처리 및 분석을 도와주는 라이브러리(엑셀같은 기능 구현하고 싶을때 Pandas로 구현할 수 있는게 찾아보면 많다.)
  - `matplotlib`: 데이터 시각화를 도와주는 라이브러리이다.
  - `django`: 웹 개발을 위한 프레임워크
  - `flask`: 좀더 가벼운 웹 개발 프레임워크



### 1. IDE(통합개발환경) Settings

#### (1) Anaconda 설치

- 아나콘다 홈페이지에서 원하는 파이썬의 버전과 OS에 맞추어서 다운로드 한다.

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/SettingAnaconda.jpg?raw=true" style="zoom:50%;" />

- 기존에 설치해둔 다른버전의 파이썬/아나콘다 있다면 꼭 **삭제** 해야 충돌 발생 방지 할 수 있다.

- 아래 이미지의 체크박스를 꼭 체크하기(환경변수 자동 연결)

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/SettingAnaconda_2.jpg?raw=true" style="zoom: 67%;" />

- 설치 후, `Anaconda Prompt` 와 `Jupyter Notebook` 이 모두 설치 되어 있는지 확인하면 완료.

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/SettingAnaconda_3.jpg?raw=true" style="zoom:67%;" />



#### (2) Tensorflow 설치해보기

- `Anaconda Prompt` 를 찾아 우 클릭 후, "관리자 권한으로 실행" 버튼을 클릭

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/SettingAnaconda_4.jpg?raw=true" style="zoom:50%;" />

- 아래 처럼 `conda install tensorflow==1.13.1` 을 입력해서 Tensorflow 설치하기(Uninstall 필요 시 : 'conda uninstall tensorflow')

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/SettingAnaconda_5.jpg?raw=true" style="zoom:67%;" />

  > 관리자 권한으로 실행하는 이유는 이런 방식으로 해야 global(전역)로 설치 되어 일부에서 오류가 생기는 것을 방지할 수 있다고 한다.

- 잘 설치 되었으면 아래 코드들을 한 줄씩 입력하여 설치되었는지 확인하자(아래 코드처럼 나오면 문제 없음!)

  1. `python`

  2. `import tensorflow as tf`

  3. `tf.__version__`

     ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/SettingAnaconda_6.jpg?raw=true)



#### (2) Trouble 발생 시 참고 사항

- `connection error : [SSL : CERTIFICATE_VERIFY_FAILED] ` 에러 발생 시(HTTPS, SSL 보안 관련 사항 때문에 파이썬 패키지 설치가 안될 때)

  > pip 명령어로 라이브러리 설치가 안될 때 다음 명령 사용해보자
  >
  > `pip` : python install package

  1. cmd 창에서 https 대신에 http url 사용해서 pip install 설치
     - `pip install--trusted-host pypi.org--trusted-host files.pythonhosted.org{라이브러리 이름}`
     - `pip install--trusted-host pypi.python.org{라이브러리 이름}`
     - `pip install--index-url=http://pypi.python.org/simple/--trusted-host pypi.python.org{라이브러리 이름}`
  2.  Anaconda prompt에서 conda 명령어 설치(차례대로 입력)
     - `conda config --set ssl_verify false`
     - `conda install{라이브러리 이름}`
  3. 프록시가 해제된 경우 문제가 발생할 수 있다.
     - 브라우저 > 인터넷 옵션 > 연결 < **LAN 설정 항목** 전체 체크 해제
     - 제어판 > 시스템 > 고급시스템 설정 > 환경변수 > 시스템 변수 항목에 HTTP_PROXY가 있는 경우 삭제

- Conda install tensorflow 명령어로 설치 했을때, `conda verification Error` 가 발생한 경우

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/SettingAnaconda_7.JPG?raw=true)

  - `conda clean--all`
  - `conda install tensorflow`

- pip 업그레이드가 필요한 경우:

  - `python -m pip install -upgrade pip` 입력

- pip를 통해 라이브러리 설치속도가 느릴 경우(미러사이트를 국내로 변경)

  - 윈도우 탐색기 입력 `%appdata%`

  - "pip" 폴더 생성 후 아래 3줄을 내용으로 "pip.ini" 파일 작성

    ```shell
    [global]
    Index-url=https://ftp.daumkakao.com/pypi/simple
    Trusted-host=ftp.daumkakao.com
    ```

    

### 2. Jupyter Notebook 시작하기

> 주피터 노트북의 Jupyter는 Julia,python,R 의 합성어라고 한다. 말하자면 여러 프로그래밍 언어를 여기서 툴로 사용할 수 있다는 말. 시작하기 앞서 크롬을 기본 웹브라우저로 설정해야 한다.
>
> 코딩하며 바로바로 결과를 확인할 수 있어서 피드백이 빠른게 장점이고, 내 개인적으로는 다른 툴을 써보니 주피터 노트북이 반응도 빠르고 단축기도 심플해서  여러모로 직관성이 좋은 것 같다.

#### (1) 주피터 노트북 실행하기

- Jupyter Notebook은 해당 Prompt를 실행해서 켜야한다.

  ![](https://t1.daumcdn.net/cfile/tistory/99347C4C5A9CDCE50B)

- Prompt를 `Enter`를 누르면 웹브라우저를 통해 실행된다.

  <img src="https://dojang.io/pluginfile.php/14085/mod_page/content/7/046011_.png" alt="주피터 노트북 실행에 대한 이미지 검색결과" style="zoom:67%;" />



#### (2) 주피터 노트북 테마 바꿔보기

> 계속 하얗게 빛나는 화면을 보다보니 적응이 안되기도 했고, 기본 적용되어 있는 폰트가 개인적으로 별로였다. 조금 서치해보면 본인 취향에 맞게 다양하게 셋팅할 수 있어서 원한다면 바꿔보는 것도 좋을 것 같다.

1. 윈도우의 `cmd`를 실행한다.

2. 아래 글을 그대로 입력한다.

   ```shell
   pip install --upgrade jupyterthemes
   ```

3. 원하는 조합을 찾아 테마 조정한다

   - https://goo.gl/g5Mzsi (여기에 다양한 예시와 테마에 대한 설명이 나와있다. 특히 주피터 노트북 내에서 실행하는 방법도 설명 되어있다)

     ```shell
     jt -t chesterish -T -N -f bitstream -fs 10 -nf opensans -nfs 11 -tf robotosans -tfs 10 -cellw 1140 -lineh 150
     ```

     > 나는 조금 어둡고  파랑파랑한 버전을 사용했다.

   - 테마 조합 코드 해설

     ```shell
     - `테마` : chesterish
     - `툴바 & 제목바 보임` : T & N
     - `코드 폰트 (입력 & 출력)` : bitstream & 10 (f, fs)
     - `노트북 폰트 (메인화면, 상단 제목 bar 및 메뉴 bar)` : opensans 11 (nf, nfs)
     - `마크다운 폰트` : robotosans 10 (tf, tfs)
     - `cell 너비` : 1140
     - `line height` : 150 
     ```

   - 이 외에도 밝은 조합도 있다.

     ```shell
     jt -t solarizedl -T -N -f bitstream -fs 10 -nf opensans -nfs 11 -tf robotosans -tfs 10 -cellw 1140 -lineh 150
     ```

     ```shell
     jt -t grade3 -T -N -f bitstream -fs 10 -nf opensans -nfs 11 -tf robotosans -tfs 10 -cellw 1140 -lineh 150
     ```

     

##  참고한 자료

- 강사님 자료 (이미지분석 인공지는 서비스 개발 실무)
- 개인 홈페이지 (Github)
  * https://goo.gl/g5Mzsi 