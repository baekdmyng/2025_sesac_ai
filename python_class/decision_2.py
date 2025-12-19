# 주문액을 입력받고 할인율을 계산하여 할인율과 지불액을 출력하는 프로그램을 작성
amount = int(input("주문액을 입력하세요: "))

if amount < 30000:
    discount = 0
else: # 30000 이상
    if amount < 70000:
        discount = 0.05
    else: # 70000 이상
        if amount < 150000:
            discount = 0.1
        else: # 150000 이상
            discount = 0.2

pay = amount - amount * discount
print("할인율: ", discount)
print("지불액", pay)
