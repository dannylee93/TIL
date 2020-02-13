# Colab 구글드라이브 연동

> 구글 코랩 사용할 때 구글 드라이브와 연동 방법, 경로 설정에 대한 정리



코랩에서 파일 경로를 지정할 때는 두 가지 방법이 있다. 

1. 내 컴퓨터의 파일 업로드
2. 구글 my-drive와 연동하기



## 내 컴퓨터에서 파일 업로드



#### View Codes

```python
from google.colab import files
uploaded = files.upload()
```

- 위의 코드를 실행하면 아래 `Output` 에 파일 선택창이 뜬다.

- 여러개를 한번에 업로드 할 수도 있다.

  ```python
  !ls
  ```

  > 위 코드로 클라우드 상에 스토리지 해당 파일 업로드 되었는지 리스트로 확인 가능하다.

- `./` 등의 경로 지정 없이 파일명만 `""` 안에 넣으면  로딩 된다.

  예를 들어,

  ```python
  import numpy as np
  
  dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")
  
  print(dataset)
  ```

  > 넘파이 모델로 파일 로딩한 예시이다. 물론 판다스로도 불러올 수 있다.



## 구글 드라이브와 연동하기



#### View Codes

```python
from google.colab import drive
drive.mount('/gdrive', force_remount=True)
```

- 위의 코드를 실행하면 아래 `Output` 에 아래 창이 뜬다.

  ```shell
  Go to this URL in a browser: https://accounts.google.com/o/oauth2/auth?----(생략)
  
  Enter your authorization code:
  ··········
  Mounted at /gdrive
  ```

  - 링크를 선택
  - 구글 계정 로그인 하면 권한 코드 생성된다.
  - 복사후 `Output` 에 붙여넣기
  - 정상적으로 진행 되었다면 `Mounted at /gdrive` 메세지가 뜬다.

- 아래 명령으로 구글 드라이브 파일 목록 확인할 수 있다.

  ```python
  !ls "/gdrive/My Drive"
  ```

  > **/gdrive/My Drive** 는 구글 드라이브와 연동할 때 기본 주소이다. 내가 추가로 폴더 내에 파일을 저장해 놨다면 `/주소` 를 적어야한다.





## References

- [캐라스 코리아 김태영님의 블로그](https://tykimos.github.io/2019/01/22/colab_getting_started/)