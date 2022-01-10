# 두 개의 단어 begin, target과 단어의 집합 words
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있다.
# 2. words에 있는 단어로만 변환할 수 있다.
#예. begin = hit, target = cog
#words = [hot, dot, dog, lo, log, cog]
# 변환 => hit -> hot -> dot -> dog -> cog
# 최소 몇 단계의 과정으로 begin을 target으로 변환할 수 있는지 return

# begin에서 target까지 하나씩 다른 단어를 찾기
# words 안에 target 없으면 0 리턴
# 있으면 바꾸기 진행
#1글자만 다른 단어 찾기 과정을 반복
#bfs가 나온 인터넷 참고해서 dfs 과정으로 만들어보려 했으나 실패...

begin, target = map(str, input().split())
words = list(map(str, input().split()))
answer = 0
visited = [False]*(len(words))

def dfs(begin,target,words,visited):
    global answer
    if(begin==target):
        return answer

    for i in range(len(words)):
        if visited[i] == True:
            continue
        count = 0
        for a,b in zip(begin,words[i]):
            if a!=b:
                count += 1
        if(count==1):
            visited[i] = True
            answer +=1
            dfs(words[i],target,words,visited)

if target not in words:
    print(0)

else :
    print(dfs(begin, target, words, visited))
    