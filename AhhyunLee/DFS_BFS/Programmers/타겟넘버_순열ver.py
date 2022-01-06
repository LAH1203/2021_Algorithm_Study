import itertools

# 숫자가 많을 경우, 시간이 오래 걸리므로 시간 초과 발생

def isAllFalse(arr):
    for i in arr:
        if i:
            return False
    return True

def calculateResult(numbers, types):
    result = 0
    
    for i in range(len(numbers)):
        if types[i]:
            result += numbers[i]
        else:
            result -= numbers[i]
    
    return result

def solution(numbers, target):
    answer = 0
    
    plus = [True] * len(numbers)
    idx = 0
    
    while isAllFalse(plus) == False:
        typeSet = set(itertools.permutations(plus))
        
        for types in typeSet:
            if calculateResult(numbers, types) == target:
                answer += 1
        
        plus[idx] = False
        idx += 1
    
    return answer
