def solution(numbers):
  numStr = [str(num) for num in numbers]
  numStr.sort(key=lambda num: num*3, reverse=True)
  
  return str(int(''.join(numStr)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 0, 0]))
