const solution = (people, limit) => {
    let answer = 0;
    
    // 배열 내림차순 정렬
    people.sort((a, b) => b - a);
    
    // minIdx: 아직 타지 않은 사람 중 가장 가벼운 사람의 위치
    // maxIdx: 아직 타지 않은 사람 중 가장 무거운 사람의 위치
    let minIdx = people.length - 1;
    let maxIdx = 0;
    
    // 모든 사람 태우기
    while (maxIdx < minIdx) {
        // 가벼운 사람도 탈 수 있으면 태우기
        if (limit >= people[maxIdx] + people[minIdx]) {
            minIdx--;
        }
        // 무거운 사람 태우기
        maxIdx++;
        answer++;
    }

    // 만약 아직 한 사람이 타지 않았으면 마저 태우기
    if (minIdx === maxIdx) {
        answer++;
    }
    
    return answer;
}