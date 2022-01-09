# words의 최대 개수가 50개여서 그런가 테스트 케이스 3번에서만 시간초과가 발생 -> 변환할 수 없는 경우의 로직을 다시 짜는 것이 필요

def isDifferentOneLetter(word1, word2):
    differentCount = 0
    
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            differentCount += 1
    
    if differentCount == 1:
        return True
    else:
        return False

def dfs(now, target, words, count, resultList):
    if now == target:
        resultList.append(count)
        return
    # 변환할 수 없는 경우 - words의 모든 단어로 바꿔본 적이 있을 경우라고 생각
    elif count > len(words):
        return
    
    for word in words:
        if isDifferentOneLetter(now, word):
            dfs(word, target, words, count + 1, resultList)

def solution(begin, target, words):
    answer = 0
    resultList = []
    
    # target이 words에 있는 경우만 고려
    if target in words:
        dfs(begin, target, words, 0, resultList)
    
    # 결과가 나온 경우에만 최소 횟수 대입
    if len(resultList) > 0:
        answer = sorted(resultList)[0]
    
    return answer
