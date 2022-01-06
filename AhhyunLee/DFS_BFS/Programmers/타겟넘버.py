def dfs(numbers, v, result, target, resultList):
    if v >= len(numbers):
        resultList.append(result)
        return
    
    dfs(numbers, v + 1, result + numbers[v], target, resultList)
    dfs(numbers, v + 1, result - numbers[v], target, resultList)

def solution(numbers, target):
    answer = 0
    resultList = []
    
    dfs(numbers, 0, 0, target, resultList)
    
    for result in resultList:
        if result == target:
            answer += 1
    
    return answer
