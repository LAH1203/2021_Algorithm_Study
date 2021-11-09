def solution():
    answer = 0

    # N과 M이 공백을 기준으로 하여 각각 자연수로 주어짐
    N, M = map(int, input().split())
    # N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐
    firsts = []
    for i in range(N):
        data = list(map(int, input().split()))
        # 각 행에서 가장 작은 값을 집어넣음
        firsts.append(min(data))
    
    answer = max(firsts)

    return answer

# 결과 출력
print(solution())