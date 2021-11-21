#유제품 2+1 세일. 한 번에 3개 살 때만 가장 싼 것 무료.
#유제품의 수 n, 유제품의 가격 c, 최소비용 구하기
#가장 큰 꾸러미부터 만들기

#꾸러미를 3으로 나누고, 몫만큼 해당하는 인덱스의 원소를 빼고 더한다.

n = int(input())
c = list()

for _ in range(n):
    c.append(int(input()))

c.sort(reverse=True)

count=2 #pop할 때마다 빠지는 인덱스 보충
for i in range(n//3):
    c.pop(i+count)
    count+=1

result = 0

for j in c :
    result += j

print(result)