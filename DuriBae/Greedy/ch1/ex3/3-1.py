import time # 시간 계산

#n이 1이 될 때까지 반복
#1. n에서 1을 뺌
#2. n을 k로 나눈다 단, 나누어 떨어질 때만
#3. 최소 횟수 구하기

n, k = map(int, input().split())

start_time = time.time() #측정 시작

count = 0
while(n!=1):
    if(n%k==0):
        n//=k
        count +=1
    else :
        n-=1
        count +=1

print(count)

end_time = time.time() #측정 종료
print("수행시간 :", end_time - start_time) # 수행 시간 출력

#풀이 시간 : 3분 52초