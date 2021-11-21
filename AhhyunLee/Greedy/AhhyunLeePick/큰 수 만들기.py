def solution(number, k):
    answer = ''
    
    # 마지막으로 answer에 넣은 값의 위치를 저장할 변수
    idx = -1
    
    # number에서 k개를 제거한 숫자를 뽑아냄
    for i in range(len(number) - k):
        # 가장 컸던 수의 값을 저장할 변수
        maxNow = '0'
        
        # 마지막으로 넣었던 값의 다음 인덱스부터 k개의 수를 읽어냄
        for j in range(idx + 1, i + k + 1):
            # 더 큰 값이 나올 경우, 갱신
            if maxNow < number[j]:
                maxNow = number[j]
                idx = j
                # TC 10의 시간초과를 해결하기 위해, 9를 만나면 무조건 반복문을 종료하도록 추가
                if maxNow == '9':
                    break
        
        # k개만큼 읽으며 가장 컸던 수를 집어넣음
        answer += maxNow
    
    return answer