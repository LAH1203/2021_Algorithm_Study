n, m = map(int, input().split())
a, b, d = map(int, input().split())
gameMap = []

for _ in range(n):
  gameMap.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
turnCount = 0

# 0: 아직 가지 않은 육지
# 1: 바다
# 2: 가본 육지

while True:
  if gameMap[a][b] == 0:
    gameMap[a][b] = 2
    count += 1

  # 왼쪽 방향으로 회전
  if d == 0:
    d = 3
  else:
    d -= 1

  # 아직 가보지 않은 육지라면 이동 후 값 변경
  nextA = a + dx[d]
  nextB = b + dy[d]
  if nextA >= 0 and nextA < n and nextB >= 0 and nextB < m:
    if gameMap[nextA][nextB] == 0:
      a = nextA
      b = nextB
      turnCount = 0
    # 이미 가본 육지이거나 바다라면 turnCount 1 증가
    else:
      turnCount += 1

  # turnCount가 4라면 모든 방향으로 이동할 수 없다는 표시이므로 현재 방향 기준 뒤로 이동
  if turnCount == 4:
    nextA = a - dx[d]
    nextB = b - dy[d]
    # 만약 뒤가 바다라서 이동할 수 없는 경우, 움직임을 멈춤 -> 종료 조건
    if nextA >= 0 and nextA < n and nextB >= 0 and nextB < m:
      if gameMap[nextA][nextB] == 1:
        break
      else:
        a = nextA
        b = nextB
    turnCount = 0

print(count)
