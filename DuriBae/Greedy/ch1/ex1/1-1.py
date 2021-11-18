import time # 시간 계산

# 큰 수의 법칙
# 1차 풀이
#M번 더하기, 연속 K번 더하기

n,m,k = map(int, input().split())
num = list(map(int, input().split()))

start_time = time.time() #측정 시작

num.sort(reverse=True)
big1 = num[0] #제일 큰 원소
big2 = num[1] #그 다음 큰 원소
bignum = 0 # 수의 합이 들어갈 변수
count = 0 # m만큼 더하는 횟수를 셀 변수

#제일 큰 원소를 k번 더하고, 그 다음 원소를 1번 더하고 바꾸면 됨.

while(count<m):
    i=0
    while(i<k):
        bignum += big1
        count += 1
        i+=1
    if(i==k):
        bignum += big2
        count +=1
        i=0

print(bignum)
    
end_time = time.time() #측정 종료
print("수행시간 :", end_time - start_time) # 수행 시간 출력

#1차 풀이시간 : 12분