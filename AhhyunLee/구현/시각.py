def isIn3(hour, minute, second):
  return str(hour).count('3') > 0 or str(minute).count('3') > 0 or str(second).count('3') > 0

n = int(input())
count = 0
now = {
  'hour': 0,
  'minute': 0,
  'second': 0,
}

# n시 59분 59초까지 완탐
while now['hour'] != n or now['minute'] != 59 or now['second'] != 59:
  # 시, 분, 초에 3이 하나라도 포함되어 있다면 count 1 증가
  if isIn3(now['hour'], now['minute'], now['second']):
    count += 1
  # 1초 증가
  now['second'] += 1
  # 분 또는 초가 60일 경우, 위의 단위를 1 증가시키고 0으로 초기화
  if now['minute'] == 60:
    now['hour'] += 1
    now['minute'] = 0
  if now['second'] == 60:
    now['minute'] += 1
    now['second'] = 0

print(count)
