#1차 풀이. 테스트 케이스는 성공했지만 결과가 오답.
#k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기
#문자열 형식 숫자 number, 제거할 수의 개수 k
#만들 수 있는 가장 큰 수를 문자열 형태로 return

number = str(input())
k = int(input())

#k 이하 인덱스에서 가장 큰 수 이하는 잘라냄
#이후 2개씩 비교 후 큰 수를 answer에 더하기
#k를 감소시켜가며 문자열을 자른 후 나머지 문자열 합치기

def solution(number,k):
    answer =""
    count = [] 
    for i in range(k):
        count.append(number[i])

    answer += str(max(count))

    delnum = number.index(max(count))

    number = number[delnum+1:]
    k-= delnum

    while(k>0):
        if(number[0]>number[1]):
            answer += number[0]
            k-=1
        elif(number[0]==number[1]):
            answer += number[0]
        else :
            answer += number[1]
            k-=1

        number = number[2:]
    
    answer += number

    return answer

print(solution(number,k))



