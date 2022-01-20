#맵 안에서 움직이는 시스템
#n*m 영역, 육지/바다 칸. 
#(A,B) A는 위에서 떨어진 칸 수, B는 우측에서 떨어진 칸 수
#1. 현위치에서 왼쪽 방향(반시계 방향으로 90도 회전)부터 갈 곳을 정한다.
#2. 왼쪽에 가지 않은 칸이 존재하면, 왼쪽으로 회전 후 1칸 전진
#가지 않은 칸이 없다면 회전만 수행 후 1단계로 돌아간다.
#3. 네 방향 모두 가봤거나 바다라면 방향 유지 후 뒤로 가서 1단계.
# 뒤쪽칸이 바다면 움직임을 멈춘다.
#입력
#n*m 을 공백으로 구분하여 입력
#좌표(A,B) 바라보는 방향d 를 입력받음
#방향 값 0:북, 1:동, 2:남, 3:서
#육지 바다 정보 주어짐. 0:육지, 1:바다
#출력 : 이동을 마친 후 캐릭터가 방문의 칸의 수

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
