#인터넷 참고
#정렬해서 가장 작은 것과 가장 큰 것을 매칭.
#제한 무게보다 무겁지 않으면 같은 보트로 보고 미리 정해둔 보트 수에서 뺌.

people = list(map(int, input().split()))

limit = int(input())

def solution(people, limit):
    answer = len(people)

    i = 0
    j = len(people)-1

    people.sort()

    while(i<j):
        if(people[i]+people(j)<=limit):
            answer-=1
            i+=1
        j-=1
    
    return answer

print(solution(people,limit))