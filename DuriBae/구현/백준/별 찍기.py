#이전 별을 한 파트로 하는 별삼각형 만들기
#홀수는 정방향, 짝수는 역방향
#인터넷 참고
#star=1, row=1, col =1
#star=2, row=1+2^2, col =1+2^(2-1)
#star=3, row=1+2^2+2^3, col=1+2^(2-1)+2^(3-1)
#star=k, row=1+2^2+++2^k, col=1+2^(2-1)++++2^(k-1)
#등비수열의 합
#row = 2^(k+1)-3
#col = 2^k-1



star = int(input())
row = pow(2,star+1)-3
col = pow(2,star)-1

stars = [[' ']*row for _ in range(col)]

def stamp(star, x, y):
    if star ==1 :#하나일 때
        stars[y][x] = '*'
        return
    row = pow(2,star+1) - 3
    col = pow(2,star)- 1
    # 짝수일때
    if star % 2 == 0:
        for i in range(x,row+x):
            stars[y][i] = '*'
        for i in range(col):
            stars[y+i][x+i] = '*'
            stars[y+i][x+row-1-i] = '*'
        # 재귀 호출
        stamp(star-1,pow(2,star-1)+x,y+1)
    # 홀수 일때
    else:
        for i in range(x,row+x):
            stars[y+col-1][i] = '*'
        for i in range(col):
            stars[y+i][x+row//2-i]='*'
            stars[y+i][x+row//2+i]='*'
        # 재귀 호출
        stamp(star-1,pow(2,star-1)+x,y+col//2)

stamp(star,0,0)

if star % 2 == 0:
    for i in range(col):
        for j in range(row-i):
            print(stars[i][j], end="")
        print()
else:
    for i in range(col):
        for j in range(row-col+i+1):
            print(stars[i][j], end="")
        print()


    

