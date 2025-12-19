# 윤년 계산하기
'''
연도를 입력받고 해당 연도가 윤년인지 아닌지 여부 판단 및 출력
'''

import re
IS_NUMERIC = "^[-+]?\\d+(\\.\\d+)?$"

inp = input("년도를 입력하세요: ")
if re.match(IS_NUMERIC, inp):
    year = int(inp)
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        print(year, "윤년입니다.")
    else:
        print(year, "윤년이 아닙니다.")
else:
    print("오류 발생")