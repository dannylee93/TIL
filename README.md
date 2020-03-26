# Today I Learned
> Summarize what I Learned today to record the process of my development for becoming a Data-related Expert

<p align="center"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ8FJR6cjcfy0w3APFLG9kPQaHB6u-b3njRrYJ1rVNZ4xAwrZ3l"/></p>

<br>

## Crawling

Add Comment soon

```python
# 2.크롤러 모델링
td_data = []

for nums in range(1, 1342, +1):
    page = requests.get("URL-주소(임의 변경)".format(nums))
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('tbody')
    th_data = [item.get_text().strip() for item in table.select('th')]
    td_data.append([item.get_text().strip() for item in table.select('td')])
```

- **Reference Resources :** [새로비] https://engkimbs.tistory.com/

<br>

## Deep_Learning

Add Comment soon

<p align="center"><img src=https://camo.githubusercontent.com/8ddd25193f1e31e571129ec4b0b3fe4451e3ee67/68747470733a2f2f6d69726f2e6d656469756d2e636f6d2f6d61782f3435332f312a353144304d7174714875336832765445356f4a2d37672e706e67></p>

- **Reference Resources :** 
  - 모두를 위한 머신러닝 & 딥러닝 https://hunkim.github.io/ml/
  - 데이터 분석하는 문과생, 싸코 https://sacko.tistory.com/
  - 조대협 님 블로그 https://bcho.tistory.com/1149

<br>

## Git&Github

Add Comment soon

<p align="center"><img src="https://evan-moon.github.io/2019/07/25/git-tutorial/thumbnail.png"></p>

- **Reference Resources :**
  - Original :
  - Translated :

<br>

## OPEN_CV

Add Comment soon

```python
# 브로드캐스팅과 형식캐스팅 한번에 실험하기

import numpy as np

# 브로드 캐스팅 : 서로 다른 배열에서도 산술 연산 가능
array_1 = np.array([1,2,3,4]).reshape(2,2)
array_2 = np.array([1.5, 2.5])

# 형식 캐스팅 : 데이터 타입이 자연스럽게 변환된다.
add = array_1 + array_2

print(add)
===============================================
[[2.5 4.5]
 [4.5 6.5]]
```

- **Reference Resources :** 

<p align='center'><img src=http://image.kyobobook.co.kr/images/book/large/669/l9791158391669.jpg><img src=http://image.kyobobook.co.kr/images/book/large/410/l9788966262410.jpg></p>

<br>

## Practice_CodingChallenges

Add comment soon

```python
def d(n):                   # d(n)이라는 문제부터 정의한다.
    a = 0                   # a를 0으로 두면서 디폴트랑 속성 생성
    for x in list(str(n)):  # n의 숫자를 쪼개서 for문으로 하나씩 넣어줌
        a = a + int(x)      # 0에 쪼개진 숫자를 더해줌
    return int(n) + a       # 원래 숫자(int)에 a를 더해줌
a= []
for i in range(1,10001):    # 1~10000의 숫자를 내가 정의한 d(n)에 넣어 계산하고
    k = d(i)
    a.append(k)             # a라는 깡통 리스트 객체에 넣는다. == 생성자 가진 숫자들 모임

for b in range(1, 10001):   # 1~10000까지 숫자에서 뽑은게       
    if b in a:              # a에 있다면 지나치고, 없으면 프린트 해라.
        pass
    else:
        print(b)
# d(n) 이라는 함수를 정의한다 : a라는 곳에
```

<br>

## Python_Basic

Add comment soon

<br>

## References

Add comment soon

```python
from google.colab import drive
drive.mount('/gdrive', force_remount=True)
```

> Colab 구글드라이브 연동.md

```python
import matplotlib.pyplot as plt
%matplotlib inline

# figre크기
plt.rcParams["figure.figsize"] = (14,4)

# 선 두께
plt.rcParams['lines.linewidth'] = 2

# 선 색깔
plt.rcParams['lines.color'] = 'r'

# 차트의 격자 표시 유무
plt.rcParams['axes.grid'] = True
```

> Change_default_matlplotlib.ipynb

