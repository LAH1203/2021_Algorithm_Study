#배열 A와 배열 B 
#N개의 원소, 모두 자연수
#동빈이 최대 k번 바꿔치기 연산
#A배열 원소의 합이 최대가 되는 게 목표
#배열 A의 모든 원소의 합의 최대값 출력
#A의 가장 작은 원소를 B의 가장 큰 원소와 교체

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i] = b[i],a[i]
    else :
         break
print(sum(a))
