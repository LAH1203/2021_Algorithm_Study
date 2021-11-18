# 주식 하나를 산다.
# 원하는 만큼 가지고 있는 주식을 판다.
# 아무것도 안한다.

# 날별로 주식의 가격을 알려주면, 위의 세 가지 동작 중 매일 한 가지를 골라 수행했을 때의 최대 이익을 구해라

# 최대 이익 계산하는 함수
def maxProfit(arr):
    # rtn: 반환할 최대 이익
    # maxElement: 현재 가장 큰 가격
    rtn = 0
    maxElement = arr[-1]
    
    # arr 배열을 거꾸로 돌면서
    for i in range(len(arr) - 2, -1, -1):
        # 현재 값이 maxElement보다 크면 값 교체
        if arr[i] > maxElement:
            maxElement = arr[i]
        # 현재 값이 maxElement보다 작으면 주식을 사서 미래에 팔았다는 셈 치고 그 차익을 rtn에 더함
        else:
            rtn += maxElement - arr[i]

    return rtn


# main
T = int(input())

for i in range(T):
    N = int(input())
    
    # N일의 가격을 넣을 배열
    arr = []
    
    prices = input().split(' ')
    for price in prices:
        arr.append(int(price))
    
    # 최대 이익 출력
    print(maxProfit(arr))
