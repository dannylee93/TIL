PI = 3.141592

def num_input() :
	output = input("숫자 입력>> ")
	return (float(output))

def get_circumference(radius) :
	return (2 * PI * radius)

def get_circle_area(radius) :
	return (PI * radius * radius)

# 동작예시 설명 예시 및 메인에서는 출력 안되게 조건 추가
# 현재 파일이 에느리 포인트 인지 확인하고 엔트리 포인트일 때만 실행한다.
if __name__ == "__main__" :
	print("get_circumference(10): ", get_circumference(10))
	print("get_circle_area(10) ", get_circle_area(10))