def solution(citations):
  answer = 0
    
  # 논문 인용횟수 정렬
  citations.sort()
    
  for i in range(len(citations)):
    h1 = citations[i]
    h2 = len(citations) - i
    if h1 >= h2:
      answer = h2
      break
    
  return answer

print(solution([3, 0, 6, 1, 5]))
