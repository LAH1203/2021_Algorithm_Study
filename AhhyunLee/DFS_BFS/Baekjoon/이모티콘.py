from collections import deque

def bfs(visited, queue, n):
  # queue가 빌 때까지 반복
  while queue:
    screen, clipboard = queue.popleft()
    # 1. 아직 방문한 적이 없을 경우, 클립보드에 값 복사
    if visited[screen][screen] == -1:
      visited[screen][screen] = visited[screen][clipboard] + 1
      queue.append((screen, screen))
    # 2. 현재 화면에 있는 이모티콘에 클립보드에 있는 이모티콘을 붙여넣기 해도 되는 경우, 클립보드를 화면에 붙여넣기
    paste = screen + clipboard
    if paste <= n and visited[paste][clipboard] == -1:
      # 클립보드에 복사된 값 붙여넣기
      visited[paste][clipboard] = visited[screen][clipboard] + 1
      queue.append((paste, clipboard))
    # 3. 화면에서 이모티콘을 하나 삭제하는 경우
    delete = screen - 1
    if screen > 0 and visited[delete][clipboard] == -1:
      visited[delete][clipboard] = visited[screen][clipboard] + 1
      queue.append((delete, clipboard))

# MAIN
n = int(input())
visited = [[-1] * (n + 1) for _ in range(n + 1)]
queue = deque()

# 초기 상태 만들기
queue.append((1, 0))
visited[1][0] = 0

bfs(visited, queue, n)

# 해당 이모티콘을 만드는데 소요된 시간을 모두 넣음
time = list(filter(lambda tmp : tmp != -1, visited[n]))

# 최소 시간 출력
print(sorted(time)[0])
