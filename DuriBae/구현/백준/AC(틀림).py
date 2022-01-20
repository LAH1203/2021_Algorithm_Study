#새로운 언어AC, 함수 R(뒤집기), D(버리기)
#R : 배열에 있는 수의 순서를 뒤집는 함수
#D : 첫 번재 수를 버리는 함수
#배열이 비어있는 데 D를 사용한 경우 에러 발생
#RDD 하면 배열을 뒤집고 처음 두 수를 버리는 함수
#배열의 초기값과 수행할 함수가 주어졌을 때 최종 결과 구하기

#입력
#테스트 케이스 개수 t가 주어진다. 최대 100
#각 테스트 케이스 첫째줄에 수행할 함수p가 주어진다.
#배열에 들어있는 수의 개수 n이 주어진다
#배열에 들어있는 정수가 주어진다.
#출력
#함수를 수행한 결과를 출력한다.

#인터넷 참고.

def AC(p,n,array): #지울 수를 세서 한번에 지운다
    rnum,lnum,b,r = 0,0,True,0
    if(n<1):
        return 'error'
    for i in p :
        if(i == 'R'):
            r+=1
            b = not b #False값으로 바꿔줌
        if(i == 'D'):
            if(b):
                lnum += 1 #왼쪽에서 지울 값 추가
            else:
                rnum += 1 #오른쪽에서 지울 값 추가


    result0 = array[lnum:n-rnum]
    if(len(result0)==0):
        return 'error'
    
    result = []
    for i in result0:
        result.append(int(i))
        
    if(r%2!=0):
        result.reverse()
    return result

t = int(input())
result=[]
for i in range(t):
    p = str(input())
    n = int(input())
    array = input()[1:-1].split(',')
    result.append(AC(p,n,array))

for i in result:
    print(i)
    

