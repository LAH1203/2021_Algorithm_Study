# 연결된 노드의 집합을 네트워크라고 명명
# 네트워크의 개수 즉, 연결된 노드 집합의 개수를 반환
# [주의점] 간접 연결도 연결로 판단하여 매개변수가 주어짐

# 풀이 생각: DFS를 사용해 나와 연결된 모든 노드들을 하나의 집합으로 치부하면 되지 않을까?

def isVisitAll(visited):
    for i in visited:
        if i == False:
            return False
    return True

def dfs(v, graph, visited):
    if visited[v]:
        return False
    
    visited[v] = True
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i, graph, visited)
    
    return True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    idx = 0
    
    while isVisitAll(visited) == False:
        if dfs(idx, computers, visited):
            answer += 1
        idx += 1
    
    return answer
