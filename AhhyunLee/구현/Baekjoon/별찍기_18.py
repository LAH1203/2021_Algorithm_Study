def drawTriangle(x, y, n, answer):
  row = 2 ** n - 1
  column = 2 * row - 1

  if n == 1:
    answer[x][y] = '*'
    return
  
  if n % 2 != 0:    # 홀수
    # 정삼각형
    for i in range(row - 1, -1, -1):
      answer[x + row - i - 1][y + i] = '*'
      answer[x + row - i - 1][y + column - i - 1] = '*'
      if i == 0:
        for j in range(1, column - 1):
          answer[x + row - 1][y + j] = '*'
    drawTriangle(x + 2 ** (n - 1) - 1, y + 2 ** (n - 1), n - 1, answer)
  else:             # 짝수
    # 역삼각형
    for i in range(row):
      answer[x + i][y + i] = '*'
      answer[x + i][y + column - i - 1] = '*'
      if i == 0:
        for j in range(1, column - 1):
          answer[x][y + j] = '*'
    drawTriangle(x + 1, y + 2 ** (n - 1), n - 1, answer)

n = int(input())
row = 2 ** n - 1
column = 2 * row - 1
answer = [[' '] * column for _ in range(row)]

drawTriangle(0, 0, n, answer)

for i in answer:
  print(''.join(i).rstrip())
