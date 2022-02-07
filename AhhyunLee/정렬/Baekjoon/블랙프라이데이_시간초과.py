# MAIN
n, c = map(int, input().split())
weights = list(map(int, input().split()))
check = False

if c in weights:
  check = True
else:
  for i in range(n):
    for j in range(i + 1, n):
      weight = weights[i] + weights[j]
      if weight == c:
        check = True
        break
      elif weight < c:
        goal = c - weight
        if goal in weights and goal != weights[i] and goal != weights[j]:
          check = True
          break
    if check:
      break

if check:
  print(1)
else:
  print(0)
