#1차 풀이
#가로세로 한 블록의 시간과 대각선 한 블록 시간 비교
#연산 결과가 다름
x,y,w,s = map(int, input().split())

time = 0
if(2*w>s):
    #대각선이 이득
    time += min(x,y)*s
    time += (max(x,y)-min(x,y))*w
else :
    #대각선이 이득 아님
    time += (x+y)*w

print(time)
