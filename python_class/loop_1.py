#루프 제어 구조의 순서도
for hour in range(1,25):
    print ("현재 시간은", hour, "시입니다.")
    if hour < 12:
        print("현재 시간은 오전입니다.")
    else:
        print("현재 시간은 오후입니다.")  