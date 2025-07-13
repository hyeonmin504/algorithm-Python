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
