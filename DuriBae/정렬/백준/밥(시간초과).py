#식당에 두 개의 메뉴. A로 가면 5천원 메뉴, B로 가면 천원 메뉴
#대면 수업 시작 -> N일동안 매일 두 메뉴 중 하나를 골라 먹어야 함.
#N일간 메뉴는 이미 공지되었고, 각 메뉴 맛 수치도 매겨두었다.
#N일간 X원 이하의 금액을 써야 한다.
#N일간 지정된 금액으로 맛의 합을 최대화 해야한다.
#입력 : 두 정수 N, X가 주어진다. 
# : N개 줄에 A메뉴 맛과 B메뉴 맛이 공백을 두고 주어진다.
#출력 : 고른 메뉴의 맛의 합을 최대화했을 때 값을 구하라.


n,x = map(int,input().split())
a = []
b = []
point = []
money = x
result = 0

for _ in range(n):
    data = list(map(int,input().split()))
    a.append(data[0])
    b.append(data[1])
    point.append(data[0]-data[1])

money -=n*1000 #모든 날에 밥을 먹어야 하기 때문에 미리 천원어치를 빼둔다.
#point에서 가장 이득이 큰 것부터 차례대로 추가한다. 

while(money>=4000 and max(point)>0):
    #비싼 밥을 먹는 게 이득일 때 
        idxP = point.index(max(point))
        result += a[idxP]
        a[idxP] = 0 #추가 후 값 바꾸기
        money -= 4000
        point[idxP]=0 #추가 후 값 바꾸기


for i in range(n):
    if(a[i]!=0):
        result+=b[i]


print(result)