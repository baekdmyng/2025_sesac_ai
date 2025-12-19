# 차량 종류에 따른 요금 계산 프로그램
# BUS: 5000원, TRUCK: 3000원, CAR: 2000원, Motercycle: 1000원
# 알 수 없는 차량 종류 입력 시 오류 메시지 출력
# 사용자로부터 차량 종류 입력 받기

# .upper() 메서드를 사용하여 대소문자 구분 없이 입력 처리 
# .upper() 사용/대문자로 변경, .lower() 사용/소문자로 변경
v = input("차량 종류를 입력하세요 (BUS, TRUCK, CAR, MOTORCYCLE): ").upper()

if v == "BUS":
    print("차량 요금은 5000원 입니다.")
elif v == "TRUCK":
    print("차량 요금은 3000원 입니다.")
elif v == "CAR":
    print("차량 요금은 2000원 입니다.")
elif v == "MOTORCYCLE":
    print("차량 요금은 1000원 입니다.")
else:
    print("알 수 없는 차량 종류입니다.")
