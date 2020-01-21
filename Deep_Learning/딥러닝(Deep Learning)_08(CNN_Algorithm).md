

# Understanding CNN Algorithm

> CNN(Convolutional neural network)은 '심층 합성곱 신경망'이라하며, 다층 퍼셉트론(Multi-layer Perceptrons)의 한 종류이다.  주로 이미지 데이터에 잘 맞는 알고리즘이며, 영상 과 음성데이터에도 충분히 활용 가능하다고 한다.



## CNN(Convolutional neural network)

<img src="http://mblogthumb2.phinf.naver.net/MjAxNzExMTdfNTIg/MDAxNTEwOTA5NDgxOTc0.pHWKTKcW5D_JdvciIV47G-CfkyLlzFzwxsG_FEeH488g.bAef3bngPGCMC5kxLoNHyNQcbXbmroDpEnVXrQ7YnKYg.PNG.samsjang/%EA%B7%B8%EB%A6%BC1.png?type=w2" alt="고양이 실험" style="zoom:80%;" />

아래 사진은 '고양이 실험' 이라는 유명한 예시이다. 일반 완전 연결층(Fully Connected Layer)처럼 한번에 모든 데이터를 보면서 학습하는 것이 아니라 , **일부 특징 있는 데이터를 보면서 학습하는 모델**을 본따 만든 모델이 바로 CNN(Convolutional neural network)이다.

<img src="https://t1.daumcdn.net/cfile/tistory/213C6141583ED6AB0A" alt="CNN 맥락 이미지" style="zoom:80%;" />

> 위 이미지는 전체적인 맥락을 이해할 수 있도록 도와주는 예시이다.



## Convolutional Layer 

> Convolutional Layer 는 Input 의 특징을 추출하는 역할을 한다. 특징을 추출하는 기능인 Filter와 필터의 값을 비선형의 값으로 바꾸어 주는 활성화 함수(Activation Function)이 있다.



<img src="https://t1.daumcdn.net/cfile/tistory/23561441583ED6AB29?download" style="zoom: 50%;" />

### (1) 필터 Filter

