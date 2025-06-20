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
#제일 작은 수 제거하기
def solution2_1(arr):
    min_num = min(arr)
    arr.remove(min_num)
    if arr == []:
        return [-1]
    return arr
#내적
def solution2_2(a, b):
    sum = 0
    for i in range(0,len(a)):
        sum += (a[i] * b[i])
    return sum
#수박수박수박수박수?
def solution2_3(n):
    if n%2 == 0:
        return "수박"*(n//2)
    return "수박"*(n//2)+"수"
#약수의 개수와 덧셈
def solution2_4(left, right):
    sum = 0
    for i in range(left,right+1):
        if int(i**0.5) == i**0.5:
            sum -= i
        else: sum +=i
    return sum
#문자열 내림차순으로 배치하기
def solution2_5(s):
    return ''.join(sorted(s, reverse = True))
#부족한 금액 계산하기
def solution2_6(price, money, count):
    rest = money - sum(i for i in range(1,count+1))*price
    if rest > 0:
        return 0
    return -rest
#문자열 다루기 기본
def solution2_7(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
#행렬의 덧셈
def solution2_8(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            arr1[i][j] += arr2[i][j]
    return arr1
#직사각형 별찍기
a, b = map(int, input().strip().split(' '))
for i in range(0,b):
    print('*'*a)
#같은 숫자는 싫어 -> [:] 슬라이싱은 인덱스를 초과해도 오류가 안뜬다.
def solution2_10(arr):
    arr.append(10)
    return [arr[i] for i in range(0,len(arr)-1) if arr[i] != arr[i+1]]
#최대공약수 최소공배수
def solution2_11(n, m):
    answer = []
    n_measure = [i for i in range(1,n+1) if n%i == 0]
    m_measure = [i for i in range(1,m+1) if m%i == 0]
    if n<m:
        answer.append(max([i for i in n_measure if m%i == 0]))
        answer.append(min([i*n for i in m_measure if (n*i)%m == 0]))
    else:
        answer.append(max([i for i in m_measure if n%i == 0]))
        answer.append(min([i*n for i in m_measure if (n*i)%m == 0]))
    return answer
#def solution(n, m): -> 유클리드 공약수 공배수
    # def gcd(a, b): 최대 공약수: a를 b로 나눈 나머지로 계속 나누다 0이 되면 b가 최대공약수다
    #     while b:
    #         a, b = b, a % b
    #     return a
    #
    # g = gcd(n, m)
    # l = (n * m) // g 최소 공배수: a*b를 최대공약수로 나누면 최소공배수다.
    # return [g, l]
#크기가 작은 부분문자열
def solution2_12(t, p):
    return len([i for i in range(0,1+len(t)-len(p)) if t[i:i+len(p)] <= p])
#예산
def solution2_13(d, budget):
    d_sorted = sorted(d)
    count=0
    for i in d_sorted:
        budget -= i
        if budget >= 0 :
            count +=1
        else: break
    return count
#3진법 뒤집기 -> int에는 n진법인 tmp를 10진법으로 변환해
def solution2_14(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
#삼총사
def solution2_15(number):
    result = 0
    for i in range(0,len(number)):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):
                if number[i]+number[j]+number[k] == 0:
                    result +=1
    return result
#이상한 문자 만들기
def solution2_16(s):
    list_str = s.split(" ")
    result = ""
    for word in list_str:
        temp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                temp += word[i].upper()
            else :
                temp += word[i].lower()
        result = result + temp + ' '
    return result[0:-1]
#파이썬의 문자열(str)은 **immutable(불변)**이라서,
#i[j] = something처럼 인덱스로 직접 수정할 수 없습니다.
#최소 직사각형
def solution2_17(sizes):
    wide = 0
    high = 0
    for size in sizes:
        temp_w = 0
        temp_h = 0
        if size[0] < size[1]:
            temp_w = size[1]
            temp_h = size[0]
        else :
            temp_w = size[0]
            temp_h = size[1]
        if wide < temp_w:
            wide = temp_w
        if high < temp_h:
            high = temp_h
    return wide * high
# def solution2_17(sizes): -> 2차원을 돌려서 1차원의 값을 가져옴
#     row = 0
#     col = 0
#     for a, b in sizes:
#         if a < b:
#             a, b = b, a
#         row = max(row, a)
#         col = max(col, b)
#     return row * col