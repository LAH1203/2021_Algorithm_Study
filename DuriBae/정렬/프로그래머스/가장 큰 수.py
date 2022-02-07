#0또는 양의 정수가 주어졌을 때, 정수를 이어 븉여 만들 수 있는 가장 큰 수.
#[6,10,2] -> [6102,6210,1062,2610,2106]을 만들 수 있고 가장 큰 수는 6210
#0또는 양의 정수가 담긴 배열이 매개변수로 주어질 때, 순서를 재배치하여 만들 수 잇는 가장 큰 수를 문자열로 바꾸어 return
#인터넷 참고(lambda 함수 사용)
#https://esoongan.tistory.com/103


numbers = [6,10,2]

def solution(num): 
    num = list(map(str, num)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))

print(solution(numbers))



