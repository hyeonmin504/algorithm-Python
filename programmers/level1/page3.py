#푸드 파이트 대회
def solution3_1(food):
    answer = ''
    for index, value in enumerate(food):
        if 1 < value:
            for _ in range(0,value//2):
                answer += str(index)
    another_food = answer[::-1]
    answer += '0'
    answer += another_food
    return answer
#숫자 문자열과 영단어
def solution3_2(s):
    result = ''
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    temp = 0
    for index, value in enumerate(s):
        if not "0"<= value <="9":
            if s[index-temp:index+1] in num :
                result += str(num.index(s[index-temp:index+1]))
                temp = 0
            else:
                temp += 1
        else:
            result += value
            temp = 0
    return int(result)
#num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)
#K번째 수
def solution3_3(array, commands):
    result = []
    sliced = []
    for i in commands:
        sliced = array[i[0]-1:i[1]]
        sliced.sort()
        result.append(sliced[i[2]-1])
    return result
#콜라 문제
def solution3_4(a, b, n):
    bottle = 0
    rest = 0
    while(n >= a):
        bottle += n//a*b
        rest = n%a
        n = n//a*b + rest
    return bottle
#문자열 내 마음대로 정렬하기
def solution3_5(s):
    answer = []
    for string in strings:    
        answer.append(string[n] + string)
    answer.sort()
    return [i[1:] for i in answer ]
#명예의 전당 (1)
def solution3_6(s):
    answer = []
    top_3 = []
    for yesterday,point in enumerate(score):
        if k > yesterday:
            top_3.append(point)   
        elif min(top_3) < point:
            top_3.remove(min(top_3))
            top_3.append(point)
        answer.append(min(top_3))
    return answer
#카드 뭉치
def solution3_7(cards1, cards2, goal):
    for string in goal:
        if cards1 and cards1[0] == string:
            cards1.pop(0)
            continue
        elif cards2 and cards2[0] == string:
            cards2.pop(0)
            continue
        return "No"
    return "Yes"    
#[1차] 비밀지도]
def solution3_8(n, arr1, arr2):
    answer = [] 
    col = 0
    for num1, num2 in zip(arr1, arr2):
        rowData = ''
        for i in range(0,n):
            if num1 % 2 == 1 or num2 % 2 == 1:
                rowData = '#' + rowData
            else :
                rowData = ' ' + rowData
            if num1 >= 1:
                num1 = num1//2
            if num2 >= 1:
                num2 = num2//2
        answer.append(rowData)
        print(answer)
        col += 1
    return answer
#추억 점수
def solution3_9(name, yearning, photo):
    answer = []
    name_dict = dict(zip(name,yearning))
    for index, array in enumerate(photo):
        sum_year = 0
        for string in photo[index]:
            if string in name_dict:
                sum_year += name_dict[string]
        answer.append(sum_year)
    return answer
#기사단원의 무기
def solution3_10(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        yaksu_cnt = 0
        for index in range(1,int(i**0.5) +1):
            if i%index == 0:
                yaksu_cnt += 1
                if i/index != index:
                    yaksu_cnt += 1
            if yaksu_cnt > limit:
                yaksu_cnt = power
                break
        answer += yaksu_cnt
    return answer
#폰켓몬
def solution3_11(nums):
    return min(len(nums)//2, len(set(nums)))