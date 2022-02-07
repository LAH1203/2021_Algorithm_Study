#인터넷 참고
#정렬하면 겹칠 가능성 있는 수가 앞뒤로 정렬된다.
#=뒤쪽 번호만 확인하면 된다.
# https://alpyrithm.tistory.com/72
# https://chldkato.tistory.com/83

t = int(input())
for _ in range(t):
    n = int(input())
    num = []
    for _ in range(n):
        num.append(input())
    
    result=True
    num.sort()
    
    for i in range(n-1):
        if(num[i]==num[i+1][:len(num[i])]):
            result=False
            break

    if(result):
        print('YES')
    else:
        print('NO')