const solution = (number, k) => {
    let answer = '';
    
    let idx = -1
    
    // number에서 k개를 제거한 숫자 뽑아내기
    for (let i = 0; i < number.length - k; i++) {
        let maxNow = '0';
        
        // 마지막으로 넣은 값의 다음 인덱스부터 k개의 수를 읽어냄
        for (let j = idx + 1; j <= i + k; j++) {
            // 더 큰 값이 나올 경우 갱신
            if (maxNow < number[j]) {
                maxNow = number[j]
                idx = j
                // 9를 만나면 반복문을 돌지 않고 무조건 종료
                if (maxNow === '9') {
                    break;
                }
            }
        }
        
        answer += maxNow;
    }
    
    return answer;
}