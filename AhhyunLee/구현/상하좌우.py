n = int(input())
plan = list(map(str, input().split()))
now = {
  'x': 1,
  'y': 1
}

for behavior in plan:
  if behavior == 'L':
    # 왼쪽으로 이동 가능하다면 이동
    if now['y'] - 1 > 0:
      now['y'] -= 1
  elif behavior == 'R':
    # 오른쪽으로 이동 가능하다면 이동
    if now['y'] + 1 <= n:
      now['y'] += 1
  elif behavior == 'U':
    # 위로 이동 가능하다면 이동
    if now['x'] - 1 > 0:
      now['x'] -= 1
  elif behavior == 'D':
    # 아래로 이동 가능하다면 이동
    if now['x'] + 1 <= n:
      now['x'] += 1

print(now['x'], now['y'])
