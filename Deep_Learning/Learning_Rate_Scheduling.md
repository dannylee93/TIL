# Learning Rate Scheduling



![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_learning_rates_header.png)



## Adam Optimizer



#### view Codes

```python
# decay에서 전체 에포크 수로 나누었음.(a common rule of thumb)
opt = SGD(lr=1e-2, momentum=0.9, decay=1e-2/epochs)
```

> 케라스 내부적으로 각 배치마다 학습률 업그레이드 한다고 생각하지만 표준적으로 감소하지 않는다고 한다. 그래서 `decay` 를 직접 부여한다.



1. **momentum** (β1 : momentum decay rate`(default : 0.9)`)

   ![](https://media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-1-4842-4470-8_33/MediaObjects/463852_1_En_33_Fig1_HTML.jpg)

   > 모멘텀(관성)을 알고리즘에 추가로 부여해서 가중치의 변화를 제어

2. **Learning Rate Schduling**

   ![](https://1.bp.blogspot.com/-OKPqU48zyBI/WXlHw47OxiI/AAAAAAAALKU/nxgTgdnl7ksSAF4KRHvmp0UlVL8SooH1ACK4BGAYYCw/s1600/o4.PNG)

   > minimum에 가까워 질수록 학습률을 조정(Decay)하면서 세밀하게 학습한다.



**Adam Optimizer is combination of proper momentum & Learning Rate Schduling**



## Learning Rate Decay



#### Why adjust our learning rate and use learning rate schedules?

1. 학습률은 하이퍼 파라미터 튜닝에서 **가장 중요한 요인**으로 작용하기도 한다.

   - 너무 작으면, 신경망이 학습을 전혀 하지 못한다.

   - 너무 크면,  Overshoot 된다(학습할 수 있는 지역)을 벗어난다.

     ![](https://www.pyimagesearch.com/wp-content/uploads/2019/08/learing_rate_finder_lr_plot.png)

2. LR Scheduling이 모델의 정확도를 높이고 손실이 적은 영역이 되는 유용한 방법임을 알아채려면 신경망에서 사용되는 **표준 가중치 업데이트** 공식을 봐야한다.

   ![](https://www.pyimagesearch.com/wp-content/latex/8d2/8d23f6dc734ab53419a7e73ea7952295-ffffff-000000-0.png)

3. 일반적으로, 대부분 사용하는 초기 학습률은 모듈에 **[1e-1, 1e-2, 1e-3]**으로 있다. 그리고 신경망은 고정된 에포크 수(내가 지정한 하나의 에포크 수)에 따라 **학습률 변화없이 사용된다**.



####  view the process of learning rate scheduling as:

1. 더 잘 학습하는 그 학습률을 train 과정 *초기에 찾기*
2. *학습속도를 줄여보면서* 더 최적의 가중치 찾기



### **how to implement and utilize a number of learning rate schedules?**

1. *The decay schedule built into most Keras optimizers*
2. *Step-based learning rate schedules*
3. *Linear learning rate decay*
4. *Polynomial learning rate schedules*
5. *Exponential learning rate schedules*



#### 2. Step-based learning rate schedules

![img](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_learning_rates_drop_scheduling.png)

> 특정 Epoch 당 학습률이 감소하는 패턴을 Step-based 라고 한다.



#### 3. Linear learning rate decay

![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_learning_rates_linear_output.png)

> (*left*) shows that our learning rate is decreasing linearly over time while (*right*) visualizes our training history.



#### 4.  Polynomial learning rate decay

![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_learning_rates_poly_output.png)

> (*left*) visualizes the fact that our learning rate is now decaying according to our polynomial function while (*right*) plots our training history.



1. 다항식 함수 파라미터에 기반해 학습률이 감소한다.
2. 선정한 지수(exponent)가 클 수록 빠르게 감소한다.
3. 다항식의 힘`power==1.0`으로 하면 선형적 감소를 사용한다는 뜻 / 다항은 숫자를 높이면됨(5.0써보기)



#### What is the POINT??

 *initial learning rate(초기 학습률) & total number of epochs(에포크 수 변경) 위 두가지를 통해 적절한 학습률을 결정해야한다.*





## Cyclical Leaning Rate

> 학습률 감소의 방법 중 하나로, 지수 감소법과 주기적 학습률 감소법 이 있다. 여기에서는 주기적 학습률 감소법의 발전된 예시로 Cyclical Leaning Rate에 대해 다룬다.



#### How do we use Cyclical Learning Rates?

![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_clr_learning_rate_variations.png)

> **Cyclical** learning rates **seek to handle training issues** when your learning rate is too high or too low shown in this figure.



## 3 ways for Policy

> [Cyclical Learning Rates for Training Neural Networks - Leslie N. Smith /Cornell Univ.](https://arxiv.org/abs/1506.01186)



![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_clr_saddle_points.png)

단조로운 학습률 감소는 위와 같은 데이터 분포에서 **Local Minima**에 갇힐 수 있는 문제가 발생한다. 학습률을 주기적으로 변형하면서 [**학습률 초기값**]으로 부터 자유로워질 수 있고,  Local Minima에서 벗어나며, 하이퍼파라미터 튜닝 실험 횟수를 줄일 수 있다.

#### The “triangular” policy

![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_clr_triangular.png)

> The “triangular” Cyclical Learning Rate policy is a simple triangular cycle.

#### The “triangular2” policy

![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_clr_triangular2.png)

>  “triangular2” policy is **cuts** the max learning rate bound in **half** after every cycle.

#### The “exp_range” policy

![](https://www.pyimagesearch.com/wp-content/uploads/2019/07/keras_clr_exp_range.png)

>  The “exp_range” cyclical learning rate policy undergoes **exponential decay** for the max learning rate bound while still exhibiting the “triangular” policy characteristics.



#### HOW Do we know MIN & MAX Learning Rates??



## Learning Rate Finder

> pytorch 기반의 fast.ai 를 활용하는 LR Finder 메소드로서, 학습이 잘 되는 구간을 찾을 수 있다.



Learning Rate Scheduling을 통해서 적절한 학습률 과 에포크의 설정이 학습에 영향을 끼친다는 것을 알았다.

그러면 `적정 학습률` 을 어떻게 찾을 수 있을까?

### Network Architecture

![](https://www.pyimagesearch.com/wp-content/uploads/2019/08/keras_learning_rate_finder_algorithm.png)

#### The automatic learning rate finder algorithm works like this:

- **Step #1:** 엄청 작은(1e-10) / large(1e+1) LR 바운드가 있다

  -  We start by defining an upper and lower bound on our learning rate. The lower bound should be very small (1e-10) and the upper bound should be very large (1e+1).

- **Step #2:** 신경망 학습을 시작한다.

  - After each batch update, we exponentially increase our learning rate.

- **Step #3:** 학습률을 증가(지수)시킨다 

  - Typically, this entire training process/learning rate increase only takes 1-5 epochs.

- **Step #4:** 각 배치가 끝날 때마다 loss와 학습률을 기록한다

  - Just large enough for loss to decrease
  - And too large, to the point where loss starts to increase.

  ![](https://www.pyimagesearch.com/wp-content/uploads/2019/08/learing_rate_finder_lr_plot.png)

  > Fashion MNIST 예제에서 적정 학습률을 찾은 샘플 그래프

- **Step #5:** n개의 에포크를 훈련해본다.

- **Step #6:** loss와 학습률을 구성한다.

- **Step #7:** 그 구성(plot)을 검토하고, 최적의 학습률 값을 식별한다.

- **Step #8:** 학습률 값을 업데이트

- **Step #9:** 전체를 학습한다.





## 이론 실험해보기



### View Codes of Modeling codes First:

```python
model=Sequential()

model.add(Dense(64,input_shape=(20, ))) # input dimension
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.1))

model.add(Dense(128))
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.1))

model.add(Dense(256))
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.1))

model.add(Dense(128))
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.1))

model.add(Dense(128))
model.add(LeakyReLU(alpha=0.1))
model.add(Dropout(0.4))

model.add(Dense(num_classes, activation='softmax'))
```

> 5 Layer의 DNN 과 활성화 함수로는 Leaky-ReLU 를 사용했다.

```python
model.fit(x_train, y_train, batch_size=38, epochs=50, verbose=2,validation_split=0.25)
```

> 상단의 모델링 코드와 fitting에서의 파라미터는 동일하게 적용했다.



#### View Codes :

1. **일반 adam 옵티마이저 적용했을 때**

   ```python
   # 모델 훈련
   model.compile(loss='categorical_crossentropy', optimizer= 'adam', metrics=['accuracy'])
   ```

   ![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_00.jpg?raw=true)

   > Loss: 0.4180  / Accuracy: 0.8600



2. **adam 옵티마이저에 파라미터 추가 적용했을 때**

   ```python
   optimizer_adam = adam(lr=0.001, clipvalue=1.0, decay=1e-8/epochs)
   ```

   - `clipvalue` = Gradient Clipping
     - 말 그대로 기울기 값을 자르는 것이다. 파라미터 조정이 크게 크게 변하지 않게(급경사를 지나 정지하지 않게) 충분히 작은 step을 반들수 있도록 최대한 **최적화 알고리즘의 방향을 유지하면서 업데이트 되어야 하는 step의 크기(Learning Rate)를 제어** 해준다.

   ![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_01.jpg?raw=true)

> Loss: 0.4035  / Accuracy: 0.8609

3. **Linear / Polynomial Decay 적용했을 때**

   ```python
   from tensorflow.keras.optimizers.schedules import PolynomialDecay
   
   starter_learning_rate = 0.001
   end_learning_rate = 0.0001
   decay_steps = 10000
   
   learning_rate_fn = PolynomialDecay(initial_learning_rate= starter_learning_rate, 
                                      decay_steps= decay_steps,
                                      end_learning_rate= end_learning_rate,
                                      power=1.0,
                                      cycle=False)
   ```

   > 초기 값, step, 학습 끝난 상태에서의 마지막 값을 지정한다. (아직 실험 중 / 내부 알고리즘 오류)

4. **Cyclical Learning Rate 적용**

   ```python
   # import CyclicLR
   clr = CyclicLR(base_lr=0.00001, max_lr=0.001, step_size=8, mode='exp_range')
   ```

   ![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_03-1.jpg?raw=true)

> Loss: 0.3990 / Accuracy: 0.8619

![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_03-2.jpg?raw=true)

5. Learning Rate Finder로 최적의 학습구간 찾기

   ```python
   from keras_lr_finder import LRFinder
   
   lr_finder = LRFinder(model)
   lr_finder.find(x_train, y_train, 0.0001, 1, 200, 5)
   ```

   ![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_04.jpg?raw=true)

> 10<sup>-4</sup> 에서 10<sup>-2</sup> 사이에서 최적의 학습을 하는 것으로 보인다.



6. adam 옵티마이저에서 최적의 학습률을 적용했을 때

   ```python
   optimizer_adam = adam(lr=0.01, clipvalue=1.0, decay=1e-4)
   ```

   ![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_05.jpg?raw=true)

   

7. adam 옵티마이저와 cyclic LR을 적용했을 때

   ![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_06-1.jpg?raw=true)

   > Loss: 0.3910 / Accuracy: 0.8655

   ![](https://github.com/dannylee93/Images/blob/master/Other/%EC%8B%A4%ED%97%98_06-2.jpg?raw=true)

