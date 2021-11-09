def solution(N, M, K, arr):
    answer = 0

    cnt = 0

    while cnt < M:
        # 가장 큰 수를 K번 더함
        for i in range(K):
            # 만약 더하기 전에 이미 cnt가 M이 되었을 경우엔 반복문 빠져나옴
            if cnt >= M:
                break
            answer += arr[N - 1]
            cnt += 1
        # cnt가 M이 되었을 경우 한 번 더 거름
        if cnt >= M:
            break
        # 두 번째로 큰 수 한 번 더함
        answer += arr[N - 2]
        cnt += 1
    
    return answer

# main
NMK = input().split(' ')
N = int(NMK[0])
M = int(NMK[1])
K = int(NMK[2])

arr = input().split(' ')

for i in range(N):
    arr[i] = int(arr[i])

arr.sort()

print(solution(N, M, K, arr))