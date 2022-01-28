#수를 큰 수부터 작은 수까지 내림차순으로 정렬하는 프로그램

n = int(input())
num=[]
for _ in range(n):
   num.append(int(input()))

num.sort(reverse=True)

for i in num:
    print(i, end=' ')