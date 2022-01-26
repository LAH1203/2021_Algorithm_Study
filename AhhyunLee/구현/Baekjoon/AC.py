'''
R: 배열에 있는 수의 순서를 뒤집는 함수
D: 첫 번째 수를 버리는 함수
-> 배열이 비어있는데 D를 사용한 경우 에러 발생

배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구해보자
'''
from collections import deque

t = int(input())

for _ in range(t):
  p = list(map(str, input()))
  n = int(input())
  numStr = input()[1:-1]
  deq = deque()
  if numStr:
    num = numStr.split(',')
    for i in range(len(num)):
      deq.append(num[i])
  
  error = False
  r = False
  for i in range(len(p)):
    if p[i] == 'R':
      if r:
        r = False
      else:
        r = True
    elif p[i] == 'D':
      if len(deq) == 0:
        error = True
        break
      elif r:
        deq.pop()
      else:
        deq.popleft()
  
  if error:
    print('error')
  else:
    if r:
      deq.reverse()
    numStr = ','.join(deq)
    print(f'[{numStr}]')
