#주식
#1차 풀이
#오답 출력. 소요시간 : 25분 31초

t = int(input())
solution=[]
count=0
while(count<t):
        n = int(input())
        stock = list(map(int, input().split()))

        #가장 큰 날을 찾아서 그 전까지 계속 산다고 가정하면?

        maxst = max(stock) #가장 높은 주가
        maxidx = stock.index(maxst) # 가장 높은 주가의 인덱스
        result = 0 # 이익

        for i in range(maxidx+1):
            result += (maxst - stock[i])
        
        solution.append(result)
        count+=1
    
for idx in solution :
    print(idx)
       