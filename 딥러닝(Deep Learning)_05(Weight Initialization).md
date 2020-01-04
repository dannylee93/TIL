# Weight Initialization

> 최적화(Optimization) 만큼 중요한게 신경망에 부여하는 초기의 가중치 값 설정이다.  아래 이미지와 같이 종착지(아웃풋)가 달라지기도 한다.
>
> 대표적인 기법으로 `Xavier Initialization`, `HE Initialization`  두가지가 있다.



가중치의 초기값을 0으로 하게되면 오차 역전파에서 가중치의 값이 똑같이 갱신되기 때문에 고르게되어 노드를 만든 의미를 잃게 된다.



### 1. Xavier Initialization

>  앞 층(Layer)의 입력 노드 수에 더해 다음 층의 출력 노드 수를 함께 고려하여 초기 값을 설정하는 방법이다.

#### (1) 활성화 함수로 Sigmoid를 활용 했을 때

- `표준편차가 1`

  아래 그래프 처럼 활성화 값이 주로 0과 1쪽에 분포되어, 함수 미분 값이 0에 가까워진다. 역전파의 기울기 값은 점점 사라지며 층이 깊을수록 기울기는 더 사라진다.

  ![](https://github.com/dannylee93/Images/blob/master/Sigmoid(std_1).jpg?raw=true)

- `표준편차가 0.01`

  기울기가 사라지는 Gradient Vanishing 문제는 없지만 중앙의 0.5 주변에 치우쳐져 여러 퍼셉트론을 사용할 이유가 없어진다.(100개가 다 똑같은 Output을 보여주면 의미가 없으니까)

  ![](https://github.com/dannylee93/Images/blob/master/Sigmoid(std_0.01).jpg?raw=true)



#### (2) Sigmoid함수를 사용하며 Xavier Initialization 적용했을 때

- 앞서 설명한바와 같이 앞층의 입력 노드 수와 다음 층의 출력 노드 수를 함께 고려해서 초기 값을 설정한다.

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.random.randn(1000, 100)
node_num= 100
hidden_layer_size = 5
activations ={}

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]
        
    w = np.random.randn(node_num, node_num) / np.sqrt(node_num)
    
    a = np.dot(x, w)
    z = sigmoid(a)
    activations[i] = z
```

![](https://github.com/dannylee93/Images/blob/master/Xavier_Ini.jpg?raw=true)

> 그래프 분포를 보면 앞의 두 방식보다 고르게 분포되어 학습이 효율적으로 이루어 질 수 있음을 엿볼 수 있다. 같은 시그모이드 함수를 활용했음에도 표현력문제가 생기지 않는다.



### 2. HE Initialization

> ReLU 활성화 함수에 특화된 초기값 설정 기법이다. 앞 계층의 노드 수가 n개 일때 , 표준편차가 (√ 2/n) 인 정규분포를 사용한다.



**`ReLU`활성화 함수 짚고 넘어가기**

<img src="https://miro.medium.com/max/666/1*nrxtwp6rzqdFhgYh0x-eVw.png" style="zoom:67%;" />

> 0 이하는 0으로 출력하고 그 이상일 때는 해당 값을 출력하는 함수이다.
>
> Hidden Layers의 계층이 깊을수록 가충치 값이 0에 수렴하는 Gradient Vanishing 문제 있다.



### 3. 활성화 함수 - 가충치 초기값 설정방식 매칭

> 각 활성화 값 분포에 대한 비교이다.

#### (1) Sigmoid 함수 - Std 0.01, Xavier, He

![](https://github.com/dannylee93/Images/blob/master/Sigmoid_Standard(std_0.01).jpg?raw=true)

![](https://github.com/dannylee93/Images/blob/master/Sigmoid_Xavier(std_0.01).jpg?raw=true)

![](https://github.com/dannylee93/Images/blob/master/Sigmoid_HE(std_0.01).jpg?raw=true)

#### (2) ReLU 함수 - Std 0.01, Xavier, He

![](https://github.com/dannylee93/Images/blob/master/ReLU_Standard(std_0.01).jpg?raw=true)

![](https://github.com/dannylee93/Images/blob/master/ReLU_Xavier(std_0.01).jpg?raw=true)

![](https://github.com/dannylee93/Images/blob/master/ReLU_HE(std_0.01).jpg?raw=true)

#### (1) Tanh 함수 - Std 0.01, Xavier, He

![](https://github.com/dannylee93/Images/blob/master/Tanh_Standard(std_0.01).jpg?raw=true)

![](https://github.com/dannylee93/Images/blob/master/Tanh_Xavier(std_0.01).jpg?raw=true)

![](https://github.com/dannylee93/Images/blob/master/Tanh_HE(std_0.01).jpg?raw=true)



## 4. 참고한 자료

- 강사님 자료 (딥러닝 핵심자료 & 인공신경망 최적화 이론)
- 개인 홈페이지 (데이터 분석하는 문과생, 싸코 / https://sacko.tistory.com/)
- 책(케라스 창시자에게 배우는 딥러닝)