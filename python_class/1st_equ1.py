# 일차 방정식 ax+b=0의 해 구하기
# x = -b/a 
# a가 0일 때는 방정식이 성립하지 않음

a = float(input("a의 값을 입력하세요: "))
b = float(input("b의 값을 입력하세요: "))

if a == 0 or b == 0:
    print ("방정식이 성립하지 않습니다.")
else:
    x = - b/a
    print(x)

