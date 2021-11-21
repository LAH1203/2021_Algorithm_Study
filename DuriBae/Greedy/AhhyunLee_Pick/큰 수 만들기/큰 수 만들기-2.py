#2차 풀이
#인터넷 참고
#answer를 리스트로 활용하여 pop/push 활용하기

#answer의 원소가 비교하려는 수 보다 작으면 pop
#answer의 원소가 더 크면 append

number = str(input())
k = int(input())

def solution(number,k):
    answer =[]
    for i in number :
        while(k>0 and answer and answer[-1]<i):
            answer.pop()
            k-=1
        answer.append(i)
    return ''.join(answer[:len(answer)-k])

print(solution(number,k))