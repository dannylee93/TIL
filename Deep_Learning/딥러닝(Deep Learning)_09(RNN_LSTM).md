# RNN 모델과 Sequence Data

> RNN (Recurrent Neural Network) 이라는 순환신경망 모델은 텍스트(단어나 문자의 시퀀스(순서)), 혹은 일반적인 시퀀스 데이터(주식 등)를 처리하는 기본적인 딥러닝 모델이다.



*시퀀스 데이터를 살펴보기 전, 딥러닝의 **텐서**에 대해 짚고 넘어가자.*



## 딥러닝 에서 Tensor

> 신경망을 위한 데이터 표현으로서, Tensor라 부르는 다차원의 Numpy array에 데이터를 저장하는 것에서 시작한다. 즉, 텐서는 데이터를 위한 Container 이다.



#### (1) 스칼라 텐서(0D 텐서)

- 축의 개수 **0개**
- 하나의 숫자만 담고있는 텐서를 스칼라 scalar 라고 한다.
- 넘파이에서는 float32/64가 스칼라 텐서 이다.



#### (2) 벡터(1D 텐서)

- 축의 개수 **1개**

- 주의할 점:

  ```python
  x = numpy.array([1,2,3,4,5])
  
  >>> 5D벡터 == 1D텐서 (5D 벡터는 하나의 축을 따라 5개의 원소를 가졌다는 말이다.)
  ```

  

#### (3) 행렬(2D 텐서)

- 축의 개수 **2개**
- 행과 열이라는 2개의 축을 가진다.



#### (4) 3D 텐서와 고차원 텐서

- 축의 개수 **3개 이상**

  ![](https://tensorflowkorea.files.wordpress.com/2018/12/068.jpg?w=300&h=151)

#### (5) 텐서의 실제 사례

- 우리가 사용할 데이터는 대부분 다음 중 하나에 속한다.
  - **벡터 데이터**: (samples, features) 크기의 2D 텐서
  - **시계열 데이터 또는 시퀀스sequence 데이터**: (samples, timesteps, features) 크기의 3D 텐서
  - **이미지**: (samples, height, width, channels) 또는 (samples, channels, height, width) 크기의 4D 텐서
  - **동영상**: (samples, frames, height, width, channels) 또는 (samples, frames, channels, height, width) 크기의 5D 텐서



## 이 장에서 중요하게 볼 시퀀스 데이터 2가지 예시

> RNN 모델은 자연어나 음성신호, 주식은 연속적인(Sequential) 시계열(time-series) 데이터에 적합하다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F99BEDB465BD1985B100339)

#### (1) 주식가격 데이터 셋

- 1분마다 현재 주식 가격, 지난 1분 동안에 최고 가격과 최소 가격을 저장합니다. 
- 1분마다 데이터는 3D 벡터로 인코딩되고 하루 동안의 거래는 (390, 3) 크기의 2D 텐서로 인코딩됩니다(하루의 거래 시간은 390분). 
- 250일치의 데이터는 (250, 390, 3) 크기의 3D 텐서로 저장될 수 있습니다. 여기에서 1일치 데이터가 하나의 샘플이 됩니다.



#### (2) 트위터 데이터 셋

-  각 트윗은 128개의 알파벳으로 구성된 280개의 문자 시퀀스입니다. 
- 여기에서는 각 문자가 128개의 크기인 이진 벡터로 인코딩될 수 있습니다(해당 문자의 인덱스만 1이고 나머지는 모두 0인 벡터).
- 그러면 각 트윗은 (280, 128) 크기의 2D 텐서로 인코딩될 수 있습니다. 100만 개의 트윗으로 구성된 데이터셋은 (1000000, 280, 128) 크기의 텐서에 저장됩니다.



## 텍스트 데이터 다루기

> 텍스트는 가장 흔한 시퀀스 형태 데이터이다.



텍스트는 원본을 인풋으로 사용 못한다. 딥러닝 모델은 수치형 텐서만 다룰수 있어서 텍스트를 수치형 텐서로 변환하는 과정을 **텍스트 벡터화(vecterizing text)** 라고 한다.

