import time # 시간 계산

# 큰 수의 법칙
# 2차 풀이
# 1차처럼 풀게 되면 M의 크기가 커질 때 시간 초과
# 연산 횟수가 늘어나기 때문.
# 가장 큰 수는 m//k * k 만큼 더해지고, 나머지는 두번째로 큰 수가 더해진다.

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
