#상근이가 친구와, 친구의 친구를 초대.
#동기는 모두 n명, 학번은 1부터 n까지.
#동기들의 친구 관계를 조사한 리스트를 바탕으로 사람의 수 구하기
#입력 : 동기의 수, 리스트의 길이, 친구관계
#출력 : 초대하는 동기의 수

#인터넷 참고
#BFS 활용하여 depth가 2 이하인 것만 카운트
from collections import deque

n = int(input())#동기의 수
m = int(input())#리스트의 길이
rel = [[] for _ in range(n+1)] #친구 수 만큼 관계를 정리할 리스트
for _ in range(m):
    a,b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)


def bfs(start):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    count = 0
    queue = deque([[start,0]])#관계와 깊이
    while queue:
        friend, depth = queue.popleft()
        if depth <=2: #깊이가 2보다 작으면 초대할 수 있다
            count+=1
        for i in rel[friend]:
            if(visited[i]==0):
                visited[i]=1
                queue.append([i,depth+1])
    return (count-1) #카운트에 자기 자신이 포함되어 있기 때문에 1을 뺀다

print(bfs(1))