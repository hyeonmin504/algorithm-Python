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
