## 실전예제 - 그리기와 결과 저장



1. 직선 그리기
2. 사각형 그리기
3. 원 그리기
4. 호 그리기
5. 내부가 채워지지 않은 다각형
6. 내부가 채워진 다각형
7. 문자 그리기
8. 결과저장(이미지/영상)



## 직선 그리기

직선그리기 함수는 이미지나 영상 위에 단순한 선을 그린다.

```python
cv2.line(img, pt1, pt2, color, tickness=None, lineType=None, shift=None)
```

- 시작좌표(pt1) 부터 도착좌표(pt2)
- 색상 : BGR

- 비트시프트(shift) : 실수 값으로 처리할 좌표(pt)의 비트값을 지정한다.



## 사각형 그리기

사각형 그리기 함수는 주로 관심영역(ROI)를 설정하기 위한 변수값으로 활용하거나 검출된 결과를 사용자가 인식하기 쉽게 표시하는데 사용한다.

```python
cv2.rectangle(img, pt1, pt2, color, tickness=None, lineType=None, shift=None)
```

- pt1 : 좌측 상단 모서리 좌표
- pt2 : 우측 하단 모서리 좌표
- 비트시프트(shift) : 실수 값으로 처리할 모서리 좌표(pt)의 비트값을 지정한다.



## 원 그리기

주로 검출된 좌표 값을 사용자가 인식하기 쉽게 표시하는데 사용한다.

```python
cv2.circle(img, center, radius, color, tickness=None, lineType=None, shift=None)
```

- center : 원의 중심
- radius : 반지름
- 비트시프트(shift) : 실수 값으로 처리할 중심점과 반지름의 비트값을 지정한다.



## 호 그리기

주로 검출된 타원을 그리거나, 호를 그리거나, 타원 객체의 부정확한 영역을 보정하기 위해 사용한다.

```python
cv2.circle(img, center, axes, angle, startAngle, endAngle, color, tickness=None, lineType=None, shift=None)
```

- axes : 축 
  - axes.width : 장축
  - axes.height : 단축
- angle : x축 기준 시계방향으로  장축까지의 각도
  - startAngle : 시작 각도
  - endAngle : 도착 각도



## 내부가 채워지지 않은 다각형 그리기

여러 개의 다각형 곡선을 그린다.

```python
cv2.polylines(img, pts, isClosed, color, tickness=None, lineType=None, shift=None)
```

- 선 들의 묶음으로 이루어진 N개의 내부
- isClosed : 닫힘 여부 설정(첫 좌표와 마지막 좌표 연결 여부)



## 내부가 채워진 다각형 그리기

주로 복잡한 형상의 다각형을 그리거나 검출된 결과를 이미지 위에 덮어 씌울 때 사용한다.

```python
cv2.fillPoly(img, pts, color, lineType=None, shift=None, offset=None)
```

- 이미 내부가 채워져 있어, 닫힘 여부는 필요하지 않다.



## 문자 그리기

문자를 이미지에 입력하는 것이 아닌, 문자를 그리는 방식이다.

```python
cv2.putText(img, text, org, fontFace, fontScale, color, tickness=None, lineType=None, bottomLeftOrigin=None)
```

- 문자열(text)을 텍스트 박스의 좌측 상단 모서리(org)를 기준으로 그린다.
- bottomLeftOrigin : 기준좌표
  - 텍스트 박스 좌측 상단 모서리가 아닌 텍스트 박스 좌측하단 모서리를 사용할 경우 True로 지정
- OR(|) 연산자를 통해 기울임 꼴과 결합해 기울임이 적용된 글꼴로 렌더링할 수 있다.