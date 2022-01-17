startIndex = input()
row, column = int(startIndex[1]), ord(startIndex[0]) - ord('a') + 1
count = 0
# 이동 경로
ways = [
  (-2, -1),
  (-2, 1),
  (2, -1),
  (2, 1),
  (-1, -2),
  (1, -2),
  (-1, 2),
  (1, 2)
]

for way in ways:
  nextRow = row + way[0]
  nextColumn = column + way[1]
  # 가능한 경우에만 count 1 증가
  if nextRow > 0 and nextRow <= 8 and nextColumn > 0 and nextColumn <= 8:
    count += 1

print(count)
