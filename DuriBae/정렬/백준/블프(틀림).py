n,c = map(int,input().split())

weight = list(map(int, input().split()))
weight.sort(reverse=True)
result = False
#c와 같은 게 있는지 찾기. 
if c in weight:
    result = True
else :
    for i in weight:
        if(i>c-weight[0]):
            weight.remove(i)
            continue
        if((c-i) in weight and (c-i)!=i ):#2개짜리 찾기
            result = True
            break
        else :
            if(i>c-weight[len(weight)-1]-weight[len(weight)-2]):
                weight.remove(i)
                continue

            for j in weight:
                if(j==i):
                    continue
                else:
                    if(c-i-j in weight and (c-i-j)!=i and (c-i-j)!=j):#3개짜리 찾기
                        result = True
                        break

if(result):
    print(1)
else:
    print(0)
