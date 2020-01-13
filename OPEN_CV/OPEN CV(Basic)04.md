# OPEN CV(Basic)

> 오픈 소스 컴퓨터 비전 라이브러리 중 하나로 크로스플랫폼과 실시간 이미지 프로세싱에 중점을 둔 라이브러리 이며, 영상 관련 라이브러리로 표준 지위를 가지고 있고, 영상 처리를 대중화 시킨 1등 공신이라 한다. 상업적으로도 이용 가능하다.



## 변환 & 필터링

> `이미지 필터링` 은 여러 수식을 이용해서 이미지를 이루고 있는 픽셀 행렬을 다른 값으로 바꾸어 이미지를 변형하는 것을 말한다.
>
> 이미지의 위치변경(회전, 변환), 필터(블러링), 경계검출(필터, 침식과 팽창, 컨투어)에 대해 정리하자.



### 1. 위치 변경(회전 및 변환)

- 위치변경 변환 행렬 : `cv2.warpAffine(image, M, dsize)`== 이미지의 위치를 변경해준다.

  - M : 변환 행렬
  - dsize : Manual Size

   <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)00.jpg?raw=true" style="zoom: 67%;" />

  ```python
  import cv2 
  import numpy as np 
  import matplotlib.pyplot as plt 
  
  image = cv2.imread('img/image.jpg')
  
  height, width = image.shape[:2]
  
  M = np.float32([[1, 0, 200], [0, 1, 300]])
  dst = cv2.warpAffine(image, M, (width, height))
  
  plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  > 상단의 파이썬 코드를 보면 먼저 이미지를 가져온다음, 그 이미지 정보에서 컬러관련 정보를 누락시킨다. (`.shape[:2]` / 원래는 (가로, 세로, 컬러) 정보이다. / 위치변환 시키는데 컬러데이터는 필요없으니까 ) 

#### (1) 이미지 회전

- ##### 이미지 회전(row한 버전): 

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)01.jpg?raw=true" style="zoom:67%;" />

  ```python
  import cv2
  import numpy as np 
  import matplotlib.pyplot as plt
  
  img = cv2.imread('img/image.jpg')
  rows, cols = img.shape[0:2]
  
  #라디안 각도 계산 ( 60진법을 호도법으로 변경)
  d90 = 90.0 * np.pi / 180 
  
  #변환행렬 생성
  m90 = np.float32([[np.cos(d90), -1 * np.sin(d90), rows],
                    [np.sin(d90), np.cos(d90), 0]])
  
  #변환행렬 적용
  r90 = cv2.warpAffine(img, m90, (rows, cols))
  
  plt.imshow(cv2.cvtColor(r90, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  > 넘파이 모듈의 파이 범주율을 활용하여 계산한다.

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)02.jpg?raw=true)

- ##### 이미지 회전(회전에 대한 직접적인 변환행렬 만듦) : `cv2.getRotationMatrix2D(center, angle, scale)`

  - center : 회전 중심좌표, 튜플(x,y)
  - angle : 회전각도
  - scale : 확대/축소 배율

  ```python
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt
  
  img = cv2.imread('img/image.jpg')
  
  # 행과 열 정보만 저정합니다. 
  rows, cols = img.shape[0:2]
  
  m90 =cv2.getRotationMatrix2D((rows / 2, cols / 2), 90, 0.5)
  dst = cv2.warpAffine(img, m90, (rows, cols)) 
  
  plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
  plt.show() 
  ```

  > 위에 row한 버전과는 다르게,  sin-cos 공식을 사용하지 않고 간단하게 모듈 사용했다. 

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)03.jpg?raw=true)

- ##### 이미지 회전(flip 해보는 버전) :  `cv2.flip(img, 0or1)`

  ```python
  import cv2
  import matplotlib.pyplot as plt
  
  img1 = cv2.imread("img/pump_horse.jpg")
  img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
  img_flip = cv2.flip(img1, 1) # 1은 좌우 반전, 0은 상하 반전입니다.
  
  # 이 아래 부분은 그림을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
  plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열
  plt.imshow(img1)
  
  plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
  plt.imshow(img_flip)
  plt.show()
  ```

  > .flip() 의 설명을 보면 `flip(src, flipCode[, dst])` 이라고 나와 있는데 여기서 dst는 destination의 약자라고 한다. Open CV에서는 주로 함수가 끝나면 저장될 공간을 지칭한다고 한다.

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)04.jpg?raw=true)



#### (2) 변환(Transform)

