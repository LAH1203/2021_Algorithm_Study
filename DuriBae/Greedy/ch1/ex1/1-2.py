import time # 시간 계산


n,m,k = map(int, input().split())
num = list(map(int, input().split()))

start_time = time.time() #측정 시작

num.sort(reverse=True) #정렬
big1 = num[0] #제일 큰 원소
big2 = num[1] #그 다음 큰 원소

bignum = big1 * (m//k)*k + big2*(m%k)

#print(m//k*k, m%k)

print(bignum)

end_time = time.time() #측정 종료
print("수행시간 :", end_time - start_time) # 수행 시간 출력
