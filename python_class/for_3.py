n = int(input("입력할 정수의 개수를 입력하세요: "))
total = 0

for i in range(n):
    a = float(input(str(i + 1) + "번째 정수를 입력하세요: "))
    total += a

if n > 0:
    average = total / n
    print(f"평균은 {average}입니다.")
    
else:
    print("입력된 정수가 없습니다.")
