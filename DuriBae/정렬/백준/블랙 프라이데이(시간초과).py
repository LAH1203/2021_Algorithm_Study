#무게 C에 맞게 물건을 가져오면 전부 만원
#물건은 최대 3개, 같은 물건 선택 불가, 판매하는 물건의 무게는 모두 다르다.
#물건 N개가 주어질 때, 만 원에 구매할 수 있는 조합이 있는지 출력하라.
#입력 : 물건의 개수 N, 제시하는 무게 C가 공백으로 구분되어 주어진다.
#다음 줄에 N개의 물건 각각 무게 W가 공백으로 구분되어 주어진다.
#출력 : 문제의 조건을 만족하는 조합이 있으면 1, 아니면 0을 출력한다.

#일단 오름차순으로 정렬. 그 다음에 1개, 2개, 3개 조합 있는지 찾아서 있으면 1 출력.

n,c = map(int,input().split())

weight = list(map(int, input().split()))
weight.sort()
#print(weight)

result = False
#c와 같은 게 있는지 찾기. 
if c in weight:
    result = True

#3개 조건 : 뒤에서부터 c보다 작거나 같게 하는 원소 찾음. 같으면 1 출력, 작으면 더해서 또 남은 원소 찾음.
else :
    for i in range(len(weight)-1,0,-1):
        for j in range(i):
            if(i==j):
                continue
            if(weight[i]+weight[j]>c):
                continue
            if(weight[j]+weight[i]==c):
                result = True
                break
            if(weight[i]+weight[j]>(c-weight[0])):
                continue
            if(weight[i]+weight[j]<c):
                for k in range(j,i):
                    if(j==k):
                        continue
                    if(weight[i]+weight[j]+weight[k]>c):
                        continue
                    if(weight[i]+weight[j]+weight[k]<c):
                        continue
                    if(weight[i]+weight[j]+weight[k]==c):
                        result=True
                        break


if(result):
    print(1)
else:
    print(0)
                

