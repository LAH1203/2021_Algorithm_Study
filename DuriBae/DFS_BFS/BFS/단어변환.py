from collections import deque

begin, target = map(str, input().split())
words = list(map(str, input().split()))

visited = [False]*(len(words))


def bfs(begin, target, words, visited):
    queue = deque([])
    queue.append((begin, 0))
   
    while queue :
        word, depth = queue.pop()
        if(word == target):
            return depth
        for i in range(len(words)):
            if visited[i] == True:
                continue

            count = 0
            for a,b in zip(word, words[i]):
                if a!=b:
                    count += 1
            if(count==1):
                visited[i] = True
                queue.append((words[i], depth+1))
          

if target not in words:
    print(0)

else :
    print(bfs(begin, target, words, visited))
