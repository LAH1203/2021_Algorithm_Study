# 주식 하나를 산다.
# 원하는 만큼 가지고 있는 주식을 판다.
# 아무것도 안한다.

# 날별로 주식의 가격을 알려주면, 위의 세 가지 동작 중 매일 한 가지를 골라 수행했을 때의 최대 이익을 구해라

# 최대 이익 계산하는 함수
def maxProfit(arr):
    # rtn: 반환할 최대 이익
    # cnt: 현재 가지고 있는 주식의 개수
    # price: 현재 가진 주식들의 구매 비용
    rtn = 0
    cnt = 0
    price = 0
    
    # arr 배열을 돌면서
    for i in range(len(arr)):
        maxElement = max(arr)
        # 현재 값이 최대값이 아니면 구매
        if arr[i] != maxElement:
            cnt += 1
            price += arr[i]
        # 현재 값이 최대값이면 현재 가지고 있는 주식을 전부 판매
        else:
            rtn += (arr[i] * cnt - price)
            cnt = 0
            price = 0
        # 현재 값은 이제 사용하지 않으므로 0으로 초기화
        arr[i] = 0

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
