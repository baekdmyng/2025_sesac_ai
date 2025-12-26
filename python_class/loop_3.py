'''
x,y 값 찾기
-20 ~ 20 범위 내에서 다음 방정식을 만족하는 x, y 의 정숫값을 찾아 출력한다.
x*x + 6*y*y = 6
'''

for x in range(-20, 21):
    for y in range(-20, 21):
        if x*x + 6*y*y == 6: # x**2 + 6y**2 == 6
            print(x, y)
            
    
