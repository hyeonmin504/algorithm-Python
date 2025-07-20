#[1차] 다트 게임
def solution4_1(dartResult):
    sdt = {'S':1,'D':2,'T':3}
    cnt, i = 0, 0
    dart = []
    while i < len(dartResult):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit():
            point = 10
            i = i+1
        else :
            point = int(dartResult[i])
        i += 1
        point **= sdt[dartResult[i]]
        i += 1
        if i<len(dartResult) and dartResult[i] == '*':
            point *= 2
            if cnt != 0:
                dart[cnt-1] *= 2
            i += 1
        elif i<len(dartResult) and dartResult[i] == '#':
            point *= -1
            i += 1
        dart.append(point)
        cnt += 1
    return sum(dart)
# 로또의 최고 순위와 최저 순위
def solution4_2(lottos, win_nums):
    zero_cnt = len([0 for i in lottos if int(i) == 0])
    same_cnt = len([0 for i in lottos if i in win_nums])
    best = 7-zero_cnt-same_cnt
    worst = 7-same_cnt
    if best > 6:
        best = 6
    if worst > 6:
        worst = 6
    return [best,worst]
#둘만의 암호
def solution(s, skip, index):
    abc_skip = [chr(j) for j in range(ord('a'), ord('z')+1) if chr(j) not in skip]
    answer = ''
    for char in s:
        i = abc_skip.index(char)
        answer += abc_skip[(i+index) % len(abc_skip)]
    return answer
#문자ㄹ 나누기
def solution4_3(s):
    answer, first, another = 0, 0, 0
    for index, char in enumerate(s):
        if first == 0 or temp == char:
            temp = char
            first += 1
        else :
            another += 1
        if first == another or index == len(s)-1:
            answer += 1
            temp = ''
            first, another = 0, 0
    return answer
#대충 만든 자판
def solution4_4(keymap, targets):
    answer = []
    dict = {}
    for string in keymap:
        for index, char in enumerate(string):
            if char not in dict or dict[char] > index+1:
                dict[char] = index + 1
    for target in targets:
        temp = 0
        for char in target:
            if char not in dict:
                temp = -1
                break
            temp += dict[char]
        answer.append(temp)
    return answer
#[PCCE 기출문제] 9번 / 이웃한 칸
