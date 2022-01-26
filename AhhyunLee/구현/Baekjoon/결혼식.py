'''
동기 중 친구 & 친구의 친구
-> 학번: 1 ~ N
-> 상근이의 학번은 1

동기들의 친구 관계를 담은 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구해보자
'''

def dfs(people, me, friends, count):
  for i in range(len(people[me])):
    if people[me][i] and count < 2:
      friends.add(i)
      people[me][i] = False
      people[i][me] = False
      dfs(people, i, friends, count + 1)

# MAIN
n = int(input())
m = int(input())
people = [[False for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  people[a][b] = True
  people[b][a] = True

friends = set()

dfs(people, 1, friends, 0)

print(len(friends))