![](https://www.hanbit.co.kr/data/editor/20190522164921_npssnrdp.jpg)

텍스트를 단어로 나누거나, 문자로 나누거나, 혹은 단어나 **문자의 n-gram을 추출**해서 벡터로 변환해야한다.

이런 **단위를 토큰**(Token)이라고 하고, **나누는 작업을 토큰화**(Tokenization)라고 한다. 나눠진 토큰을 벡터와 연결하는 방법은 `원핫 인코딩`이나 `토큰 임베딩`이 있다.



## 순환 신경망(RNN) 이해하기

> RNN과 달리 이전의 Fully-Connected layers와 CNN 모델의 신경망 특징은 각자 퍼셉트론에 메모리가 없다. 쉽게 말하자면, 그 때 그 때 처리하고 끝이란 말이다.



#### (1) 순환 뉴런(Recurrent Neurons)

RNN 모델은 한번 출력(Output)한 걸 `타임 스텝(Time Step)`마다 다시 입력으로 받는다.

![https://excelsior-cjh.tistory.com/183?category=940400](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile29.uf.tistory.com%2Fimage%2F997C79465BD1989C14D0F3)

그래서 각 퍼셉트론은 **2개의 가중치**를 가진다.(현재 타임스텝의 가중치(W<sub>x</sub>), 이전 타임스텝의 가중치(W<sub>y</sub>))



#### (2) 메모리 셀(Memory Cell)

현재 순간인 `타임스텝 t` 에서 퍼셉트론의 출력(Output)은 이전 타임스텝의 모든 입력에 대한 함수를 포함, 결국 메모리라고 볼 수 있기 때문에 메모리셀(Memory Cell)이라고도 표현한다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile25.uf.tistory.com%2Fimage%2F99C4E6485BD198EE0E301A)

일반적으로는 출력 y가 다음 layer로 진입하지만, 위의 그림과 같은 RNN은 **출력(y<sub>t</sub>)**와 **hidden state(h<sub>t</sub>)**가 구분이 되어서 다음 입력(Input)으로 **h<sub>t</sub>**가 들어간다. 이 때 RNN의 활성화 함수로 `tanh`가 주로 사용 된다.



#### (3) Input &Output 시퀀스

RNN은 아래의 그림과 같이 다양한 입력 시퀀스(sequence)를 받아 출력 시퀀스를 만들 수 있다.

![출처: https://excelsior-cjh.tistory.com/183?category=940400 [EXCELSIOR]](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile22.uf.tistory.com%2Fimage%2F99A94F465BD1990B20352F)



## RNN Cell 의 문제점

#### (1) BPTT(BackPropagation Through Time) 의 문제

 BPTT는 RNN에서의 역전파 방법이며, BPTT(BackPropagation Through Time)은 아래의 그림과 같이 **모든 타임스텝마다 처음부터 끝까지 역전파**한다.

위의 그림과 같이 RNN을 펼치게(unfold)되면 매우 깊은 네트워크가 될것이며,**그래디언트 소실 및 폭주**(vanishing & exploding gradient) 문제가 발생할 가능성이 크다. 그리고, 계산량 또한 많기 때문에 한번 학습하는데 아주 오랜 시간이 걸리는 문제가 있다.



#### (2) 장기 의존성(Long-Term Dependency) 문제

위와 같이 이전 타임스텝들의 모든 입력에 대한 함수를 메모리셀이라고 했다. 이론적으로는, RNN 모델은 이전의 모든 타임스텝이 영향을 주지만, 다음 **타임스텝은 길어질수록 영향을 주지 못하는 문제가 발생**하는데 이걸 장기의존성 문제라고 한다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile23.uf.tistory.com%2Fimage%2F99C0A53F5BD5F5C4038E7A)



## LSTM & GRU

> 장기간의 메모리를 가질 수 있는 여러 종류의 셀이 만들어졌는데, 그 중에서 대표적인 셀들이 LSTM과 GRU 셀이다.



#### (1) LSTM

> 1997년에 제안된 이 모델은 RNN 모델의 장기 의존성 문제를 해결할 뿐만 아니라 학습 또한 빠르게 수렴한다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile5.uf.tistory.com%2Fimage%2F9905CF385BD5F5EC027F20)

아까 일반 RNN 모델은 **Hidden State(h<sub>t</sub>)**가 다음 인풋으로 들어갔다고 했다. 하지만 위의 이미지에서는 `상태(state)`가 **두개의 벡터(h<sub>t</sub>, c<sub>t</sub>)**로 나누어 진다는 것을 알 수 있다.

- **h<sub>t</sub>** : 단기 상태(short-term state)
- **c<sub>t</sub>** :  장기 상태(long-term state)

핵심은 네트워크가 장기상태에서 기억을 **삭제할 부분(Forget gate)**를 지나면서 일부 메모리를 잃고, 그다음 덧셈(+) 연산으로 **Input gate**로 부터 얻은 새로운 기억을 추가한다. 이렇게 만들어진 ct는 별도의 추가 연산없이 바로 출력되고, 타임스텝 마다 연산 반복한다.



#### (2) Gru Cell

> GRU(Gated Recurrent Unit) 셀은 2014년에 K. Cho(조경현) 등에 의해 '이 논문'에서 제안된 LSTM 셀의 간소화된 버전

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=http%3A%2F%2Fcfile7.uf.tistory.com%2Fimage%2F99F0EC3E5BD5F6460255CF)

- LSTM Cell에서의 두 상태 벡터 c<sub>t</sub>와 h<sub>t</sub>가 하나의 벡터 h<sub>t</sub>로 합쳐졌다.
- 하나의 gate controller인 z<sub>t</sub>가 forget과 input 게이트(gate)를 모두 제어한다. z<sub>t</sub>가 `1`을 출력하면 forget 게이트가 열리고 input 게이트가 닫히며, 반대로 `0`일 경우 forget 게이트가 닫히고 input 게이트가 열린다.
- 즉, 이전(t - 1)의 기억이 저장 될때 마다 타임 스텝 의 입력은 삭제된다.
- GRU 셀은 output 게이트가 없어 전체 상태 벡터 가 타임 스텝마다 출력되며, 이전 상태 의 어느 부분이 출력될지 제어하는 새로운 **gate controller**인 r<sub>t</sub>가 있다



## 참고한 자료

- 케라스 창시자에게 배우는 딥러닝(François Chollet)

- 개인 자료(tistory) : https://excelsior-cjh.tistory.com/