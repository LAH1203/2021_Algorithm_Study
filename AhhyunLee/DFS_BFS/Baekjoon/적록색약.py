# 백준 기본 재귀 깊이보다 많이 반복하는 경우가 발생하므로, 최대 재귀 깊이를 강제로 증가시킴
import sys
sys.setrecursionlimit(10 ** 9)

def dfs(graph, visited, x, y, n, find):
  # 방문할 수 있는 경우
  if visited[x][y] == False and graph[x][y] == find:
    visited[x][y] = True  # 방문처리
    # 인접 노드가 find와 같은 경우에만 탐색
    if x > 0 and graph[x - 1][y] == find:
      dfs(graph, visited, x - 1, y, n, find)
    if x < n - 1 and graph[x + 1][y] == find:
      dfs(graph, visited, x + 1, y, n, find)
    if y > 0 and graph[x][y - 1] == find:
      dfs(graph, visited, x, y - 1, n, find)
    if y < n - 1 and graph[x][y + 1] == find:
      dfs(graph, visited, x, y + 1, n, find)
    return True
  
  return False

def makeClearVisited(n):
  visited = []

  for _ in range(n):
    tmp = []
    for _ in range(n):
      tmp.append(False)
    visited.append(tmp)
  
  return visited

def makeGToR(graph):
  for i in range(len(graph)):
    for j in range(len(graph[i])):
      if graph[i][j] == 'G':
        graph[i][j] = 'R'

# MAIN
n = int(input())

graph = []

for _ in range(n):
  graph.append(list(map(str, input())))

visited = makeClearVisited(n)
count = 0

# 적록색약이 아닌 경우
for i in range(n):
  for j in range(n):
    if dfs(graph, visited, i, j, n, graph[i][j]):
      count += 1

print(count, end=' ')

# 적록색약인 경우
# R과 G를 통일해야 하므로 모든 G를 R로 변경
makeGToR(graph)
# visited, count 초기화
visited = makeClearVisited(n)
count = 0

for i in range(n):
  for j in range(n):
    if dfs(graph, visited, i, j, n, graph[i][j]):
      count += 1

print(count)
