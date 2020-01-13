# OPEN CV(Basic)

> 오픈 소스 컴퓨터 비전 라이브러리 중 하나로 크로스플랫폼과 실시간 이미지 프로세싱에 중점을 둔 라이브러리 이며, 영상 관련 라이브러리로 표준 지위를 가지고 있고, 영상 처리를 대중화 시킨 1등 공신이라 한다. 상업적으로도 이용 가능하다.



## 경계검출

> `경계검출` 은 여러 수식을 이용해서 이미지를 이루고 있는 픽셀 행렬을 다른 값으로 바꾸어 이미지를 변형하는 것을 말한다.
>
> 04번 파일에 이어 이번엔 이미지에서 경계검출(필터, 침식과 팽창, 컨투어)에 대해 정리하자.



### 1. 이미지 필터링 리마인드

- **이미지 필터링(Image Filtering) :** 

  `필터(filter)` 또는 `커널(kernel)`또는 `윈도우(window)` 라고 하는 `정방행렬`을 정의하고, 이 커널을 이동시키면서 같은 이미지 영역과 곱하여 그 결과값을 이미지의 해당 위치 값으로 하는 새로운 이미지를 만드는 연산

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)00.jpg?raw=true" alt="1" style="zoom: 67%;" />

 ##### (1) 임계 처리(thresholding) : *꼭 알고 가자*

- 임계처리는 이미지 행렬에서 하나의 픽셀 값을 사용자가 지정한 `기준값(threshold)`를 사용하여 `이진화(binarization)` 하는 가장 단순한 필터(Open CV에서는 `threshold`라는 함수로 구현 되어 있다)

  - `threshold(src, thresh, maxval, type)`
  - `src` : 그레이 스케일 이미지
    - `thresh` : 기준값
    - `maxval` : 기준값을 넘었을 때 적용할 최대값
    - `type`임계처리 유형
      - `THRESH_BINARY` : 기준값을 넘으면 최대값 아니면 0
      - `THRESH_BINARY_INV` : 기준값을 넘으면 0 아니면 최대값
      - `THRESH_TRUNC` : 기준값을 넘으면 기준값 아니면 최대값
      - `THRESH_TOZERO` : 기준값을 넘으면 원래값 아니면 0
      - `THRESH_TOZERO_INV` : 기준값을 넘으면 0 아니면 원래값
  
  

  ```python
  import cv2
  from skimage.data import coins
  
  img = coins()
  
  maxval = 255
  thresh = maxval / 2
  
  _, thresh1 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY)
  _, thresh2 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY_INV)
  _, thresh3 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TRUNC)
  _, thresh4 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO)
  _, thresh5 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO_INV)
  
  titles = ['원본이미지', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
  images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
  
  plt.figure(figsize=(9, 5))
  for i in range(6):
      plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
      plt.title(titles[i], fontdict={'fontsize': 10})
      plt.axis('off')
  
  plt.tight_layout(pad=0.7)
  plt.show()
  ```

  ![2](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)01.jpg?raw=true)
  
  > 위에 `threshold` 코드에서는 기준 값을 넘을 때 주는 최대값(maxval)을 255로 주었다. 기준값은 그 값의 절반으로 객체를 임의 지정. 
  >
  > 주의 해서 볼 점은 각 인수에서 _INV가 들어가면 이미지가 역전되어 보이는 것을 알 수 있다.
 ##### (2) 적응 임계처리 :

