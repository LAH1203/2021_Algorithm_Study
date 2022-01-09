# 각 공항들의 연결 정보를 배열로 담아 DFS를 사용하면 되지 않을까?
# 항공권을 모두 사용해야 한다는 조건이 있음 -> 모든 공항이 일직선으로 연결되는 극단적인 그래프를 찾아야 함
# 가능한 경로가 2개 이상일 경우, 알파벳 순서가 앞서는 경로를 리턴 -> sort 사용

def dfs(graph, path, stack):
    # stack에는 다음에 도착할 공항이 들어있음
    # 모든 티켓을 사용하였을 경우 -> stack이 비게 됨
    while len(stack) > 0:
        top = stack[-1]

        # 해당 공항에서 출발하는 티켓이 없는 경우
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
        # 티켓이 있는 경우에는 stack에 도착 공항을 추가하고 해당 티켓을 사용처리
        else:
            stack.append(graph[top][-1])
            graph[top] = graph[top][:-1]

def solution(tickets):
    answer = []
    graph = dict()
    
    for (start, end) in tickets:
        graph[start] = graph.get(start, []) + [end]
    
    for key in graph.keys():
        # 내림차순 정렬
        graph[key].sort(reverse=True)
    
    dfs(graph, answer, ['ICN'])

    answer = answer[::-1]

    return answer
