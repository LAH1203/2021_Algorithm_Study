#입력
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#DFS로 특정한 노드를 방문 후 연결된 노드 방문
def dfs(x,y):
    #범위를 벗어나면 종료
    if x <= -1 or x>=n or y<= -1 or y>= m:
        return False
    #노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문처리
        #상, 하, 좌, 우 모두 재귀적 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#모든 노드에 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result)
