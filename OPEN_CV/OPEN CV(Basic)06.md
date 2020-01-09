# OPEN CV(Basic)

> 오픈 소스 컴퓨터 비전 라이브러리 중 하나로 크로스플랫폼과 실시간 이미지 프로세싱에 중점을 둔 라이브러리 이며, 영상 관련 라이브러리로 표준 지위를 가지고 있고, 영상 처리를 대중화 시킨 1등 공신이라 한다. 상업적으로도 이용 가능하다.



## 이미지 컨투어(Contour, 윤곽선)

> `컨투어(Contour)` 는 색상이나 밝기의 연속된 점을 찾아내어 모양분석 과 객체 인식에 사용하는 것으로, 동일한 색 또는 동일한 픽셀 값(강도, intensity)을 가지고 있는 영역의 경계선을 찾아내는 정보다.
>
> 05번 파일에 이어 이번엔 이미지에서 경계검출_2(컨투어)에 대해 정리하자.



### 1. 컨투어 기초

 ##### (1) 컨투어 찾기 : `findContours`

- Open CV에서 처음 컨투어 값을 찾을 때 `findcontours` 함수로 이미지의 컨투어 정보, 상하구조(hierarchy) 정보를 출력한다. 중요한 점은 흑백 이미지나 이진화된 이미지만 적용할 수 있다.

  ```shell
  images, contours, hierachy = cv2.findContours(image, mode, method)
  
  image: 흑백이미지 또는 이진화된 이미지
  mode : 컨투어를 찾는 방법
  # RETR == Retrieval(회수하다) / CountourRetrieval == 컨투어 검색방법
  cv2.RETR_EXTERNAL: 컨투어 라인 중 가장 바깥쪽의 라인만 찾음
  cv2.RETR_LIST: 모든 컨투어 라인을 찾지만, 상하구조(hierachy)관계를 구성하지 않고, list에 넣음.
  cv2.RETR_CCOMP: 모든 컨투어 라인을 찾고, 상하구조는 2 단계로 구성함
  cv2.RETR_TREE: 모든 컨투어 라인을 찾고, 모든 상하구조를 구성함(tree 계층구조로)
  method : 컨투어를 찾을 때 사용하는 근사화 방법
  # ContourChain(근사화 방법)
  cv2.CHAIN_APPROX_NONE: 모든 컨투어 포인트(윤곽점)를 반환
  cv2.CHAIN_APPROX_SIMPLE: 컨투어 라인을 그릴 수 있는 포인트만 반환
  cv2.CHAIN_APPROX_TC89_L1: Teh_Chin 연결 근사 알고리즘 L1 버전을 적용하여 컨투어 포인트를 줄임
  cv2.CHAIN_APPROX_TC89_KCOS: Teh_Chin 연결 근사 알고리즘 KCOS 버전을 적용하여 컨투어 포인트를 줄임
  ```

  

  ```shell
  drawContours 함수를 사용하면 컨투어 정보에서 비트맵 이미지를 만들 수 있다.
  
  drawContours(image, contours, contourIdx, color)
  
  image: 원본 이미지
  contours: 컨투어 라인 정보
  contourIdx: 컨투어 라인 번호
  color: 색상
  ```

  > 컨투어 정보는 컨투어를 구성하는 점들로 이루어진 배열의 리스트이다. 리스트의 원소 갯수는 컨투어 갯수와 같다.

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering3)00.jpg?raw=true" alt="0" style="zoom:67%;" />

  > 위 이미지는 `drawcontour`를 사용했을때 변환되는 이미지이다.

