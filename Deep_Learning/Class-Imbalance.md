# Class Imbalance

> 현실 데이터에서 클래스 불균형 문제 다루기

어떤 데이터에서 각 클래스가 가지고 있는 데이터의 양의 차이가 있을 때 클래스 불균형이 있다고 한다. 병원에서 질병이 있는 사람과 질병이 없는 사람의 데이터를 수집하면 일반적으로 질병이 없는 사람의 데이터가 현저히 많을 것이다.

## Problem Solve

> 문제를 해결하는 두 가지 테크닉

### (1) Weight balancing

```python
import keras

class_weight = {"buy": 0.75,
                "don't buy": 0.25}

model.fit(X_train, Y_train, 
		  epochs=10, batch_size=32,
		  class_weight=class_weight)
```

> Keras의 fit 단계에서 파라미터를 조정할 수 있다.

- 클래스 비율에 따라 가중치를 두는 방법

  - 데이터의 비율이 1:9 일 때 가중치를 9:1로 변경해서 전체 loss에 반영

-  [Focal loss](https://arxiv.org/pdf/1708.02002.pdf) 를 사용하는 방법

  <img src="https://t1.daumcdn.net/cfile/tistory/99B35F3F5D04A7802C" alt="img" style="zoom:50%;" />

  - 어떤 batch 의 트레이닝 데이터에 같은 weight 를 주지 않고, 분류 성능이 높은 클래스에 대해서는 down-weighting 을 한다.

  - gamma (위 그림) 를 주어, 이 down-weighting 의 정도를 결정한다.

    ```python
    import keras
    from keras import backend as K
    import tensorflow as tf
    
    # Define our custom loss function
    def focal_loss(y_true, y_pred):
        gamma = 2.0, alpha = 0.25
        pt_1 = tf.where(tf.equal(y_true, 1), y_pred, tf.ones_like(y_pred))
        pt_0 = tf.where(tf.equal(y_true, 0), y_pred, tf.zeros_like(y_pred))
        return -K.sum(alpha * K.pow(1. - pt_1, gamma) * K.log(pt_1))-				K.sum((1-alpha) * K.pow( pt_0, gamma) * K.log(1. - pt_0))
    
    # Compile our model
    adam = Adam(lr=0.0001)
    model.compile(loss=[focal_loss], metrics=["accuracy"], optimizer=adam) 
    ```

### (2) Over and under sampling

<img src="https://t1.daumcdn.net/cfile/tistory/99AC31455D04AA9923" alt="img" style="zoom:67%;" />

- 샘플링 방법을 이용(기존의 데이터를 복사하는 방법으로 적용된다.)

## 출처

- https://3months.tistory.com/414 [Deep Play]