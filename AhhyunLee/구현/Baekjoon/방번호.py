roomNumber = list(map(int, input()))
numCount = [0 for _ in range(9)]

# 9는 6으로 판단하여 각 방번호의 숫자 개수를 세는 작업 수행
for number in roomNumber:
  if number == 9:
    numCount[6] += 1
  else:
    numCount[number] += 1

# 6의 개수 조정
if numCount[6] % 2 != 0:
  numCount[6] = numCount[6] // 2 + 1
else:
  numCount[6] //= 2

print(max(numCount))