- 컨투어 기초 샘플 코드:

  ```python
  import cv2 
  import matplotlib.pyplot as plt 
  
  image = cv2.imread('img/man_face.jpg')
  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #그레이 형태로 불러옴 
  ret, thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY) #이진화 처리 
  
  plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
  plt.show()
  
  contours, hierarchy  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
  # 모든 컨투어를 그린다.
  image = cv2.drawContours(image, contours, -1, (0,255,0), 4) # -1은 전체의 컨투어
  
  plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![1](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering3)01.jpg?raw=true)

 ##### (2) 컨투어의 상하구조(hierarchy)? :

-  `1, 0, -1` 값으로 이루어진 `컨투어의 수 * 4`  크기의 행렬(말하자면, 1X4 행렬의 아웃풋)
  - 1번 원소: 같은 수준의 다음 컨투어의 인덱스. 같은 수준의 다음 컨투어가 없으면 -1
  - 2번 원소: 같은 수준의 이전 컨투어의 인덱스. 같은 수준의 이전 컨투어가 없으면 -1
  - 3번 원소: 하위 자식 컨투어의 인덱스. 가장 하위의 컨투어면 -1
  - 4번 원소: 부모 컨투어의 인덱스. 가장 상위의 컨투어면 -1

- 컨투어(Contour)의 계층 구조는 `hierarchy` 에 담겨있다. 윤곽선의 `포함관계 여부`를 나타낸다.

  - `[다음 윤곽선, 이전 윤곽선, 내곽 윤곽선, 외곽 윤곽선]`에 대한 인덱스 정보를 포함하고 있다.

  - 계층정보 예시 :

    <img src="https://076923.github.io/assets/images/Python/opencv/ch21/2.png" style="zoom:67%;" />

    ```python
    0 [ 2 -1  1 -1]
    1 [-1 -1 -1  0]
    2 [ 4  0  3 -1]
    ```

    > `print(i, hierachy[0][i])`을 통하여 3개의 윤곽선을 출력한 결과이다. 보는 바와 같이 다음윤곽선과 이전윤곽선의 정보가 `-1` 이 아니라면 동등한 계층이다.(2번 마름모 참고) 
    >
    > 0번과 1번 인덱스를 보고 Output의 3열,4열을 비교해보자.

- 컨투어의 계층 구조 샘플 코드:

  ```python
  import cv2
  import numpy as np
  
  # 영상 읽기
  img = cv2.imread('img/shapes_donut.png')
  img2 = img.copy()
  # 바이너리 이미지로 변환
  imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
  
  # 가장 바깥 컨투어만 수집   --- ①
  contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, \
                                                  cv2.CHAIN_APPROX_NONE)
  # 컨투어 갯수와 계층 트리 출력 --- ②
  print(len(contour), hierarchy)
  
  # 모든 컨투어를 트리 계층 으로 수집 ---③
  contour2, hierarchy = cv2.findContours(imthres, cv2.RETR_TREE, \
                                              cv2.CHAIN_APPROX_SIMPLE)
  # 컨투어 갯수와 계층 트리 출력 ---④
  print(len(contour2), hierarchy)
  
  # 가장 바깥 컨투어만 그리기 ---⑤
  cv2.drawContours(img, contour, -1, (0,255,0), 3)
  # 모든 컨투어 그리기 ---⑥
  for idx, cont in enumerate(contour2): 
      # 랜덤한 컬러 추출 ---⑦
      color = [int(i) for i in np.random.randint(0,255, 3)]
      # 컨투어 인덱스 마다 랜덤한 색상으로 그리기 ---⑧
      cv2.drawContours(img2, contour2, idx, color, 3)
      # 컨투어 첫 좌표에 인덱스 숫자 표시 ---⑨
      cv2.putText(img2, str(idx), tuple(cont[0][0]), cv2.FONT_HERSHEY_PLAIN, \
                                                              1, (0,0,255))
  
  # 화면 출력
  cv2.imshow('RETR_EXTERNAL', img)
  cv2.imshow('RETR_TREE', img2)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  > 위의 코드를 실행하면 다음과 같이 결과가 출력된다.

  ```python
  3 [[[ 1 -1 -1 -1]
    [ 2  0 -1 -1]
    [-1  1 -1 -1]]]
  6 [[[ 2 -1  1 -1]
    [-1 -1 -1  0]
    [ 4  0  3 -1]
    [-1 -1 -1  2]
    [-1  2  5 -1]
    [-1 -1 -1  4]]]
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering3)04.jpg?raw=true" alt="6" style="zoom:67%;" />

### 2. 컨투어의 특징

 ##### (1) 이미지 모멘트 : `moments`

- `윤곽선(contour)`이나 `이미지(array)`의 **0차 모멘트**부터 **3차 모멘트**까지 계산하는 알고리즘.
- 이미지 모멘트는 컨투어에 관한 특징 값을 말한다. Open CV에서 `moments` 함수로 이미지의 모멘트를 구한다. 컨투어 포인트 **배열을 입력**하면 해당 컨투어의 모멘트를 `dict 타입`으로 반환한다. 

- 반환하는 모멘트는 **총 24개**로 **10개의 위치 모멘트**, **7개의 중심 모멘트**, **7개의 정규화된 중심 모멘트**로 이루어져 있다.

  ```shell
  Spatial Moments : M00, M01, M02, M03, M10, M11, M12, M20, M21, M30
  Central Moments : Mu02, Mu03, Mu11, Mu12, Mu20, Mu21, Mu30
  Central Normalized Moments : Nu02, Nu03, Nu11, Nu12, Nu20, Nu21, Nu30
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering3)03.jpg?raw=true" style="zoom:67%;" />

