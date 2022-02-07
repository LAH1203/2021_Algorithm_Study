
n = int(input())
num=[]
for _ in range(n):
   num.append(int(input()))

num.sort(reverse=True)

for i in num:
    print(i, end=' ')