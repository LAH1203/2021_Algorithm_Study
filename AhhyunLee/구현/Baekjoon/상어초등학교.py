'''
| r1 - r2 | + | c1 - c2 | = 1
-> (r1, c1)과 (r2, c2)는 인접

학생의 순서와 각 학생이 좋아하는 학생 4명을 조사
한 칸에는 한 명의 학생만 앉을 수 있음
학교에 다니는 학생의 수는 N^2명
각 자리는 (1, 1) ~ (N, N)

규칙
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정함
2. 1을 만족하는 칸이 여러 개라면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정함
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정함

규칙에 따라 자리를 모두 정한 뒤 학생의 만족도 총 합을 구해 출력하자.
학생의 만족도는 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
0명 -> 0
1명 -> 1
2명 -> 10
3명 -> 100
4명 -> 1000
'''

def rule1(likes, seats, result):
  maxCnt = 0

  # 각 자리가 비어있을 경우,
  # 주변의 좋아하는 학생 수를 파악한 뒤 현재 max보다 많다면 result를 비우고 새롭게 위치 추가
  # 현재 max와 같다면 result에 위치 추가
  for i in range(1, len(seats)):
    for j in range(1, len(seats[i])):
      if seats[i][j] == 0:
        tmpCnt = 0
        # 상하좌우 확인
        if i > 1 and seats[i - 1][j] in likes:
          tmpCnt += 1
        if i < len(seats) - 1 and seats[i + 1][j] in likes:
          tmpCnt += 1
        if j > 1 and seats[i][j - 1] in likes:
          tmpCnt += 1
        if j < len(seats) - 1 and seats[i][j + 1] in likes:
          tmpCnt += 1
        
        if tmpCnt > maxCnt:
          maxCnt = tmpCnt
          result = set()
          result.add((i, j))
        elif tmpCnt == maxCnt:
          result.add((i, j))
  
  return result

def rule2(seats, rule1Result, rule2Result):
  maxCnt = 0

  for seat in rule1Result:
    tmpCnt = 0
    x, y = seat
    # 상하좌우 확인
    if x > 1 and seats[x - 1][y] == 0:
      tmpCnt += 1
    if x < len(seats) - 1 and seats[x + 1][y] == 0:
      tmpCnt += 1
    if y > 1 and seats[x][y - 1] == 0:
      tmpCnt += 1
    if y < len(seats) - 1 and seats[x][y + 1] == 0:
      tmpCnt += 1
    
    if tmpCnt > maxCnt:
      maxCnt = tmpCnt
      rule2Result = set()
      rule2Result.add((x, y))
    elif tmpCnt == maxCnt:
      rule2Result.add((x, y))
  
  return rule2Result

# MAIN
n = int(input())
studentSequence = []
likedStudents = [[] for _ in range(n ** 2 + 1)]

for _ in range(n ** 2):
  name, s1, s2, s3, s4 = map(int, input().split())
  studentSequence.append(name)
  likedStudents[name].append(s1)
  likedStudents[name].append(s2)
  likedStudents[name].append(s3)
  likedStudents[name].append(s4)

seats = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(len(studentSequence)):
  rule1Result = rule1(likedStudents[studentSequence[i]], seats, set())
  if len(rule1Result) > 1:
    rule2Result = rule2(seats, rule1Result, set())
    sortedResult = sorted(rule2Result)
    x, y = sortedResult[0]
    seats[x][y] = studentSequence[i]
  elif len(rule1Result) == 1:
    x, y = list(rule1Result)[0]
    seats[x][y] = studentSequence[i]

satisfaction = 0

for k in range(1, len(likedStudents)):
  find = False
  for i in range(1, len(seats)):
    for j in range(1, len(seats[i])):
      if seats[i][j] == k:
        cnt = 0
        # 상하좌우 검사
        if i > 1 and seats[i - 1][j] in likedStudents[k]:
          cnt += 1
        if i < len(seats) - 1 and seats[i + 1][j] in likedStudents[k]:
          cnt += 1
        if j > 1 and seats[i][j - 1] in likedStudents[k]:
          cnt += 1
        if j < len(seats) - 1 and seats[i][j + 1] in likedStudents[k]:
          cnt += 1

        if cnt == 1:
          satisfaction += 1
        elif cnt == 2:
          satisfaction += 10
        elif cnt == 3:
          satisfaction += 100
        elif cnt == 4:
          satisfaction += 1000
        
        find = True
        break
      if find:
        break

print(satisfaction)
