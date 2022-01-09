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
    # 변환할 수 없는 경우
    elif len(words) == 0:
        return
    
    for word in words:
        if isDifferentOneLetter(now, word):
            tmpWords = words.copy()
            tmpWords.remove(word)
            dfs(word, target, tmpWords, count + 1, resultList)

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

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
