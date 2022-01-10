from collections import deque
#1. 이모티콘을 모두 복사에서 클립보드에 저장
#2. 이모티콘을 붙여넣기
#3. 이모티콘 중 하나를 삭제
#각 1초씩 걸린다.
#S개의 이모티콘을 만드는데 걸리는 시간의 최솟값

s = int(input()) #화면에 나와야 하는 이모티콘 개수
e = [[0 for _ in range(s+1)]for _ in range(s+1)] 

def bfs(s):
    queue = deque()
    queue.append((1,0))#처음에 입력한 이모티콘과 빈 클립보드
    e[1][0] = 0
    while queue:
        se,ce = queue.popleft() 
        #se는 입력한 이모티콘 개수, ce는 클립보드에 저장된 이모티콘 개수
        if e[se][se] == 0 : #모두 복사
            e[se][se] = e[se][ce] +1
            queue.append((se,se))
        if se+ce <= s and e[se+ce][ce] == 0:
            queue.append((se+ce,ce))
            e[se+ce][ce] = e[se][ce] +1
        if se-1 >= 0 and e[se-1][ce] == 0:
            queue.append((se-1,ce))
            e[se-1][ce] = e[se][ce] +1

        
bfs(s)
answer = 0

for i in range(s+1):
    if e[s][i] != 0:
        if answer == 0 or answer > e[s][i]:
            answer = e[s][i]

print(answer)