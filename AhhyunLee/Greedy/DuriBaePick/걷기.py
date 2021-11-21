'''
걷는 방법은 6가지라고 말할 수 있다.
현재 위치가 (a, b)라고 생각한다면,
1. (a + 1, b)
2. (a, b + 1)
3. (a + 1, b + 1)
4. (a - 1, b)
5. (a, b - 1)
6. (a - 1, b - 1)
로 이동할 수 있다.

[생각한 로직]
1) 만약 2*W가 S보다 크다면, X와 Y 중 작은 값의 대각선까지 간 다음 다른 큰 값에서 현재 위치를 뺀 만큼을 더 가면 되지 않을까?
2) 반대로 2*W가 S보다 작다면, 무조건 1 또는 2의 방법을 사용하여 (X, Y)까지 가면 되지 않을까?
'''

# 최소시간을 구하는 함수
def minTime(X, Y, W, S):
    time = 0

    if 2 * W > S:
        # 대각선으로 X, Y 중 작은 값의 대각선 값까지 감
        time += S * min(X, Y)
        # 만약 W가 S보다 크다면 남은 것에서 짝수만큼은 대각선으로 하는 편이 더 이득
        gap = max(X, Y) - min(X, Y)
        if W > S:
            time += S * (gap // 2) * 2
            gap %= 2
            time += W * gap
        # 그게 아니라면 정석대로 가로, 세로를 사용하여 감
        else:
            time += W * gap
    else:
        # 가로 또는 세로로 목적지까지 감
        time += W * (X + Y)

    return time

# main
# X Y W S
X, Y, W, S = map(int, input().split())

print(minTime(X, Y, W, S))