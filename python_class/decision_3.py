import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("암거나 입력하세요: ")
if re.match(IS_NUMERIC, inp):
    x = int(inp)
    if x % 5 == 0 and x % 8 == 0:
        print(f"{x}는(은) 5와 8로 나누어 떨어집니다.")
    else:
        print(f"{x}는(은) 5와 8로 나누어 떨어지지 않습니다.")
else:
    print("정수가 아닙니다.")
