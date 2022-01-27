#인터넷 참고

n = input()

set = [0]*10 

for i in n :
    j = int(i)
    if(j==6 or j==9):
        if(set[6]<=set[9]):
            set[6]+=1
        else:
            set[9]+=1
    else:
        set[j]+=1
    
print(max(set))