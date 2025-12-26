#0~N까지 제곱근 계산하기
import math

n = int(input("숫자를 입력하세요: "))

for i in range(n + 1):
    N = math.sqrt(i)
    print(f"{i}의 제곱근은 {N}입니다.")