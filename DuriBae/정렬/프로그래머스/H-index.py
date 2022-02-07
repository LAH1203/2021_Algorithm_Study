#과학자의 생산성과 영향력을 나타내는 지표.
#h-index 값을 구하는 게 문제.
#논문 n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면
#h의 최댓값이 h-index
#citations가 매개변수(인용 횟수를 담은 배열)
#h를 return 하는 solution 함수를 구하라
#5편 논문, 3회 이상 인용, 나머지 2편은 3회 이하 인용. 따라서 3.
#피인용수가 논문의 수보다 같거나 작아질 때 h가 h지수
#인터넷 참고
#https://yunaaaas.tistory.com/56
#enumerate 반복문 사용 시 몇 번째 반복인지 확인할 때 사용

citations = [3,0,6,1,5]

def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)

print(solution(citations))