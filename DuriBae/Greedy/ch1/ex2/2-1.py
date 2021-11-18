import time # 시간 계산

#숫자 카드 게임
#카드 중 가장 높은 숫자 카드를 뽑는 게임
#n*m 형태로 놓인 카드 행과 열
#행 선택 후 가장 낮은 카드 뽑기
#행에서 낮은 카드 뽑을 걸 고려하여 높은 숫자 뽑도록 전략 세움

n, m = map(int, input().split())
#가장 작은 수를 찾고, 그 중 가장 큰 값을 뽑음.

arr = [list(map(int, input().split())) for i in range(n)]
#print(arr)

start_time = time.time() #측정 시작

num = []

for j in range(n):
    num.append(min(arr[j]))

result=max(num)
print(result)

end_time = time.time() #측정 종료
print("수행시간 :", end_time - start_time) # 수행 시간 출력

#풀이시간 : 27분
# 2차원 배열 입력받기가 어려웠음.