- 일반 임계처리는 이미지 전체에 **하나의 기준 값**을 적용한다. `적응임계처리`는 일정한 **영역 내의 이웃한 픽셀들의 값들을 이용**하여 해당 영역에 적용할 기준 값을 자체적으로 생산한다.

  - `adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)`
    - `src` : 그레이스케일 이미지
    - `maxValue` – 기준값을 넘었을 때 적용할 값
    - `adaptiveMethod` : 영역 내에서 기준값을 계산하는 방법.
      - `ADAPTIVE_THRESH_MEAN_C`: 영역 내의 평균값에 C를 뺀 값을 기준값으로 사용
      - `ADAPTIVE_THRESH_GAUSSIAN_C`: 영역에 추후 설명할 가우시안 블러를 적용한 후 C를 뺀 값을 기준값으로 사용
    - `thresholdType` : 임계처리 유형
      - `THRESH_BINARY`
      - `THRESH_BINARY_INV`
    - `blockSize` : 임계처리를 적용할 영역의 크기
    - `C` : 평균이나 가중평균에서 차감할 값

```python
from skimage.data import page

img = page()

maxval = 255
thresh = 126
ret, th1 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY)

k = 15
C = 20

th2 = cv2.adaptiveThreshold(
    img, maxval, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, k, C)
th3 = cv2.adaptiveThreshold(
    img, maxval, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, k, C)

images = [img, th1, th2, th3]
titles = ['원본이미지', '임계처리', '평균 적응임계처리', '가우시안블러 적응임계처리']

plt.figure(figsize=(8, 5))
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
```

![3](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)02.jpg?raw=true)

> 위 이미지와 같이 적용 방법에 따라 다르게 처리가 되는 것을 볼 수 있다.



### 2. 경계 검출

##### (1) 소벨 필터 :

- 어윈 소벨이라는 과학자가 고안해낸 가장자리 검출 알고리즘. 3X3 행렬을 사용하여 연산할 때 중심을 기준으로 각 방향의 앞 뒤 값을 비교해서 변화량을 검출하는 알고리즘이다. (경계 검출하는 필터 중 가장 기본)

  ![4](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)03.jpg?raw=true)

  > 위 이미지와 같이 3X3 행렬을 x, y 방향별로 각각의 행렬을 가지는 형태이다.

  ```shell
  `* dst = cv2.Sobel(src, ddepth, dx, dy[, dst, ksize, scale, delta, borderType[)`
      - src : 입력 영상
      - ddepth : 출력 영상의 dtype( -1 : 입력 영상과 동일) 
      - dx, dy : 미분 차수(0, 1, 2, 둘 다 0은 안됨)
      - ksize : 커널의 크기(1, 3, 5, 7 중 선택 )
      - scale : 미분에 사용할 계수
      - delta : 연산 결과에 가산할 값 
  ```

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread("img/sudoku.jpg")
  
  # 소벨 커널을 직접 생성해서 엣지 검출 ---①
  ## 소벨 커널 생성
  gx_k = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])
  gy_k = np.array([[-1,-2,-1],[0,0,0], [1,2,1]])
  ## 소벨 필터 적용
  edge_gx = cv2.filter2D(img, -1, gx_k)
  edge_gy = cv2.filter2D(img, -1, gy_k)
  
  # 소벨 API를 생성해서 엣지 검출
  sobelx = cv2.Sobel(img, -1, 1, 0, ksize=3)
  sobely = cv2.Sobel(img, -1, 0, 1, ksize=3) 
  
  # 결과 출력
  merged1 = np.hstack((img, edge_gx, edge_gy, edge_gx+edge_gy))
  merged2 = np.hstack((img, sobelx, sobely, sobelx+sobely))
  merged = np.vstack((merged1, merged2))
  cv2.imshow('sobel', merged)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

- 아래 이미지와 같이 소벨 필터의 커널에 따라 수평 영상 주파수나 수직 영상 주파수에만 영향을 준다.

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)04.jpg?raw=true" alt="5" style="zoom:50%;" />

  > 커널사이즈를 X=1 로 설정

  ![6](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)05.jpg?raw=true)

  > 커널사이즈를  Y=1 로 설정

  ![7](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)06.jpg?raw=true)

  > 커널사이즈를 X=1 ,Y=1 로 설정

##### (2) 샤르 필터 :

