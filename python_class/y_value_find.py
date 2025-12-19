x = float(input("실수 값을 입력하세요: "))
y = (5+x)/x+(x+9)/(x-4)

if x == 0 or x == 4:
    print("0으로 나눌 수 없습니다.")

else:
    print("y의 값은:", y)