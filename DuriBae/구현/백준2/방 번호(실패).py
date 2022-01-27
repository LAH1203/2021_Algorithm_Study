#숫자는 0~9까지 한 세트
#방 번호가 주어졌을 때 필요한 세트의 개수, 최솟값
#6과 9는 뒤집어서 사용 가능.
#입력 : 다솜이 방 번호가 주어진다. 100만보다 작거나 같은 수
#출력 : 필요한 세트의 개수를 출력한다
#리스트를 만들고 리스트에 수가 있으면 빼고, 없으면 세트 추가= 말 그대로 리스트에 0~9 추가하기
#6이나 9는 6이나 9 중 남은 걸 빼기

num = [0,1,2,3,4,5,6,7,8,9] #쓰고 남은 세트
plus = [] #추가될 세트

n = input()
set = 1 #기본 1세트

for i in n :
    j = int(i)
    #print(num)
    #print(plus)
    if(j in num): #리스트에 수가 있으면 뺀다
        plus.append(j)#세트 추가시 보충될 수
        num.remove(j)
    else :
        if(j == 6 or j == 9): #6이나 9일 때
            if(6 in num):
                num.remove(6)
                plus.append(6)
                continue
            if(9 in num):
                num.remove(9)
                plus.append(9)
                continue
        set +=1 #수가 없을 때 세트 추가
        if(j in plus):
            plus.remove(j) #보충세트에서 수 빼기
        #print(plus)
        num+=plus #세트 보충
        plus = [] #보충세트 초기화
        

print(set)

