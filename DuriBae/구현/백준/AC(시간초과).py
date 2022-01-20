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

def AC(p,n,array):
    if(n<1):
        return 'error'
    for i in p :
        if(i == 'R'):
            array.reverse()
        if(i == 'D'):
            if(len(array)==0):
                return 'error'
            del array[0]
    return array

t = int(input())
result=[]
for i in range(t):
    p = str(input())
    n = int(input())
    array = input()[1:-1].split(',')
    result.append(AC(p,n,array))

for i in result:
    print(i)
    

