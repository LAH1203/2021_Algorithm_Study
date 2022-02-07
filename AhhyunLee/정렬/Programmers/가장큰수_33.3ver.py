def getMax(numbers):
  maxNum = 0
  rtnNum = 0

  for num in numbers:
    minLen = min(len(str(rtnNum)), len(str(num)))
    maxNum = max(int(str(rtnNum)[0]), int(str(num)[0]))
    for i in range(minLen):
      if str(rtnNum)[i] < str(num)[i]:
        rtnNum = num
        break
      elif str(rtnNum)[i] == str(num)[i] and len(str(num)) > len(str(rtnNum)):
        if int(str(num)[i + 1]) > maxNum:
          rtnNum = num
          break
      elif str(rtnNum)[i] > str(num)[i]:
        break
  
  numbers.remove(rtnNum)

  return rtnNum

def solution(numbers):
  answer = ''

  while len(numbers) > 0:
    answer += str(getMax(numbers))

  return str(int(answer))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))
