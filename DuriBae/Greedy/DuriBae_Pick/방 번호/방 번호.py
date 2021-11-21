#1차 풀이
#번호 n, 가진 돈 m, 번호 당 금액 p
#돈을 모두 사용해야 함

#큰 수를 만들기 위해 해야 하는 것
#자리수가 많아야 함 = 가장 싼 걸 많이 사야 함.
#큰 자리수의 수가 커야 함
#모두 0이 아니어야 함
#인터넷도 참고하고 여러 번 시도했지만 결국 이해하지 못하고 실패..

n = int(input())
p = list(map(int, input().split()))
m = int(input())

result = ''

cheap = min(p) #가장 싼 가격

cheapnum = p.index(min(p)) #싼 숫자의 인덱스

money = m%cheap #자릿수 확보 후 남은 금액

if(n<=1):
    print(0)

else:
    count = 0
    for i in range(n,0,-1):
        if((p[i-1]-cheap)==0):
            result += str(cheapnum)*((m//cheap)-count) #남은 문자 더하기
        elif(money>=(p[i-1]-cheap)):
            ext = money//(p[i-1]-cheap) #차액으로 바꾼 번호의 수
            count +=ext # 번호 수 합
            result += str(p.index(p[i-1]))*ext #바꾼 번호부터 문자열 만들기
            money -= (p[i-1]-cheap) #남은 돈
        else :
            result += str(cheapnum)*((m//cheap)-count) #남은 문자 더하기

    print(result)

            
            