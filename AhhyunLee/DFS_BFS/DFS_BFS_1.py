def dfs(graph, x, y, n, m):
  # 인덱스 벗어나는 경우 예외 처리
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  
  # 방문할 수 있는 경우
  if graph[x][y] == 0:
    graph[x][y] = 1   # 방문할 수 없도록 변경
    # 인접 노드 전부 검사
    dfs(graph, x - 1, y, n, m)
    dfs(graph, x + 1, y, n, m)
    dfs(graph, x, y - 1, n, m)
    dfs(graph, x, y + 1, n, m)
    return True
  
  return False

# MAIN

# n: 얼음 틀의 세로 길이
# m: 얼음 틀의 가로 길이
n, m = map(int, input().split())

graph = []

# n번동안 m개의 수 입력받기
for _ in range(n):
  graph.append(list(map(int, input())))

count = 0

for i in range(n):
  for j in range(m):
    if dfs(graph, i, j, n, m):
      count += 1

print(count)
