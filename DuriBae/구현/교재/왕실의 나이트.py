

n = str(input())
step = [(2,1),(2,-1),(-2,1),(-2,-1), (1,2),(-1,2),(1,-2),(-1,-2)] #이동경로
types = ['a','b','c','d','e','f','g','h'] #열 타입
count = 0 #경우의 수

#입력받은 위치를 수로 계산. 열은 인덱스로 반환하여 수로 계산
x = int(n[1])#행
y = int(types.index(n[0]))+1 #열


#이후 step만큼 더하여 가능할 경우 count에 추가
for i in step :
    nx = x+i[1]
    ny = y+i[0]
    #받은 위치에서 나가면 안되는 범위 설정
    if(nx<1 or ny<1 or nx>8 or ny>8):
        continue
    count +=1

print(count)


