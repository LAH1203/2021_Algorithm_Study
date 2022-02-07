n = int(input())
dt = [list(map(int, input().split())) for _ in range(n)]
dt.sort(key=lambda x:x[1], reverse=True) #해야하는 기한 기준으로 역순 정렬
day = dt[0][1] #처음 남은 기간 설정
for i in range(n): #과제 개수만큼 반복
    if(dt[i][1]>= day):
        day = day - dt[i][0]
    else:
        day = dt[i][1] - dt[i][0]
    #해당 과제에 남은 기간과 남은 날짜 중 더 작은 것에서 해야 하는 시간을 뺀다.

print(day)