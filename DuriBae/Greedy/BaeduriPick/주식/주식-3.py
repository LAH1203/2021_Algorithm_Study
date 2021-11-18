#3차 풀이
#인터넷 참고..
#뒤에서부터 접근할 것!

t = int(input())

solution = []

for _ in range(t) :
    n = int(input())
    stock = list(map(int, input().split()))

    result = 0 
    maxst = 0

    for i in range(len(stock)-1,-1,-1):
        if(stock[i]>maxst):
            maxst = stock[i]
        else :
            result += maxst - stock[i]
    
    solution.append(result)


for idx in solution :
    print(idx)

