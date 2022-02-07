# MAIN
t = int(input())

for _ in range(t):
  n = int(input())
  numbers = []
  for _ in range(n):
    numbers.append(input())
  
  numbers.sort()
  check = True
  
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] in numbers[j]:
        check = False
        break
    if check == False:
      break
  
  if check:
    print("YES")
  else:
    print("NO")
