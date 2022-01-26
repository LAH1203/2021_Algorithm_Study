#상근이는 결혼식에 동기 중 친구와 친구의 친구 초대
#동기는 N, 학번은 1~N까지. 상근이 학번이 1
#친구 관계 리스트 소유. 
#결혼식에 초대할 사람 수 구하는 프로그램 작성


n = int(input()) #동기 수
m = int(input()) # 리스트 길이
relation = []
for _ in range(m):
    relation.append(list(map(int, input().split())))

#1과(상근이) 친구인 애들을 초대
#1과 친구인 애들과 친구인 애들까지 초대

friend = [] #친구 리스트
invite = [] #초대 리스트

for i in relation :
    i.sort()
    if 1 in i :
        friend.append(i[1])

for i in relation :
    i.sort()
    for j in friend:
        if(i[0]==j):
            if i[1] not in friend:
                invite.append(i[1])

result = len(friend)+len(invite)
print(result)