- ##### 어핀 변환(Affine Transform) :  `cv2.getAffineTransform(pts1, pts2)`

  - pts1 : 변환 전 영상의 좌표 3개, 3 x 2 Numpy 배열(float32)
  - pts2 : 변환 후 영상의 좌표 3개, pts1과 동일
  - matrix : 변환행렬 반환, 2 x 3 행렬

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  
  img = cv2.imread('img/fish.jpg')
  rows, cols = img.shape[:2]
  
  # ---① 변환 전, 후 각 3개의 좌표 생성
  pts1 = np.float32([[100, 50], [200, 50], [100, 200]]) # 전
  pts2 = np.float32([[80, 70], [210, 60], [250, 120]])  # 후
  
  # ---② 변환 전 좌표를 이미지에 표시
  cv2.circle(img, (100,50), 5, (255,0), -1)
  cv2.circle(img, (200,50), 5, (0,255,0), -1)
  cv2.circle(img, (100,200), 5, (0,0,255), -1)
  
  #---③ 짝지은 3개의 좌표로 변환 행렬 계산
  mtrx = cv2.getAffineTransform(pts1, pts2)
  
  #---④ 어핀 변환 적용
  dst = cv2.warpAffine(img, mtrx, (int(cols*1.5), rows))
  
  #---⑤ 결과 출력
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()
  plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
  plt.show()
  
  ```

  > pts1,2에 정의한 3개의 좌표 공간은 임의 지정이다. 
  >
  > circle 함수로 정의한 공간은 변환과 전혀 관련 없다. 위치가 어떻게 변화했는지 깃발 찍고 확인하는 용도.

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)05.jpg?raw=true)

  - `cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])`

    - radius : 반지름
    - 컬러 : 파란색(255,0,0) , 초록색(0,255,0), 빨간색(0,0,255), 노란색(0,255,255)
    - 두께 : +(양수) 이면 테두리의 두께, 음수(-1)이면 도형 안에 색이 채워진다.

    

- ##### 원근 변환(Perspective Transform) :  `cv2.getPerspectiveTransform(pts1, pts2) `

  - pts1, 2 : 변환 이전 영상의 좌표 4개, 4 X 2 Numpy 배열(float32)
  - mtrx : 변환행렬 반환, 3 X 3 행렬
  - `cv2.warpPerspective(src, mtrx, dsize[, dst, flags, borderMode, borderValue])` : cv2.warpAffine()함수와 기능 동일
    - src : image
    - mtrx : 변환행렬
    - dsize : Manual Size

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  
  img = cv2.imread("img/fish.jpg")
  rows, cols = img.shape[:2]
  
  #---① 원근 변환 전 후 4개 좌표
  pts1 = np.float32([[0,0], [0,rows], [cols, 0], [cols,rows]])
  pts2 = np.float32([[100,50], [10,rows-50], [cols-100, 50], [cols-10,rows-50]])
  
  #---② 변환 전 좌표를 원본 이미지에 표시
  cv2.circle(img, (0,0), 10, (255,0,0), -1)
  cv2.circle(img, (0,rows), 10, (0,255,0), -1)
  cv2.circle(img, (cols,0), 10, (0,0,255), -1)
  cv2.circle(img, (cols,rows), 10, (0,255,255), -1)
  
  #---③ 원근 변환 행렬 계산
  mtrx = cv2.getPerspectiveTransform(pts1, pts2)
  #---④ 원근 변환 적용
  dst = cv2.warpPerspective(img, mtrx, (cols, rows))
  
  
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()
  plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  > 4가지 좌표의 pts 정의로 ()에서 위치는 각각 (좌상, 좌하, 우상, 우하) 이다 이미지 옆의 좌표숫자를 잘 기억하자

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)06.jpg?raw=true)

  

### 2. 필터링(Filtering)

> 필터링이란 입력 값에서 원하지 않는 값은 걸러내고 원하는 결과만을 얻는다는 의미이다.
>
> 영상을 흐리게 하거나 또는 또렷하게 할 수 있다. `컨볼루션 계산`을 통해서 정보를 계산한다. 

- ` 컨볼루션 계산` : n x n 크기의 커널의 각 요소와 대응하는 입력 픽셀 값을 곱해서 결과 값으로 결정하는 연산의 반복
- `블러링(Blurring)` : 이미지를 흐릿하게 만드는 것 (평균 블러링, 가우시안 블러링)
  - 이미지 속 데이터를 누락시키면서 흐리게 만들고, 반대로 어떤 추정값을 다시 넣으면서 고품질의 이미지로 바꿀 수 있다. 



#### (1) 평균값 적용(각 픽셀에 적용 / 전용 함수 사용) 필터:

- `cv2.filter2D(src, ddepth, kernel[, dst, anchor, delta,  borderType])` : 모든 픽셀에 대해서 각각 firter 적용

  -  ddepth : 출력값의 dtype 
  - kelnel : 컨볼루션 커널, float32의 n x n 크기의 배열

  ```python
  import cv2
  import numpy as np
  from matplotlib import pyplot as plt
  
  img = cv2.imread('img/aircraft.jpg')
  '''
  #5x5 평균 필터 커널 생성    ---①
  kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04, 0.04],
                     [0.04, 0.04, 0.04, 0.04, 0.04]])
  '''
  # 5x5 평균 필터 커널 생성  ---②
  kernel = np.ones((5,5))/5**2
  # 필터 적용             ---③
  blured = cv2.filter2D(img, -1, kernel)
  
  # 결과 출력
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()
  plt.imshow(cv2.cvtColor(blured, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

- 전용 함수 적용 : `cv2.blur(src, ksize[, dst, anchor, borderType])`

  - src : 입력 영상
  - ksize : 커널의 크기

  ```python
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt
  
  file_name = 'img/aircraft.jpg'
  img = cv2.imread(file_name)
  print(img.shape)
  # blur() 함수로 블러링
  blur = cv2.blur(img, (10,10))
  print(blur.shape)
  
  # 결과 출력
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()
  plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)07.jpg?raw=true)

#### (2) 가우시안 블러 :

- `cv2.GaussianBlur(src, ksize, sigmaX)` : 평균이 아닌 가우시안 분포를 갖는 커널로 중앙값이 가장 크고 멀어질수록 그 값이 작아지는 커널

  - X방향 표준편차(sigmaX) :  sigmaX에 0을 전달하면 자동으로 표준편차 값을 선택해서 사용

  ```python
  import cv2 
  import matplotlib.pyplot as plt
  
  image = cv2.imread('img/abnormal.jpg')
  plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.show()
  
  dst = cv2.GaussianBlur(image, (5,5),0) #가우시안분포는 커널사이즈가 홀수크기를 적용
  plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)08.jpg?raw=true)

