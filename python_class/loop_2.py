#1부터 100까지의 합 계산하기

# while 문을 사용한 예제
s = 0
i = 1

while i <= 100:
    s = s + i
    i+= 1
print("1부터 100까지의 합은", s, "입니다.")

# for 문을 사용한 예제

s = 0

for i in range (1, 101):
    s += i
    print("1부터 100까지의 합은", s, "입니다.")