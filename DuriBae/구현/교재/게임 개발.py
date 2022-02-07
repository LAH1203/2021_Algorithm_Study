
n, m = map(int,input().split())

direction = [[0]*m for _ in range(n)]

x,y,d = map(int,input().split())
direction[x][y]=1 #현재 좌표 방문 처리

#w전체 맵 정보를 입력받기
array = []

for i in range(n):
    array.append(list(map(int,input().split())))

#북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1] 

#왼쪽으로 회전
def turn_left():
    global d
    d -=1
    if d == -1:
        d = 3


count = 1
turn_time = 0

while True :
    turn_left()#왼쪽으로 회전
    nx = x + dx[d]
    ny = y + dy[d]
    #회전한 후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if direction[nx][ny] == 0 and array[nx][ny] == 0:
        direction[nx][ny]=1
        x=nx
        y=ny
        count +=1
        turn_time=0
        continue
    #회전한 후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time +=1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            n = nx
            y = ny

        #뒤가 바다로 막혀있는 경우
        else :
            break
        turn_time = 0

#정답 출력
print(count)
