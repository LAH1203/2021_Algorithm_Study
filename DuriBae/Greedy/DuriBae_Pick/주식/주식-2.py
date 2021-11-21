#2차 풀이
#가장 큰 값 이후 가격이 또 오를 때.
#큰 값에 팔고 또 오르면?
#큰 값에 팔고 지운 후 다시 계산. 리스트가 없어질 때까지 반복
#풀이시간 13분 22초
#시간초과

t = int(input())
solution=[]
count=0
while(count<t):
        n = int(input())
        stock = list(map(int, input().split()))

        #가장 큰 날을 찾아서 그 전까지 계속 산다고 가정하면?

        result = 0 

        while(len(stock)>1):
            maxst = max(stock) #가장 높은 주가
            maxidx = stock.index(maxst) # 가장 높은 주가의 인덱스
        
            for i in range(maxidx+1): #가장 높은 날에 판매
                result += (maxst - stock[i]) #이익
            
            del stock[0:maxidx+1] #이전까지 삭제
        
        solution.append(result)
        count+=1

for idx in solution :
    print(idx)