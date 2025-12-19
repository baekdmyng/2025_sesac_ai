#2차 방정식 ax^2 + bx + c = 0 풀기
#해는 x = (-b ± √(b^2 - 4ac)) / 2a

import math
a = float(input("a의 값을 입력하세요: "))
b = float(input("b의 값을 입력하세요: "))
c = float(input("c의 값을 입력하세요: "))

if a == 0:
    # b가 0일 때
    if b == 0:
        if c == 0: # c가 0일 때
            print("부정")
        else:
            print("불능") #c가 0이 아닐 때
    # b가 0이 아닐 때
    else:
        x = -c / b
        print(format(x, ".2f"))
else:
    D = b**2-4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a) 
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("서로 다른 두 실근:", format(x1, ".2f"), format(x2, ".2f"))
    elif D == 0:
        x = -b/(2*a)
        print("중근:", format(x, ".2f"))
    else:
        print("허근")



