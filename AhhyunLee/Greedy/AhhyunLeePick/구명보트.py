def solution(people, limit):
    answer = 0
    
    # 구명보트의 수를 적게 하는 것이 목표이므로 가장 무거운 사람부터 태우도록 정렬
    people = sorted(people)
    
    # 사람들을 모두 태우자!
    # cnt: 현재까지 태운 사람의 수
    # maxIdx: 아직 태우지 않은 사람 중 가장 무거운 사람의 위치
    # minIdx: 아직 태우지 않은 사람 중 가장 가벼운 사람의 위치
    cnt = 0
    maxIdx = len(people) - 1
    minIdx = 0
    while cnt < len(people):
        # 가장 무거운 사람을 태움
        maxIdx -= 1
        cnt += 1
        # 만약 가장 가벼운 사람도 탈 수 있다면, 같이 태우기
        if limit >= (people[maxIdx + 1] + people[minIdx]):
            minIdx += 1
            cnt += 1
        answer += 1
    
    return answer