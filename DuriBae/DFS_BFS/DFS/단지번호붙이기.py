#입력
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
    global count
    #공간을 벗어나면 종료
    if x<0 or y<0 or x>=n or y>=n:
        return False

    if graph[x][y] == 1 :
        count += 1 
        graph[x][y]= 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True

count = 0
result = []

for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result.append(count)
            count=0

print(len(result))

result.sort()

for i in range(len(result)):
    print(result[i])
