#단지 구분
#적록색약은 R과 G를 같게 봄 = 통일
from collections import deque

#입력
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(str,input())))

#이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS
def bfs(x,y,v, graph):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([])
    queue.append((x,y))
    graph[x][y]=0

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
            #이전 노드와 값이 일치할 때
            if graph[nx][ny] == v :
                graph[nx][ny]=0
                queue.append((nx,ny))





graph2 = [[0]*n for i in range(n)]
count2 = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' or graph[i][j] == 'G':
            graph2[i][j] = 1
        else :
             graph2[i][j] = 2



count = 0
for i in range(n):
    for j in range(n): 
        if graph[i][j] != 0: #적록색약이 아닐 때
            bfs(i,j,graph[i][j], graph) 
            count += 1
        if graph2[i][j] != 0 : #적록색약일 때
            bfs(i,j,graph2[i][j], graph2)
            count2 += 1


print(count)
print(count2)

