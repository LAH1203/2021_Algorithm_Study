# 유제품 3개를 한번에 산다면 가장 싼 것은 덤으로 지급

# 최소비용을 구하는 함수
def getMinCost(C):
    cost = 0

    # 덤으로 받을 수 있는 유제품의 개수
    freeCnt = len(C) // 3

    # 3개의 조합씩 묶어서 가장 싼 제품을 제외한 나머지 제품 더함
    for i in range(freeCnt):
        cost += C[3 * i] + C[3 * i + 1]

    # 3개의 조합이 되지 못한 나머지 것들의 가격도 더함
    for i in range(3 * freeCnt, len(C)):
        cost += C[i]

    return cost

# main
N = int(input())
C = list()
for i in range(N):
    C.append(int(input()))

# 내림차순 정렬
C = sorted(C, reverse=True)

print(getMinCost(C))