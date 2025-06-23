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