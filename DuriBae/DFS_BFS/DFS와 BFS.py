
from collections import deque

def bfs(v):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([v])
    #현재 노드를 방문 처리
    visited[v]=True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        l = queue.popleft()
        print(l,end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[l]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(v):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

#입력
n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    m1, m2 = map(int, input().split())
    graph[m1].append(m2)
    graph[m2].append(m1)
for i in range(1, n+1):
    graph[i].sort()


dfs(v)
visited = [False] * (n+1)
print()
bfs(v)