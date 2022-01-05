# [목표] 총 단지 수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력
# [주의할 점]
# 1. 1은 집이 있는 곳, 0은 집이 없는 곳
# 2. 단지는 연결된 집의 모임
# 3. 연결되었다는 것은 어떤 집이 상하좌우 중 하나에 있는 것을 의미. 고로 대각선은 해당되지 않음

# DFS
def dfs(graph, x, y, n):
  # 위치를 벗어나는 경우 예외 처리
  if x < 0 or y < 0 or x >= n or y >= n:
    return 0
  
  # 방문할 수 있는 경우
  if graph[x][y] == 1:
    cnt = 1
    # 방문할 수 없도록 변경
    graph[x][y] = 0
    # 인접 노드 검사
    cnt += dfs(graph, x - 1, y, n)
    cnt += dfs(graph, x + 1, y, n)
    cnt += dfs(graph, x, y - 1, n)
    cnt += dfs(graph, x, y + 1, n)
    return cnt
  
  # 방문할 수 없는 경우
  return 0

# main
# n: 지도의 크기
n = int(input())

graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

group = []

for i in range(n):
  for j in range(n):
    cnt = dfs(graph, i, j, n)
    if cnt != 0:
      group.append(cnt)

print(len(group))

# 오름차순 정렬
group.sort()

for i in group:
  print(i)
