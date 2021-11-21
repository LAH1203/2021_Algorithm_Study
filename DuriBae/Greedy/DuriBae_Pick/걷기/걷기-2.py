#2차 풀이
#인터넷 참고
#케이스별로 나누어서 가장 작은 경우 출력

x,y,w,s = map(int, input().split())


if((x+y)%2==0): #짝, 홀 이동
    time1 = max(x,y)*s #짝수
else:
    time1 = (max(x,y)-1)*s+w #홀수

time2 = (x+y)*w #직선 이동
time3 = min(x,y)*s + (max(x,y)-min(x,y))*w #혼합

print(min(time1,time2,time3))


