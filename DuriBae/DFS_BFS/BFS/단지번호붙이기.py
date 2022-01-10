from collections import deque

#입력
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS
def bfs(x,y):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([])
    queue.append((x,y))
    graph[x][y]=0
    count = 1

    #큐가 빌 때까지 반복
    while queue:
        x,y= queue.popleft()
        #현 위치에서 네 방향의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            #해당 노드를 처음 방문하는 경우 count 증가
            if graph[nx][ny] == 1 :
                graph[nx][ny]=0
                queue.append((nx,ny))
                count += 1
    return count

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            result.append(bfs(i,j))

print(len(result))

result.sort()

for i in range(len(result)):
    print(result[i])
