#n*n 크기 공간에 물고기m마리와 아기 상어 1마리. 한 칸에 물고기 1마리
#상어와 물고기는 모두 크기를 가진다. 가장 처음 아기상어 크기 = 2
#아기 상어는 1초에 상하좌우 한 칸씩 이동
#자기보다 큰 물고기가 있는 칸은 지나갈 수 없음.
#작은 물고기만 먹을 수 있음.
#크기가 같은 물고기는 먹을 수 없지만 지나갈 수는 있음.
#이동과 동시에 물고기를 먹는다. 자신의 크기와 같은 수의 물고기를 먹으면 크기가 1 증가한다.
#1. 먹을 수 있는 물고기가 없으면 엄마한테 도움을 청한다
#2. 먹을 수 있는 물고기가 1마리면 그 물고기를 먹으러 간다.
#3. 1마리보다 많으면 가까운 물고기를 먹는다.
#3-1. 아기 상어 칸에서 물고기 칸으로 이동할 때 지나야하는 최솟값=거리
#3-2. 거리가 가까운 물고기가 많으면 가장 위에 있는 물고기, 그런 물고기가 여러마리면 가장 왼쪽에 있는 물고기를 먹는다.
#0: 빈칸
#1, 2, 3, 4, 5, 6 : 물고기의 크기
#9: 아기 상어의 위치
#인터넷 참고

from collections import deque

n = int(input())

direction = [[0]*n for _ in range(n)]

#전체 맵 정보를 입력받기
array = []

for i in range(n):
    array.append(list(map(int,input().split())))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1] 

sx,sy = 0,0 #상어좌표
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            array[i][j] = 0 #좌표 초기화
            sx, sy = i, j 
            break

size=2 #초기 크기
movecount=0 #움직인 수
eat=0 #먹은 물고기 수

while True:
    q = deque()
    q.append((sx,sy,0))
    visited = [[False]*n for _ in range(n)]
    flag = 1e9 
    fish = []
    while q:
        x,y,count = q.popleft()

        if count > flag: #물고기를 먹은 이동까지만 센다
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx<0 or ny<0 or nx>=n or ny>=n):
                continue
            if(array[nx][ny] > size or visited[nx][ny]): #물고기가 더 크거나 이미 방문한 경우
                continue
            if(array[nx][ny] != 0 and array[nx][ny] < size): #물고기가 있고 상어보다 작을 때
                fish.append((nx,ny,count+1)) #물고기 추가
                flag = count
            visited[nx][ny]=True
            q.append((nx,ny,count+1))

        
    if(len(fish)>0):
        fish.sort() 
        x,y,move = fish[0][0],fish[0][1],fish[0][2]
        movecount += move #이동한 수 
        eat += 1 #물고기 먹은 수
        array[x][y] = 0 #물고기 먹고 빈 칸 만들기
        if(eat == size): #먹은 수가 크기와 같을 때
            size +=1
            eat = 0
        sx,sy = x,y #먹고 난 자리를 상어 위치로 설정
    else:
        break


print(movecount) #이동한 수 출력
