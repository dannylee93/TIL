# OPEN CV(Basic)

> 오픈 소스 컴퓨터 비전 라이브러리 중 하나로 크로스플랫폼과 실시간 이미지 프로세싱에 중점을 둔 라이브러리 이며, 영상 관련 라이브러리로 표준 지위를 가지고 있고, 영상 처리를 대중화 시킨 1등 공신이라 한다. 상업적으로도 이용 가능하다.

### 1. Open CV 개요

- 머신러닝과의 관계:

  이미지를 머신러닝 입력으로 전달하려면 숫자 배열의 형식으로 데이터를 변경해야 한다. 이미지는 일반적으로 BMP, PNG, JPG 형식 등으로 다양하다. 또한 흑백, 컬러 의 색상을 가지고 있기도 하다. 여기서 `Open CV` 는 이미지 형식을 가공하고 색상을 맞출 때 사용한다.

- 환경구축하기

  *설치 명령어:*

  ```shell
  - pip install opencv-python / pip3 install opencv-python  
  - pip3 install opencv-contrib-python (엑스트라 모듈 포함) 
  ```

  

### 2. 기본 입출력 연습을 통해 기초 다지기

- 새창에 이미지 띄우기: `imshow`

  ```python
  import cv2
  
  img_file = "img/girl.jpg" # 표시할 이미지 경로            ---①
  img = cv2.imread(img_file)  # 이미지를 읽어서 img 변수에 할당 ---②
  
  
  cv2.imshow('IMG', img)   # 읽은 이미지를 화면에 표시      --- ③
  cv2.waitKey()           # 키가 입력될 때 까지 대기      --- ④
  cv2.destroyAllWindows()  # 창 모두 닫기            --- ⑤
  ```

- 주피터 노트북에서 바로 보기: `%matplotlib inline`

  ```python
  %matplotlib inline
  
  import matplotlib.pyplot as plt
  import cv2
  img = cv2.imread("img/girl.jpg")
  plt.axis('off') #axis 출력 끄기 
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  > matplotlib모듈의 인라인 출력을 하면 이미지를 새창으로 띄우지 않고 볼 수있다.(+ axis 'off' 하지 않으면 이미지의 사이즈가 x,y축에 표시 된다.)

  | 모듈       | 컬러 데이터의 공간      |
  | ---------- | ----------------------- |
  | Open CV    | BGR(파란색 녹색 빨간색) |
  | matplotlib | RGB(빨간색 녹색 파란색) |

  > 모듈에 따라 컬러 순서가 달라 cvtColor()를 사용하지 않으면 붉은색과 파란색이 반전되어 출력된다.

- 회색화면(Grayscale로 읽기) : `cv2.IMREAD_GRAYSCALE`

  ```python
  import cv2
  
  img_file = "img/girl.jpg" 
  img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  #그레이 스케일로 읽기
  
  cv2.imshow('IMG', img)
  cv2.waitKey()
  cv2.destroyAllWindows()
  ```

- 이미지 저장하기 : `cv2.imwrite(file_path, img)`

  - file_path : 저장할 파일 경로 이름, 문자열
  - img : 저장할 영상, Numpy 배열

  ```python
  import cv2
  
  img_file = 'img/girl.jpg'
  
  img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
  cv2.imwrite('img/girl_gray.jpg', img) #파일로 저장, 포맷은 확장에 따름
  
  cv2.imshow(img_file, img)
  cv2.waitKey()
  cv2.destroyAllWindows()
  ```

- 동영상 및 카메라 프레임 읽기: `cv2.VideoCaputure(file_path 또는 index)`

  - file_path : 동영상 파일 경로
  - index : 카메라 장치 번호 (0 부터 차례로 증가)
  - ret = cap.isOpend() : 객체 초기화 확인
    - ret : 초기화 여부, True/False
  - ret, img = cap.read() : 영상 프레임 읽기
    - ret : 프레임 읽기 성송 또는 실패 여부, True / False
    - img : 프레임 이미지, Numpy 배열 또는 None
  - cap.set(id, value) : 프로퍼티 변경
  - cap.get(id) : 프로퍼티 확인
  - cap.release() : 객체 자원 반납

  ```python
  import cv2
  
  video_file = "img/big_buck.avi" # 동영상 파일 경로
  
  cap = cv2.VideoCapture(video_file) # 동영상 캡쳐 객체 생성  ---①
  if cap.isOpened():                 # 캡쳐 객체 초기화 확인
      while True:
          ret, img = cap.read()      # 다음 프레임 읽기      --- ②
          if ret:                     # 프레임 읽기 정상
              cv2.imshow(video_file, img) # 화면에 표시  --- ③
              cv2.waitKey(25)            # 25ms 지연(40fps로 가정)   --- ④
          else:                       # 다음 프레임 읽을 수 없슴,
              break                   # 재생 완료
  else:
      print("can't open video.")      # 캡쳐 객체 초기화 실패
  cap.release()                       # 캡쳐 자원 반납
  cv2.destroyAllWindows()
  ```

  > waitKey(value)의 value 값 변경하면서 변화 확인하기

- 프레임 스트림 프로퍼티 얻기:

  - `cv2.CAP_PROP_FRAME_WIDTH` : 프레임 폭
  - `cv2.CAP_PROP_FRAME_HEIGHT` : 프레임 높이
  - `cv2.CAP_PROP_FPS` : 프레임 초당 프레임 수
  - `cv2.CAP_PROP_POS_MSEC` : 동영상 파일의 프레임 위치(MS)
  - `cv2.CAP_PROP_POS_AVI_RATIO` : 동영상 파일의 상대 위치 (0:시작 , 1:끝)

  ```python
  import cv2
  
  def print_capture_properties(*args):
      capture = cv2.VideoCapture(*args)
      print('Frame count:', int(capture.get(cv2.CAP_PROP_FRAME_COUNT)))
      print('Frame width:', int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)))
      print('Frame height:', int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
      print('Frame rate:', capture.get(cv2.CAP_PROP_FPS))
      
  print_capture_properties("img/big_buck.avi")
  print_capture_properties(0)
  ```

- 영상 파일에서 프레임간의 이동

  - `cap.set(id, value)` : 프로퍼티 변경
  - `cap.get(id)` : 프로퍼티 확인
  - `cv2.CAP_PROP_POS_FRAMES` : 현재프레임의 개수

  ```python
  import cv2
  
  capture = cv2.VideoCapture('img/big_buck.avi')
  frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
  print('Frame count:', frame_count)
  
  #첫번째 프레임을 가져온다. 
  print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
  cature, frame = capture.read()
  cv2.imshow('frame0', frame)
  
  # 100번째 프레임으로 이동한다. 
  capture.set(cv2.CAP_PROP_POS_FRAMES, 100)
  print('Position:', int(capture.get(cv2.CAP_PROP_POS_FRAMES)))
  cature, frame = capture.read()
  cv2.imshow('frame100', frame)
      
  cv2.waitKey()
  cv2.destroyAllWindows()
  ```

> 이 외에도 웹캠을 활용한 사진찍기(`cv2.VideoCapture()`), 녹화하기(`cv2.VideoWriter(file_path, fourcc, fps, size)`)가 있다.



## 참고한 자료

- 도서 참고
  - 파이썬으로 만드는 Open CV 프로젝트(이세우 지음 / 프로그래밍인사이트)
  - 파이썬과 Open CV를 이용한 컴퓨터 비전 학습(알렉셰이 스피쉐보이)
  - 파이썬을 이용한 머신러닝,딥러닝 실전 앱 개발(쿠지라 히코우즈쿠에)