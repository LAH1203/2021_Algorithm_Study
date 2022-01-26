#n을 입력받고 계획을 입력받음
#계획대로 실행하는데 공간을 벗어나면 무시, 그래서 최종적으로 가게 되는 위치를 반환 

n = int(input())
plan = input().split()


dx = [0,0,-1,1]
dy = [-1,1,0,0]
types = ['L','R','U','D']
x,y=1,1

for p in plan:
    for i in range(len(types)):
        if p == types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if(nx<1 or ny<1 or nx>n or ny>n):
        continue
    x,y=nx,ny

print(x,y)



