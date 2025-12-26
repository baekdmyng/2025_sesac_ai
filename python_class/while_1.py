#while문을 이용해 숫자 네 개를 입력 받아 총합을 구하고 출력한다.
i = 1
total = 0

while i <= 4:
    num = int(input("정수를 입력하세요: "))
    total += num
    i += 1
print("네 수의 총합은:", total)

    
