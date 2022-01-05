from collections import deque

# [목표] 그래프를 입력받고 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력
# [주의할 점]
# 1. 방문할 수 있는 정점이 여러 개인 경우, 정점 번호가 작은 것을 먼저 방문하고 더 이상 방문할 수 있는 점이 없는 경우 종료
# 2. 어떤 두 정점 사이에는 여러 개의 간선이 있을 수 있으며, 모든 간선은 양방향

# DFS
def dfs(v, graph, visited):
  # 현재 노드를 방문처리
  visited[v] = True
  print(v, end=' ')

  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(i, graph, visited)

# BFS
def bfs(v, graph, visited):
  queue = deque([v])

  # 현재 노드를 방문처리
  visited[v] = True

  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v, end=' ')
    # 해당 원소와 연결된 것 중 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# main
# n: 정점의 개수
# m: 간선의 개수
# v: 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

# 작은 번호부터 방문할 수 있도록 정렬
for i in range(1, n + 1):
  graph[i].sort()

visited = [False] * (n + 1)

dfs(v, graph, visited)
print()

# 방문 기록 초기화
visited = [False] * (n + 1)

bfs(v, graph, visited)