- **가우시안 분포(Gaussian distribution)이란? :** 

  - 표준 정규분포라고도 부르며, 좌우 대칭의 종모양으로 생긴 분포이다. (평균이 0, 표준편차가 1)

    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/1200px-Normal_Distribution_PDF.svg.png" style="zoom:50%;" />

    ```python
    import cv2 
    import matplotlib.pyplot as plt
    
    image = cv2.imread('img/abnormal.jpg')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
    
    dst = cv2.GaussianBlur(image, (5,5),0) #가우시안분포는 커널사이즈가 홀수크기를 적용
    plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    plt.show()
    ```

    

#### (3) 미디언 블러링(median Blurring) :

- 커널(Kernel) 영역 픽셀 값중에 `중간 값` 을 대상 픽셀의 값으로 선택하는 것

  ` cv2.medianBlur(src, ksize)`

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread("img/salt_pepper_noise.jpg")
  
  # 미디언 블러 적용 --- ①
  blur = cv2.medianBlur(img, 5)
  
  # 결과 출력 
  merged = np.hstack((img,blur))
  cv2.imshow('media', merged)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)09.JPG?raw=true)

#### (4) 바이레터럴 필터(BilateralFilter):

- `가우시안 필터`와 `경계 필터` 2가지를 사용하며, 블러링 필터에서 경계 라인도 흐릿하게 만들어버리는 문제를 보완하는데 사용한다. **대신 속도가 느린 단점이 있다.**

- `cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst, borderType])`

  - d : 필터의 직경 , 5보다 크면 매우 느림

  - sigmaColor : 색공간 필터의 시그마 값
  - sigmaSpace : 좌표 공간의 시그마값 (sigmaSpace와 같은 값을 권장하며, 10~150 사이 값을 권장)

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread("img/gaussian_noise.jpg")
  
  # 가우시안 필터 적용 ---①
  blur1 = cv2.GaussianBlur(img, (5,5), 0)
  
  # 바이레터럴 필터 적용 ---②
  blur2 = cv2.bilateralFilter(img, 5, 75, 75)
  
  # 결과 출력
  merged = np.hstack((img, blur1, blur2))
  cv2.imshow('bilateral', merged)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  > 원본 데이터는 사각형 1개이다.

  ![](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering)10.JPG?raw=true)



## 참고한 자료

- 도서 참고
  - 파이썬으로 만드는 Open CV 프로젝트(이세우 지음 / 프로그래밍인사이트)
  - 파이썬과 Open CV를 이용한 컴퓨터 비전 학습(알렉셰이 스피쉐보이)
  - 파이썬을 이용한 머신러닝,딥러닝 실전 앱 개발(쿠지라 히코우즈쿠에)