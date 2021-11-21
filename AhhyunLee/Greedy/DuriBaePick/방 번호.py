'''
- 숫자를 구매하기 위해 준비한 금액: M원
- 문방구에서 파는 숫자: 0 ~ N-1
- 각 숫자 i의 가격: Pi
- 같은 숫자를 여러 개 구매할 수 있고, 항상 원하는 만큼 숫자 구매 가능
- 방 번호가 0이 아니라면 0으로 시작할 수 없음
'''

# 가장 큰 방 번호를 구하는 함수
def maxNum(N, P, M):
    num = ''
    # 현재 비용
    cost = 0

    # 자릿수를 늘리는 것이 우선적으로 수행되어야 하므로 가장 싼 숫자 기반으로 가능한 자릿수를 뽑아냄
    minValueIdx = P.index(min(P))
    # 첫 자리는 0이 아니어야 하므로 0이 아닌 다른 수 뽑아냄
    if minValueIdx == 0:
        tmp = P[0]
        P[0] = 51
        # 만약 그 다음 작은 비용으로 그 수를 사지 못하면 바로 0 리턴
        if min(P) > M:
            return 0
        # 0이 아닌 다른 숫자 집어넣고 다시 0의 비용을 돌려놓음
        num += str(P.index(min(P)))
        cost += min(P)
        P[0] = tmp

    # 0을 포함하여 모든 숫자 중에서 가장 적은 비용의 수 뽑아냄
    minValueIdx = P.index(min(P))
    minValue = P[minValueIdx]

    # 남은 돈으로 만들 수 있는 최대 자릿수
    digit = (M - cost) // minValue
    for i in range(digit):
        num += str(minValueIdx)
    cost += minValue * digit
    
    # 남은 비용
    remainCost = M - cost
    # 방 번호를 하나하나 돌면서
    for i in range(len(num)):
        tmp = int(num[i])
        # 큰 수부터 현재 최소 비용의 수까지 돌면서
        for j in reversed(range(tmp, len(P))):
            # 만약 최소값의 비용에서 남은 비용보다 작은 비용을 더하였을 때 사용할 수 있는 더 큰 숫자가 있다면 갱신
            if P[j] > P[tmp]:
                if P[j] - P[tmp] <= remainCost:
                    remainCost -= P[j] - P[tmp]
                    tmp = j
                    break
            # 또한 최소값과 같은 비용의 더 큰 숫자가 있다면 갱신
            elif P[j] == P[tmp]:
                tmp = j
                break
        numList = list(num)
        numList[i] = str(tmp)
        num = ''.join(numList)

    return num

# main
N = int(input())
P = list(map(int, input().split()))
M = int(input())

print(maxNum(N, P, M))