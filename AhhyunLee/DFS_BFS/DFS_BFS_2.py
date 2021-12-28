def solution(graph, x, y, beforeCost, n, m):
  # 인덱스 벗어나는 경우 예외 처리
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  
  # 방문할 수 있는 경우
  if graph[x][y] != 0:
    # 값이 1이거나 지금 도달한 값보다 큰 경우 업데이트
    if graph[x][y] == 1 or graph[x][y] > beforeCost + 1:
      graph[x][y] = beforeCost + 1
    # 최소이므로 오른쪽과 아래 노드만 검사
    solution(graph, x + 1, y, graph[x][y], n, m)
    solution(graph, x, y + 1, graph[x][y], n, m)

# MAIN
n, m = map(int, input().split())

graph = []

# n번동안 m개의 수 입력받기
for _ in range(n):
  graph.append(list(map(int, input())))

solution(graph, 0, 0, 0, n, m)

print(graph[n - 1][m - 1])
