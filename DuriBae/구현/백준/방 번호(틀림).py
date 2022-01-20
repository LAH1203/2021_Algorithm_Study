#다솜이가 은진이의 옆집에 이사옴.
#방 번호에 플라스틱 숫자 붙임. 0~9가 한 세트.
#필요한 세트 개수의 최솟값 (6과 9는 뒤집어서 사용 가능)

#6이나 9가 나오면 2개당 한 세트로 취급
#다른 수에서 중복이 나오면 세트 추가
#숫자를 입력받고, 정렬.
#이전 수보다 크면 세트 냅둠
#이전 수와 같으면 카운트 증가
#현재 수가 6이나 9면 카운트 안하고 빈 리스트에 넣어둠
#6이랑 9가 모여있는 리스트의 개수를 세고, 2/n -1 만큼 카운트 추가
#이때 반올림할 것.

n = str(input()) #문자열로 입력받음

number = [] #숫자를 담을 리스트
for i in n :
    number.append(int(i))

number.sort() #오름차순으로 정렬
sixnine = []
sncount = 0
count = 1
for i in range(len(number)):
    if(i-1 <0):
        if(number[i]==6 or number[i]==9):
            sixnine.append(number[i])
        continue
    if(number[i]==6 or number[i]==9):#6이나 9가 나왔을 때
        sixnine.append(number[i])
        continue
    if(number[i] == number[i-1]): #이전 수와 같으면
        count +=1

if(len(sixnine)!=0):
    sncount = round(len(sixnine)/2+0.1)-1 #반올림 오차 해소를 위해 0.1 더한다
result = int(count+sncount)
print(result)