- 어떤 특징이 데이터에 있는지 없는지 검출해주는 함수 이다.

  <img src="https://t1.daumcdn.net/cfile/tistory/27319141583ED6AC18" style="zoom: 33%;" />

  - 우측의 `이미지 데이터`의 특징이 필터를 거치며 좌측의 `행렬 데이터`로 정의 된다.

    ![](https://t1.daumcdn.net/cfile/tistory/224E1641583ED6AC34)

    <img src="https://t1.daumcdn.net/cfile/tistory/2723C841583ED6AC23" style="zoom:67%;" />

  - 상단의 두 이미지의 예시에서 비슷한 특징인 첫번째 이미지는 상대적으로 높은 값을 가지고, 아래 이미지는 0에 수렴하는 낮은 값이 나온다.



*"필터는 Input Data 에서 특성을 판별하는 이진 분류의 값으로 나오게 되며, 그 특성을 가지고 있는지 없는지 여부를 알 수 있게 해준다."*

![00](C:\Users\bruce0809\Desktop\이미지 저장 폴더\00.JPG)

> 원본 데이터에서 필터를 통해 값들을 만들어 내는데, 얼마나 많은 값들을 만들어 낼까

- **Stride :**

  위 이미지의 질문처럼 얼마나 많은 값들을 만들어 낼지 컨트롤 하는 하이퍼 파라미터 중 하나가 Stride 이다. 쉽게 말하면, 필터가 이동하면서 특징 데이터들을 추출하는데, 얼마나 이동하면서 볼지 정하는 것이다.(default == 1)

  <img src="C:\Users\bruce0809\Desktop\이미지 저장 폴더\01.JPG" alt="01" style="zoom:67%;" />

  > 굵은 글씨로 적혀진 공식으로 Output의 데이터 크기를 빠르게 가늠할 수 있다. 이렇게 해 필터을 적용해서 얻은 결과를 Feature map 또는 Activation map 이라고 한다.

  

- **Padding:**

  통상 필터를 적용하면, 그 이후의 값은 전보다 **작아진다. **필터 적용 후, 결과 값이 작아지면 처음에 비해서 특징이 많이 유실될 수가 있다. 그러면 아직 특징이 충분히 추출 되기전에 값이 작아져 추출되지 않을 수 있다.

  이를 방지하기 위한 방법으로, `Padding`은 입력 값 주위로 데이터의 크기를 임의로 키워서 필터를 계산하게 만드는 방법이다.



***필터를 어떻게 만들까?***

 *데이터를 넣고 학습시키면, 자동으로 학습된 데이터에서 그 특징을 인식하고 필터를 만들어 낸다.*



<img src="C:\Users\bruce0809\Desktop\이미지 저장 폴더\02.JPG" alt="02" style="zoom:50%;" />

> 상단의 이미지는 6개의 (5X5X3) 필터를 사용했다. Filter와 Stride를 고려하여 (28X28X6)의 Activation maps 가 생긴 것을 볼 수 있다.

- 3차원인 Input data와 Filter를 통해서 여러 개의 2차원인 특징 맵을 추출했다.

- **How many `Weight Variavles`?**

  가중치 변수가 몇개 일까? 

  상단의 이미지는  6개의 (5X5X3) 필터를 사용했으니, `6X5X5X3`의 개수 임을 알 수 있다.





### (2) 활성화 함수 Activation function 

- 필터들을 통해서 나온 특성 맵(Feature map)으로, 활성화 함수를 적용한다. 특징맵은 정량적인 값으로 나오고, 그 특징을 `"있다 or 없다"`의 비선형 값으로 바꿔주는 과정이 필요한데, 활성화 함수가 이 역할을 한다.(아까 쥐 특징맵을 비교해서 0 or 6000 이 나온 것 처럼)

- **Sigmoid 보다 ReLU 사용하는 이유?**

  신경망이 깊어질수록 학습이 어렵다. 가중치를 역전파 할때, 시그모이드는 층이 깊어지면 `기울기 감소 Gradient Vanishing` 현상이 생긴다.



## Pooling(sub sampling)

> convolution layer를 거쳐 추출된 특징맵(Feature map) 들은 필요에 따라 Pooling 과정을 거친다. 모든 특징을 가지고 판단할 필요가 없기 때문이다.(우리가 동물 분류를 할 때 처럼) 그래서 convolution layer에서 추출된 특징맵(Feature map)을 인위로 줄이는 작업하는데, 이걸 Sub Sampling 또는 Pooling 이라고 한다.



<img src="C:\Users\bruce0809\Desktop\이미지 저장 폴더\03.JPG" alt="03" style="zoom:67%;" />

> Resize를 통해서 샘플링 하는 과정을 Pooling이라 한다. 



*max pooling, average pooling, L2-norm pooling 등이 있고, 그중에서 max pooling 이라는 기법이 많이 사용된다.*



### Max Pooling : 

<img src="https://t1.daumcdn.net/cfile/tistory/2121E641583ED6AF23" style="zoom:80%;" />

- 맥스 풀링은 특징맵(Feature map)을 MxN의 크기로 잘라낸 후, 그 안에서 **가장 큰 값**을 뽑아내는 방법이다.

- 이렇게 하는 이유의 전제는 **특징 값 중 큰 값이** 다른 부수적인 특징들을 **대표**한다는 개념을 기반으로 하는 것이다. 특징 맵(activation map)에 매번 적용하는 것이 아니라 중간에 **데이터를 줄이고 싶을 때 선택적으로 사용**하는 것이다.

  ![](https://t1.daumcdn.net/cfile/tistory/254DF041583ED6AF34)

  > Convolutional layer와 활성화 함수, Pooling 의 맥락을 전체적으로 볼 수 있고 마지막에 초록 글씨인 FC(Fully Connected layer)에서 분류되는 모습을 볼 수 있다.



## Fully connected Layer

> 앞서 컨볼루셔널 계층에서 특징 추출되면 이 특징 값을 가지고, 이제 Fully Connected layer의 계층으로 진입하면서 역전파(Back Propagation)를 통해 필터 값이 가중치 조정을 하며 학습한다.



![](https://t1.daumcdn.net/cfile/tistory/23630641583ED6B01E?download)

### Softmax Function

상단의 이미지 마지막에 적용된 Softmax Function. 이 함수도 앞에서 언급한 sigmoid나 ReLU와 같은 **활성화 함수의 일종**이다.
sigmoid나 ReLU가 이산분류(참 또는 거짓을 분류)하는 함수라면, 소프트 맥스는 **여러 개의 분류**를 가질 수 있는 함수다. 각각 x1, x2,x3 등의 특징일 확률 값을 가지고 **합하면 1**이 되는 특징이 있다.



## Tensorflow로 실습해보기 





## 출처

- [김성훈 교수님의 모두를 위한 딥러닝] https://hunkim.github.io/ml/

- [조대협의 블로그] https://bcho.tistory.com/1149 

- [구글 텐서플로우 한글화된 공식문서]

   https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/

- [머신러닝 교과서]