- ```python
  In [8]:
  c0 = contours[0]
  M = cv2.moments(c0)
  M
  ------------------------------------
  Out []:
  {'m00': 42355.0,
   'm10': 7943000.166666666,
   'm01': 6115675.833333333,
   'm20': 1914995009.1666665,
   'm11': 1043128904.8333333,
   'm02': 1041817606.0,
   'm30': 517465951777.85004,
   'm21': 233874687443.69998,
   'm12': 169430720481.3,
   'm03': 200904428563.85,
   'mu20': 425412866.6175771,
   'mu11': -103767899.87557864,
   'mu02': 158769774.61250484,
   'mu30': -1219318387.8395386,
   'mu21': -3713125246.697487,
   'mu12': 4020833974.2852783,
   'mu03': 4625649126.278534,
   'nu20': 0.2371380524771235,
   'nu11': -0.0578433790256196,
   'nu02': 0.08850309451896964,
   'nu30': -0.003302595676372647,
   'nu21': -0.010057218449154588,
   'nu12': 0.010890665663146169,
   'nu03': 0.012528843128440374}
  ```

  > 상단에는 임의의 사진에 대한 모멘트 출력 예시이다. 컨투어의 이미지 모멘트를 간단히 출력 해보면 상단의 블럭과 같이 정보를 출력한다.

- 컨투어의 **면적**은 모멘트의 `m00` 값이고, `cv2.contourArea()` 함수로도 구할 수 있다.

  ```python
  In [9]:
  cv2.contourArea(c0)
  ------------------------------------
  Out []:
  42355.0
  ```

- 컨투어의 **둘레**는 `arcLength` 함수로 구할 수 있다. 두번째 파라미터인 closed의 의미는 폐곡선의 여부로, 설정한 값이 True 일 때는 컨투어의 시작점과 끝점을 이어 도형을 구성하고 그 둘레 값을 계산한다. False인 경우 시작점과 끝점을 잇지 않고 둘레를 계산한다.

  ```python
  In [10]:
  cv2.arcLength(c0, closed=True), cv2.arcLength(c0, closed=False)
  ------------------------------------
  Out []:
  (2203.678272008896, 2199.678272008896)
  ```

- 컨투어를 둘러싸는 박스는 `boundingRect` 함수로 구한다.

  > 아래 2개의 입출력된 파이썬 코드들을 보고 맥락만 이해하자

  ```python
  In [11]:
  x, y, w, h = cv2.boundingRect(c0)
  x, y, w, h
  ------------------------------------
  Out []:
  (18, 9, 371, 304)
  
  ------------------------------------
  In [12]:
  plt.plot(x0, y0, c="b")
  plt.plot(
      [x, x + w, x + w, x, x], 
      [y, y, y + h, y + h, y],
      c="r"
  )
  plt.show()
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering3)02.jpg?raw=true" alt="4" style="zoom:67%;" />

- 모멘트를 이용한 `중심점`, `넓이`, `둘레길이` 구하기:

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread("img/shapes.png")
  # 그레이 스케일 변환
  imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # 바이너리 스케일 변환
  ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
  # 컨투어 찾기
  _, contours, hierachy = cv2.findContours(th, cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_SIMPLE)
  
  # 각 도형의 컨투어에 대한 루프
  for c in contours:
      # 모멘트 계산
      mmt = cv2.moments(c)
      # m10/m00, m01/m00  중심점 계산
      cx = int(mmt['m10']/mmt['m00'])
      cy = int(mmt['m01']/mmt['m00'])
      # 영역 넓이
      a = mmt['m00']
      # 영역 외곽선 길이
      l = cv2.arcLength(c, True) # True값은 외곽선의 닫힘 여부 출력
      # 중심점에 노란색 점 그리기
      cv2.circle(img, (cx, cy), 5, (0, 255, 255), -1)
      # 중심점 근처에 넓이 그리기
      cv2.putText(img, "A:%.0f"%a, (cx, cy+20) , cv2.FONT_HERSHEY_PLAIN, \
                                                              1, (0,0,255))
      # 컨투어 시작점에 길이 그리기
      cv2.putText(img, "L:%.2f"%l, tuple(c[0][0]), cv2.FONT_HERSHEY_PLAIN, \
                                                              1, (255,0,0))
      # 함수로 컨투어 넓이 계산해서 출력 # True : 방향에 따라 음수, False : 절대값
      print("area:%.2f"%cv2.contourArea(c, False)) 
  
  # 결과 출력
  cv2.imshow('center', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering3)05.jpg?raw=true" alt="7" style="zoom:80%;" />



*컨투어 심화(추가적으로 활용할만한 메소드) 추가정리 하기* 



## 참고한 자료

- 강사님 자료 (이미지분석 인공지능 서비스 개발 / 최진영 강사님)
- 사이트 참고
  - 데이터사이언스스쿨(https://datascienceschool.net/view-notebook/f9f8983941254a34bf0fee42c66c5539/)
  - 이미지 컨투어 관련 정보(https://076923.github.io/posts/Python-opencv-21/)
  - 컨투어의 계층구조 관련 정보(https://076923.github.io/posts/Python-opencv-22/)
  - 모멘트 관련 정보(https://076923.github.io/posts/Python-opencv-25/)