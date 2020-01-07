# OPEN CV(Basic)

> 오픈 소스 컴퓨터 비전 라이브러리 중 하나로 크로스플랫폼과 실시간 이미지 프로세싱에 중점을 둔 라이브러리 이며, 영상 관련 라이브러리로 표준 지위를 가지고 있고, 영상 처리를 대중화 시킨 1등 공신이라 한다. 상업적으로도 이용 가능하다.



### 1. 기본 입출력 연습을 통해 기초 다지기

> Open CV와 matplotlib 모듈 활용하여 도형 그려보기

- 직선 그리기 : `cv2.line(img, start, end, color[, thickness, lineType])`

  - img : 그림그릴 대상 이미지, Numpy 배열
  - start : 선 시작 지점 좌표 (x,y)
  - end : 선 끝 지점 좌표 (x,y)
  - color : 선 색상 ,(BGR), (0 ~ 255)
  - thickness=1 : 선 두께
  - lineType: 선그리기 형식
    - cv2.LINE_4,LINE_8, LINE_AA

  ```python
  import cv2
  import matplotlib.pyplot as plt 
  import numpy as np 
  
  #512행, 512열, 3채널 , 255 값을 가지는 numpy 행렬 만들기 
  image = np.full((512, 512, 3), 255, np.uint8)
  image = cv2.line(image, (0,0), (255, 255), (255, 0 ,0),30,cv2.LINE_AA )
  
  plt.imshow(image)
  plt.show
  ```

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/matplotlib_line.jpg?raw=true)

-  사각형 그리기 : `cv2.rectangle(img, start, end, color[, thickness, lineType])`

  - img : 그림 그릴 대상 이미지, NumPy 배열
  - start : d사각형 시작 꼭짓점 (x,y)
  - end : 사각형 끝 꼭짓점( x, y)
  - color : 색상 (BGR)
  - thickness : 선 두께
    - -1 : 채우기
  - lineType : 선타입, cv2.line()과 동일

  ```python
  import cv2
  import matplotlib.pyplot as plt 
  import numpy as np 
  
  image = np.full((512, 512, 3), 255, np.uint8)
  
  image = cv2.rectangle(image, (20,20), (255, 255), (255, 0, 0), 5) 
  #image = cv2.rectangle(image, (20,20), (255, 255), (255, 0, 0), -1) 
  
  
  plt.imshow(image)
  plt.show
  ```

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/matplotlib_line2.jpg?raw=true)

- 세개의 사각형 한번에 그리기:

  ```python
  import cv2
  
  img = cv2.imread('img/blank_500.jpg')
  
  # 좌상, 우하 좌표로 사각형 그리기
  cv2.rectangle(img, (50, 50), (150, 150), (255,0,0) )        
  # 우하, 좌상 좌표로 사각형 그리기
  cv2.rectangle(img, (300, 300), (100, 100), (0,255,0), 10 )  
  # 우상, 좌하 좌표로 사각형 채워 그리기 ---①
  cv2.rectangle(img, (450, 200), (200, 450), (0,0,255), -1 )  
  
  cv2.imshow('rectangle', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/matplotlib_line3.jpg?raw=true" style="zoom:67%;" />

- 다각형 그리기:`cv2.polylines(img, points, isClosed, color[, thickness, lineType])`

  img : 그림 그릴 대상 이미지

  - points : 꼭짓점 좌표, Numpy 배열 리스트
  - isClosed: 닫힌 도형 여부, True/False
  - color : 색상(BGR)
  - thickness : 선 두께
  - lineType : 선 타입, cv2.line()과 동일

  ```python
  import cv2
  import matplotlib.pyplot as plt 
  import numpy as np 
  
  image = np.full((512, 512, 3), 255, np.uint8)
  points = np.array([[5, 5], [128, 258] , [483, 444], [400, 150]])
  image = cv2.polylines(image, [points], True, (0, 0, 255), 4)
  
  plt.imshow(image)
  plt.show
  ```

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/matplotlib_line4.jpg?raw=true)

  ```python
  import cv2
  import numpy as np                          # 좌표 표현을 위한 numpy 모듈  ---①
  
  img = cv2.imread('img/blank_500.jpg')
  
  # Numpy array로 좌표 생성 ---②
  # 번개 모양 선 좌표
  pts1 = np.array([[50,50], [150,150], [100,140],[200,240]], dtype=np.int32) 
  # 삼각형 좌표
  pts2 = np.array([[350,50], [250,200], [450,200]], dtype=np.int32) 
  # 삼각형 좌표
  pts3 = np.array([[150,300], [50,450], [250,450]], dtype=np.int32) 
  # 5각형 좌표
  pts4 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]],dtype=np.int32) 
  
  # 다각형 그리기 ---③
  cv2.polylines(img, [pts1], False, (255,0,0))       # 번개 모양 선 그리기
  cv2.polylines(img, [pts2], False, (0,0,0), 10)     # 3각형 열린 선 그리기 ---④
  cv2.polylines(img, [pts3], True, (0,0,255), 10)    # 3각형 닫힌 도형 그리기 ---⑤
  cv2.polylines(img, [pts4], True, (0,0,0))          # 5각형 닫힌 도형 그리기
  
  cv2.imshow('polyline', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/matplotlib_line5.jpg?raw=true" style="zoom:67%;" />

- 원그리기 : `cv2.circle(img, center, radius, color[, thickness, lineType])`

  - img : 그림 대상 이미지
  - center : 원점 좌표 (x,y)
  - radius : 원의 반지름
  - color : 색상 (BGR)
  - thickness : 선 두께 (-1 : 채우기)
  - lineType : 선 타입, cv2.line()과 동일

  ```python
  import cv2
  import matplotlib.pyplot as plt 
  import numpy as np 
  
  image = np.full((512, 512, 3), 255, np.uint8)
  
  image = cv2.circle(image, (255,255),100, (255, 0, 0), 3) 
  # image = cv2.circle(image, (255,255),100, (255, 0, 0), -1)
  
  plt.imshow(image)
  plt.show
  ```

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/matplotlib_line6.jpg?raw=true)

- 텍스트 그리기 : `cv2.putText(image, text, position, font_type, font_scale, color)`

  - position : 텍스트가 출력될 위치
  - font_type : 글씨체
  - font_scale: 글씨 크기 가중치

  ```python
  import cv2
  import matplotlib.pyplot as plt 
  import numpy as np 
  
  image = np.full((512, 512, 3), 255, np.uint8)
  image = cv2.putText(image, 'Hello World', (0, 200), cv2.FONT_ITALIC, 2, (255, 0, 0))
  
  cv2.imshow('text', image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/matplotlib_line7.jpg?raw=true" style="zoom:67%;" />



## 참고한 자료

- 강사님 자료 (이미지분석 인공지능 서비스 개발 / 최진영 강사님)
- 도서 참고
  - 파이썬과 Open CV를 이용한 컴퓨터 비전 학습(알렉셰이 스피쉐보이)
  - 파이썬을 이용한 머신러닝,딥러닝 실전 앱 개발(쿠지라 히코우즈쿠에)
