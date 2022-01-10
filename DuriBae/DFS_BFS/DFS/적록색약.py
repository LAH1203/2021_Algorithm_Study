
#입력
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(str,input())))

graph2 = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R' or graph[i][j] == 'G':
            graph2[i][j] = 1
        else :
             graph2[i][j] = 2

#이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visitied = [[False]*n for _ in range(n)]
#DFS
def dfs(x,y,graph,type):
    visitied[x][y]==True

    for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            #이전 노드와 값이 일치할 때
            if visitied[nx][ny]==False :
                graph[nx][ny]=0

                if(type==1): #적록색약
                    dfs(nx,ny,graph2,1)
                if(type==0): #색약이 아닐때
                    dfs(nx,ny,graph,0)


count = 0
count2 = 0
for i in range(n):
    for j in range(n): 
        if visitied[i][j]==False: #적록색약이 아닐 때
            dfs(i,j, graph,0) 
            count += 1
           
for i in range(n):
    for j in range(n): 
        if visitied[i][j]==False: #적록색약일 때
            dfs(i,j, graph2,0) 
            count2 += 1

print(count)
print(count2)