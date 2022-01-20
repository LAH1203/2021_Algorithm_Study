#교실 n*n 학생은 n^2
#(r,c) r행 c열 가장 위가 (1,1) 오른쪽 아래가 (n,n)
#학생 번호는 1~n^2
#학생의 순서 정했고, 학생이 좋아하는 학생 4명도 조사.
#한 칸에 학생 1명. |r1-r2|+|c1-c2|=1을 만족하는 두 칸이
#(r1,c1)과 (r2,c2)를 인접한다고 한다.
#1. 비어있는 칸 중에 좋아하는 학생과 인접한 칸이 가장 많은 칸으로 자리를 정한다.
#2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
#3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 
#가장 작은 칸으로 자리를 정한다.


n = int(input())
students_list = []
table_list = [[0 for j in range(n)] for i in range(n)]
dic = {}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
 
for i in range(n ** 2):
    students_list.append(list(map(int, input().split(" "))))
 
 
def cnt(f_list, i, j):
    count = 0
    f_count = 0
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if table_list[ny][nx] == 0:
                count += 1
            if f_list:
                if table_list[ny][nx] in f_list:
                    f_count += 1
    return count, f_count
 
 
for s in students_list:
 
    friend = []
    # table_list안에 내가 좋아하는 칭구가 있는지 확인해야함
    for i in range(1, 5):
        if s[i] in dic:
            friend.append(s[i])
 
    # 좋아하는 친구가 이미 자리를 잡았을때
    if friend:
        # 모든 자리를 탐색하자
        # 주변에 친한친구 수, 근처 비어있는곳의 갯수, i좌표, j좌표
        max_cnt = []
        for i in range(n):
            for j in range(n):
                if table_list[i][j] == 0:
                    result, f_cnt = cnt(friend, i, j)
                    if not max_cnt:
                        max_cnt = [f_cnt, result, i, j]
                    if f_cnt > max_cnt[0]:
                        max_cnt = [f_cnt, result, i, j]
                    elif f_cnt == max_cnt[0] and result > max_cnt[1]:
                        max_cnt = [f_cnt, result, i, j]
 
        # 자리를 찾았으면 앉히자
        table_list[max_cnt[2]][max_cnt[3]] = s[0]
        dic[s[0]] = s[1:]
 
 
    # 친구가 아직 자리를 잡기 전일때
    else:
        # 비어있는 곳의 갯수, i좌표, j좌표
        max_cnt = []
        for i in range(n):
            for j in range(n):
                if table_list[i][j] == 0:
                    result, f_cnt = cnt(friend, i, j)
                    if not max_cnt:
                        max_cnt = [result, i, j]
                    elif result > max_cnt[0]:
                        max_cnt = [result, i, j]
 
 
        # 자리를 찾았으면 앉히자
        table_list[max_cnt[1]][max_cnt[2]] = s[0]
        dic[s[0]] = s[1:]
 
# 다 앉힌 후에 점수를 계산하자
# 0:0 / 1:1 / 2:10 / 3:100 / 4:1000
point = 0
for i in range(n):
    for j in range(n):
        f_list = dic[table_list[i][j]]
        empty_val, f_cnt = cnt(f_list, i, j)
        if f_cnt == 0:
            point += 0
        elif f_cnt == 1:
            point += 1
        elif f_cnt == 2:
            point += 10
        elif f_cnt == 3:
            point += 100
        else:
            point += 1000
 
print(point)