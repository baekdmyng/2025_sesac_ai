#최솟값과 최댓값 검증하고 찾기: 10명의 몸무게를 입력받고 1~100 사이일 때만 가장 많이 나가는 몸무게를 출력한다
min_weight = 100
max_weight = 1
num = 10
weights = []

for i in range(num):
    weights.append(int(input()))
    if weights[i] < min_weight and 1 <= weights[i] <= 100:
        min_weight = weights[i]
    if weights[i] > max_weight and 1 <= weights[i] <= 100:
        max_weight = weights[i]