- 샤르 필터는 소벨 필터와 마찬가지로 널리 사용되고 있으며, 3X3 행렬의 소벨필터 보다 더 정확한 미분 계산을 수행한다고 한다.

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)07.jpg?raw=true" alt="8" style="zoom:80%;" />

  ```shell
  `* dst = cv2.Scharr(src, ddepth, dx, dy[, dst, scale, delta, borderType]) :`
      - src : 입력 영상
      - ddepth : 출력 영상의 dtype( -1 : 입력 영상과 동일) 
      - dx, dy : 미분 차수(0, 1, 2, 둘 다 0은 안됨)
      - scale : 미분에 사용할 계수
      - delta : 연산 결과에 가산할 값
  ```

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread("img/sudoku.jpg")
  
  # 샤르 커널을 직접 생성해서 엣지 검출 ---①
  gx_k = np.array([[-3,0,3], [-10,0,10],[-3,0,3]])
  gy_k = np.array([[-3,-10,-3],[0,0,0], [3,10,3]])
  edge_gx = cv2.filter2D(img, -1, gx_k)
  edge_gy = cv2.filter2D(img, -1, gy_k)
  
  # 샤르 API로 엣지 검출 ---②
  scharrx = cv2.Scharr(img, -1, 1, 0)
  scharry = cv2.Scharr(img, -1, 0, 1)
  
  # 결과 출력
  merged1 = np.hstack((img, edge_gx, edge_gy))
  merged2 = np.hstack((img, scharrx, scharry))
  merged = np.vstack((merged1, merged2))
  cv2.imshow('Scharr', merged)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)08.JPG?raw=true" alt="9" style="zoom:50%;" />

> 잠깐!
>
> 소벨 필터는 1차 미분하는 필터이라고도 하고, 이 1차 미분 마스크는 밝기가 급격하게 변화하는 영역 뿐만 아니라 점진적으로 변화하는 부분까지 민감하게 에지를 너무 검출할 수가 있다. 
>
> 이를 보완하기 위해서 2차 미분 연산을 사용하고, 변화하는 영역의 중심에 위치한 경계 만을 검출한다.

##### (3) 라플라시안 필터 :

- 라플라시안 필터는 2차 미분 마스크의 대표격이다. 아래 이미지는 라플라시안 필터의 수식을 만족시키는 이미지이다. 특히 `(b) 8방향` 은 라플라시안 함수를 가로, 세로, 양 대각선 방향으로 모두 미분 연산을 수행할 경우를 나타내는 마스크이다.

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)10.jpg?raw=true" alt="10" style="zoom: 50%;" /> 

  ```shell
  `* dst = cv2.Laplacian(src, ddepth[, dst, ksize, scale, delta, borderType):`
      - src : 입력 영상
      - ddepth : 출력 영상의 dtype( -1 : 입력 영상과 동일) 
      - dx, dy : 미분 차수(0, 1, 2, 둘 다 0은 안됨)
      - ksize : 커널의 크기(1, 3, 5, 7 중 선택 )
      - scale : 미분에 사용할 계수
      - delta : 연산 결과에 가산할 값 
  ```

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread("img/sudoku.jpg")
  
  # 라플라시안 필터 적용 ---①
  edge = cv2.Laplacian(img, -1)
  
  # 결과 출력
  merged = np.hstack((img, edge))
  cv2.imshow('Laplacian', merged)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  <img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)09.JPG?raw=true" alt="11" style="zoom: 80%;" />
  
  > 아래 코드를 적용했을 때 결과이다. 엣지가 뚜렷하게 나오는 것을 알 수 있다.



##### (4) 캐니 엣지(Canny edges):

- 대부분의 경계 검출 필터는 노이즈에 민감하다. 작은 노이즈도 경계로 간주해서 추출한 경우가 많은데  캐니 엣지는 이러한 단점을 보완한다.

