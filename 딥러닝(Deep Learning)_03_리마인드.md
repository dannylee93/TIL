# 딥러닝 관련 용어 리마인드

> 헷갈리는 용어들과 모델 학습 방법 순서등 정리하고 다시 새겨보자



*머신러닝의 모델 학습방법*

```shell
1. 데이터 전처리
2. Training set, Test set으로 나누기
3. 문제에 맞는 알고리즘 선택하고 모델링 하기
4. Training set으로 학습시키기
5. K - Folds 교차검증과 같은 검증으로 Test set과 비교하고 평균값을 확인하기
   * 테스트한 데이터셋의 정확도보다 Test set 의 정확도가 낮을 경우, 과적합(Overfitting)현상이 일어나고 있다고 볼 수 있다.(데이터를 학습하면서 암기 위주로 공부해서 응용문제 못푸는 것과 비슷한 상황이라 보자)
6. 가장 좋은 성능의 모델 채택
```



## 용어 다시 알고 넘어가자

### (1) 용어 복습하기

- `1 epoch` : 인공 신경망에서 전체 데이터가 앞으로 갔다 뒤로갔다 한바퀴 돌고 오면서 훑고 온걸 말함

  * 예를 들어, `epochs = 40` 이면 전체 데이터를 40번 뺑뺑이 돌리는 상황이다.

    그래서 적당히 돌려야 Overfitting 혹은 Underfitting 방지할 수 있음

- `Batch - size` : 한번에 너무 고생시키면 컴퓨터가 힘들어 하니까 데이터를 나눠주는데 몇 번 나눠 주는지 말해주는게 `Iteration` 이다. 이 Iteration에 부여하는 데이터 사이즈를 `Batch-size`라고 한다.

  예를 들면, 사과 100개 있는데 담는 통 몇개 둘지 정하는게 `Iteration`, 그 통안에 둘 사과의 개수가 `Batch-size`라고 하면 좋을 것 같다.

  ![](https://research.nvidia.com/sites/default/files/publications/adabatch_logo_medium.png)

### (2) 비용함수 리마인드

- 모델 학습을 할때는 비용(Cost) 오류를 최소화하는 방향으로 접근해야 한다. 비용이 최소화 되는 곳에서 성능이 가장 잘 나오며, 그 비용이 적은 부분을 찾는 것이 `최적화(Optimization)`

- 비용(손실)을 표시하는 함수:

  * 손실함수(Loss Function) 혹은 비용함수(Cost Function)

    신경망의 학습상태를 측정하는 하나의 지표로 사용한다. 가중치들의 값이 최적화 될 수 있도록 알아보기위해 손실함수로 본다손실함수라는 것 자체가 실제 데이터랑 얼마나 차이나냐를 보는건데 이게 작을수록 잘 맞다(fit)

  * 목적함수(Objective Function):

    여기서 `목적` 이라는 것은 어떤 목적을 달성하면 문제가 풀린다 의 의미인 함수인데, 상황에 따라 Maximize 하는 것이 목적일 수 있고, Minimize 하는 것이 목적일 수 있다. 여기서 Minimize하는 상황중에 사례가 손실함수(Loss Function) 혹은 비용함수(Cost Function)

  

## Loss Function(손실 함수)

### (1) 평균제곱오차(Mean Squared Error)

- 손실함수의 방법으로 가장 많이 사용 된다. 예측값과 실제값의 차이(Error)를 제곱하고 평균한 식



### (2)교차 엔트로피(Cross Entropy Error)

<img src="https://image.slidesharecdn.com/nn08-180318142641/95/-15-638.jpg?cb=1521383245" style="zoom:67%;" />

- `One-Hot-Encoding` : 정답은 1로 출력, 나머지는 0을 출력

- 사전적 정의의 Cross Entropy:

  다른 사건의 확률을 곱해서 엔트로피 계산(로그의 밑이 e인 자연로그를 예측값에 씌워서 실제 값과 곱한 후 전체 값을 합한 후 음수로 변환)

### Softmax 함수

<img src="http://www.datamarket.kr/xe/files/attach/images/24883/153/026/8cc2d67d8da963e971f87a78795e4554.JPG" style="zoom: 50%;" />

- 모든 입력신호의 영향을 받으며, 0과 1사이의 실수로 총 합이 0이 된다. 이 출력을 확률처럼 해석한다.



## Mini - Batch Learning

> 교차 엔트로피 오차(Cross Entropy Error)를 구한것 처럼 손실함수는 하나의 케이스에 대한 손실함수를 구한 Mnist 데이터 처럼 수만개의 케이스를 교차 엔트로피 오차를 통하면 그만큼(수만번) 계산해야하는 비효율이 발생한다.

<img src="http://mblogthumb4.phinf.naver.net/20150818_211/sogangori_1439883782053WkWFO_PNG/%B1%D7%B8%B225.png?type=w2" style="zoom:67%;" />

- 임의의 배치 사이즈를 만들고 그 배치 사이즈 만큼 학습 시키는게 `Mini - batch` 학습이다.

- 무작위로 추출하는 것으로 표본을 무작위로 샘플링하는 것과 개념적으로 유사하다.

  * `Full - Batch` : 전체 데이터에 대한 확률을 구하는 것

    <img src="https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&amp;fname=http%3A%2F%2Fcfile9.uf.tistory.com%2Fimage%2F9981374C5B5389B822C285" style="zoom:50%;" />

## 경사하강법(Gradient Descent)에서 수치미분과 학습률(Learning Rate)

> x축은 매개변수, y축은 비용에 대한 그래프인 경사하강법 그래프에서 x축 데이터가 바뀐만큼 비용이 얼마나 낮아졌는지 보기 위해 미분한다. 여기서 x축을 얼마나 오른쪽으로 이동시킬지 정하는 것이 학습률(Learning Rate)이다 (보통 0.01, 0.001로한다고 한다)

<img src="https://www.safaribooksonline.com/library/view/hands-on-machine-learning/9781491962282/assets/mlst_0405.png" style="zoom: 33%;" />



## 4. 참고한 자료

- 강사님 자료 (딥러닝 핵심자료 & 인공신경망 최적화 이론)
- 개인 홈페이지 (데이터 분석하는 문과생, 싸코 / https://sacko.tistory.com/)
- 책(케라스 창시자에게 배우는 딥러닝)