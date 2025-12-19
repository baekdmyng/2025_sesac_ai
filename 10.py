'''
a = int(input())

if a > 0:
    y = 2 * a
else:
    y = -3 * a 
    
print(y)
'''
a = int(input())

if a > 30:
    print("잘못된 숫자")
else:
    if a < 10:
        y = a * 2
    elif a < 20:
        y = a / 2
    elif a < 30:
        y = a + 2
    
    print(y)    


