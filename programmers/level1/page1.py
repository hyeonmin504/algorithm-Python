#약수의 합
def solution1_1(n):
    sum = 0
    for i in range(1,n +1):
        if(n%i == 0):
            sum+=i
    return sum
#자릿수 더하기
def solution1_2(n):
    sum = 0
    array = list(str(n))
    for i in range(0, len(array)):
        sum += int(array[i])

    return sum
#자연수 뒤집어 배열로 만들기
def solution1_3(n):
    array = list(str(n))
    return [int(i) for i in array[::-1]]
#짝수와 홀수
def solution1_4(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
#평균 구하기
def solution1_5(arr):
    return sum(map(int, arr))/len(arr)
#x만큼 간격이 있는 n개의 숫자
def solution1_6(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer
#나머지가 1이 되는 수 찾기
def solution1_7(n):
    answer = 0
    for i in range(2,n):
        if n%i == 1 :
            return i
#문자열을 정수로 바꾸기
def solution1_8(s):
    return int(s)
#두 정수 사이의 합
def solution1_9(a, b):
    answer = 0
    if a<b:
        for i in range(a,b+1):
            answer+=i
    elif a>b:
        for i in range(b, a+1):
            answer+=i
    else: return a
    return answer
#문자열 내 p와 y의 개수
def solution1_10(s):
    answer = True
    array = list(str(s))
    p = 0
    t = 0
    for i in array:
        if i == "p" or i == "P":
            p += 1
        elif i == "y" or i == "Y":
            t += 1
    if p == t:
        return True
    return False

#실패 - 정수 내림차순으로 배치하기
def solution1_11(n):
    return
#정수 제곱근 판별
def solution1_12(n):
    return half(0, n, n)
def half(left, right, n):
    if left > right:
        return -1

    mid = (left + right) // 2
    if mid * mid == n:
        return (mid + 1) * (mid + 1)
    elif mid * mid < n:
        return half(mid + 1, right, n)
    else:
        return half(left, mid - 1, n)
#하샤드 수
def solution1_13(x):
    result = sum(map(int, str(x)))
    if x%result == 0:

        return True
    return False
#음양 더하기
def solution1_14(absolutes, signs):
    sum = 0
    for i in range(0,len(absolutes)):
        if signs[i] == False:
            sum -= absolutes[i]
        elif signs[i] == True:
            sum += absolutes[i]
    return sum
#없는 숫자 더하기
def solution1_15(numbers):
    return 45 - sum(map(int, set(numbers)))
#나누어 떨어지는 숫자 배열
def solution1_16(arr, divisor):
    result = []
    result = [i for i in arr if i%divisor == 0]
    if not result:
        return [-1]
    result.sort()
    return result
#서울에 김서방 찾기
def solution1_17(seoul):
    result = []
    for i in seoul:
        if i == "Kim":
            break
        result.append(i)
    return "김서방은 {}에 있다".format(len(result))
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
#콜라츠 추측
def solution1_18(num):
    for i in range(0,500):
        if num == 1:
            return i
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return -1
#핸드폰 번호 가리기
def solution1_19(phone_number):
    new_phone_num = ""
    for i in range(0,len(phone_number)):
        if i >= len(phone_number)-4:
            new_phone_num += phone_number[i]
        else:
            new_phone_num += "*"
    return new_phone_num
# return ('*'*(len(s)-4)) + s[-4:]
#가운데 글자 가져오기
def solution1_20(sa):
    s = list(sa)
    if len(s)%2==1:
        return s[len(s)//2]
    return s[len(s)//2-1] + s[len(s)//2]
#def string_middle(str):
#   return str[(len(str)-1)//2 : len(str)//2 + 1]