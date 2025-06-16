#양의 실수
a= 157.93
print(a)
#음의 실수
a = -1858.2
print(a)
# 소수부가 0일 때 0을 생략
a=5.
print(a)

#지수 표현 방식 1*10^9 -> 실수형
a= 1e9
print(a)

a = 0.3 + 0.6
print(a)
print(round(0.3+0.6, 4))
if a == 0.9:
    print(True)
else :
    print(False)
#리스트 컴프리헨션 - 2차원 리스트를 초기화할 때 효과적
# 3 x 4 2차원에 전부다 0 값을 대입 한 경우
# _ :반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 자주 사용
n=4
m=3
array = [[0]*m for _ in range(n)]
print(array)
#리스트 관련 기타 메서드
#.append()
#.sort() # O(NlogN)
#.sort(reverse = True)
#.reverse()
#.insert()
#.count()
#.remove() # removeAll 없음

def solution(n):

    (int)sum = 0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
