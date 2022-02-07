n, x = map(int, input().split())
days = []

for _ in range(n):
  a, b = map(int, input().split())
  days.append({'a': a, 'b': b})

# x원으로 최대 A 메뉴를 몇 번 먹을 수 있는지 세기
eatAble_A = min(x // 5000, n)

days = sorted(days, key=lambda x : (x['a'], x['b']), reverse=True)

answer = 0
eatCnt = 0

for _ in range(eatAble_A):
  answer += days[0]['a']
  del days[0]
  eatCnt += 1

days = sorted(days, key=lambda x : (x['b'], x['a']), reverse=True)

for _ in range(min(len(days), (x - eatCnt * 5000) // 1000)):
  answer += days[0]['b']
  del days[0]

print(answer)