- 캐니 엣지 필터는 4가지 알고리즘으로 수행한다.

  ```shell
  단계 1.  가우시안 필터링을 하여 영상을 부드럽게 한다.
  단계 2.  Sobel 연산자를 사용하여 기울기(gradient) 벡터의 크기(magnitude)를 계산
  단계 3.  가느다란 에지를 얻기 위해 3x3 창을 사용하여 gradient 벡터 방향에서
               gradient 크기가 최대값인 화소만 남기고 나머지는 0으로 억제
  단계 4.  연결된 에지를 얻기위해 두 개의 임계값을 사용. 높은 값의 임계값을 사용하여
               gradient 방향에서 낮은 값의 임계값이 나올 때까지 추적하며 에지를 연결하는
               히스테리시스 임계값(hysteresis thresholding) 방식을 사용
  ```

- `edges = cv2.Canny(img, threshold1, threshold2, [, edges, apertureSize, L2gardient])`

  - `img` : 입력 영상, Numpy 배열
  - `threshold1, threshold2` : 스레시홀딩에 사용할 최소, 최대값
  - `apertureSize` : 마스크에 사용할 커널 크기
  - `L2gradient` : 그레이디언트 강도를 구할 방식 지정 플레그
    - True : 제곱합의 루트
    - False : 절대값 합

  ```python
  import cv2, time
  import numpy as np
  import matplotlib.pyplot as plt
  
  img = cv2.imread("img/sudoku.jpg")
  
  # 케니 엣지 적용 
  edges = cv2.Canny(img,100,200)
  
  # 결과 출력
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.show()
  
  plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![12](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)11.jpg?raw=true)

##### (5) 모폴로지:

- 구조 요소를 이용하여 반복적으로 영역을 확장시켜 떨어진 부분 또는 구멍을 채우거나, 잡음을 축소시켜 제거하는 등의 연산을 말한다. (대표적으로 침식, 팽창, 이 둘을 결합한 열기, 닫기가 있다.)

- 즉, 이진 영상(이미지)에서 흰부분(pixel=255)을 확장시키거나, 축소시키는(0) 것을 말한다. 침식과 팽창을 하는 대상을 흰 부분으로 보면 된다.

- `침식 연산`

  ```shell
  `* cv2.getStructuringElement(shape, ksize[, anchor])`
      - shape : 구조화 요소 커널의 모양 결정
          - cv2.MORPH_RECT: : 사각형
          - cv2.MORPH_ELLIPSE : 타원형
          - cv2.MORPH_CROSS : 십자형
      - ksize : 커널 크기 
      - anchor : 구조화 요소의 기준점, cv2.MORPH_CROSS에만 의미 있고 기본 값은 중심점(-1, -1)
  
  `* dst = cv2.erode(src, kernel [, anchor, iterations, borderType, borderValue])`
      - src : 입력영상, Numpy 객체, 바이너리 영상( 검은색 : 배경, 흰색 : 전경)
      - kernel : 구조화 요소 커널 객체
      - anchor : cv2.getStruchturingElement()와 동일
      - interatios : 침식 연산 적용 반복 횟수
      - borderType : 외곽 영역 보정 방법 설정 
  borserValue : 외곽 영역 보정 값
  ```

  ```python
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt
  
  img = cv2.imread('img/morph_dot.png')
  
  # 구조화 요소 커널, 사각형 (3x3) 생성 ---①
  k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
  # 침식 연산 적용 ---②
  erosion = cv2.erode(img, k)
  
  # 결과 출력
  merged = np.hstack((img, erosion))
  plt.imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![13](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)12.jpg?raw=true)

