def solution():
    answer = 0

    N, K = map(int, input().split())

    # K가 1이 아닌 이상 N이 K로 나누어떨어진다면 1번보다는 2번을 하는게 낫다
    # N이 K로 나누어떨어지는 만큼의 나머지를 1번을 사용하여 빼고 계산하면 되지 않을까?

    while N != 1:
        # N이 K로 나누어떨어지면 나누고 answer 1 증가
        if N % K == 0:
            N //= K
            answer += 1
        # N이 K로 나누어떨어지지 않으면 나머지만큼 빼고 answer 증가
        else:
            rem = N % K
            
            # 만약 나머지가 N과 같다면 (1로 만들어야 하므로) rem - 1을 함
            if rem == N:
                rem -= 1
            
            N -= rem
            answer += rem

    return answer

# 결과 출력
print(solution())