- `팽창 연산`

  ```sh
  `* dst = cv2.dilate(src, kernel[, dst, anchor, iterations, borderType, borderValue])` 
      - kernel : 구조화 요소 커널 객체
      - anchor : cv2.getStruchturingElement()와 동일
      - interatios : 침식 연산 적용 반복 횟수
      - borderType : 외곽 영역 보정 방법 설정 
      - borserValue : 외곽 영역 보정 값
  ```

  ```python
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt
  
  img = cv2.imread('img/morph_hole.png')
  
  # 구조화 요소 커널, 사각형 (3x3) 생성 ---①
  k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
  # 팽창 연산 적용 ---②
  dst = cv2.dilate(img, k)
  
  # 결과 출력
  merged = np.hstack((img, dst))
  plt.imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![14](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)13.jpg?raw=true)

- **침식과 팽창 응용**

  - `열림` = 침식 + 팽창 : 주변보다 밝은 노이즈 제거, 독립된 개체 분리, 돌출된 픽셀제거
  - `닫힘`= 팽창 + 침식 : 어두운 노이즈 제거, 끊어져 보이는 개체 연결, 구멍 메우기
  - `그레이디언트` = 팽창 - 침식 : 경계 검출
  - `탑햇` = 원본 - 열림 : 밝은 부분 영역을 강조
  - `블랙햇` = 닫힘 - 원본 : 어두운 부분 강조

  ```shell
  '* dst = cv2.morphologyEx(src, op, kernel, [, dst, anchor, iteration, borderType, borderValue])'
      - src : 입력 영상, Numpy 배열
      - op : 모폴로지 연산 종류 
          - cv2.MORPH_OPEN : 열림 연산
          - cv2.MORPH_CLOSE : 닫힘 연산
          - cv2.MORPH_GRADIENT : 그레이디언트 연산
          - cv2.MORPH_TOPHAT : 탑햇 연산
          - cv2.MORPH_BLACKHAT : 블랫햇 연산
      - kernel : 구조화 요소 커널
      - dst : 결과 영상 
      - anchor : 커널의 기준점
      - iteration : 연산 반복 횟수
      - borderType : 외곽 보정 방식
      - borserValue : 외곽 보정 값
  ```

  ```python
  import cv2
  import numpy as np
  
  img1 = cv2.imread('img/morph_dot.png', cv2.IMREAD_GRAYSCALE)
  img2 = cv2.imread('img/morph_hole.png', cv2.IMREAD_GRAYSCALE)    
  
  # 구조화 요소 커널, 사각형 (5x5) 생성 ---①
  k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
  # 열기 연산 적용 ---②
  opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
  # 닫기 연산 적용 ---③
  closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k)
  
  # 결과 출력
  merged1 = np.hstack((img1, opening))
  merged2 = np.hstack((img2, closing))
  merged3 = np.vstack((merged1, merged2))
  plt.imshow(cv2.cvtColor(merged3, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![15](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)14.jpg?raw=true)

- 모폴로지 그레디언트:

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread('img/morphological.png')
  
  # 구조화 요소 커널, 사각형 (3x3) 생성 ---①
  k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
  # 열림 연산 적용 ---②
  gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
  
  # 결과 출력
  merged = np.hstack((img, gradient))
  plt.imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![16](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)15.jpg?raw=true)

- 탑햇, 블랙햇 연산:

  ```python
  import cv2
  import numpy as np
  
  img = cv2.imread('img/moon_gray.jpg')
  
  # 구조화 요소 커널, 사각형 (5x5) 생성 ---①
  k = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
  # 탑햇 연산 적용 ---②
  tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
  # 블랫햇 연산 적용 ---③
  blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)
  
  # 결과 출력
  merged = np.hstack((img, tophat, blackhat))
  plt.imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
  plt.show()
  ```

  ![17](https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/OpenCV(Filtering2)16.jpg?raw=true)

  

## 참고한 자료

- 도서 참고
  - 파이썬으로 만드는 Open CV 프로젝트(이세우 지음 / 프로그래밍인사이트)
- 사이트 참고
  - 데이터사이언스스쿨(https://datascienceschool.net/view-notebook/c4121d311aa34e6faa84f62ef06e43b0/)
  - 소펠 필터 관련 정보(https://boysboy3.tistory.com/56)
  - 라플라시안 필터 관련 정보(https://thebook.io/006796/ch08/03/02_01/)
  - 캐니엣지 관련 정보(https://iskim3068.tistory.com/60)