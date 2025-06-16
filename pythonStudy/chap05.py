#chap05 함수
#형태
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times(
    "안녕"
    "하세요\n"
    "이사람아"
    ,
    5
)

#가변 매개변수
#가변 매개변수 뒤에는 일반 매개변수가 올 수 없습니다
#가변 매개변수는 하나만 사용 가능합니다.
def print_value_times(cnt,*values):
    for i in range(cnt):
        for value in values:
            print(value)
        print()

print_value_times(3, "안녕", "웃긴", "함수네")

#기본 매개변수
#매개변수를 입력하지 않았을 때 기본으로 들어가는 값입니다.
#마지막에 써준다.
def print_default_times(value,n=2):
    for i in range(n):
        print(value)
print_default_times("기본 매개변수")

#키워드 매개변수
# 가변 + 키워드 매개변수
def print_value_default(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
print_value_default("가변", "+", "키워드\n", n=3)

#키워드 매개변수
# 기본 + 키워드 매개변수
def print_n_default(a,b=10,c=100):
    print(a + b + c)
print_n_default(2,20,200)
print_n_default(a=3,b=30,c=300)
print_n_default(c=400,b=40,a=4)
print_n_default(1,c=0)
print()

#global 함수
#함수 내부에서 함수 외부에 있는 변수를 참조하지 못한다.
#따라서 global 키워드를 통해 참조한다
cnt = 0
def glo_fun(n):
    global cnt
    cnt += n
    return print(cnt)

glo_fun(100)

#튜플: 함수와 함꼐 사용되는 리스트와 비슷한 자료형으로
#     리스트와 다른 점은 한변 결정된 요소는 바꿀 수 없다.
tuple_test = (10, 20, 30)
list_test = [10, 20, 30]
print_default_times(tuple_test)

#튜플로 변수 값 저장 및 교환하는 법
a,b = 10, 20
a,b = b,a
print_value_default(a,b)

#튜플로 함수 값 리턴받는 법
def test():
    return 100,200
c,d = test()
print_value_default(c,d)

#filter(함수, 리스트)
#filter() 함수는 리턴이 True인 것으로 새로운 리스트를 구성해주는 함수
#map(함수, 리스트)
#map()함수는 리턴값으로 새로운 리스트를 구성해주는 함수
print()

#람다: 간단하게 함수를 바로 사용하는 것
#map함수와 람다로 구현
print(list(map(lambda x:x*x, list_test)))
#filter함수와 람다로 구현
print(list(filter(lambda x:x<20, list_test)))
x_y = lambda x, y: x * y

#텍스트 파일 처리
#파일 열기: 파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)
#파일 닫기: 파일 객체.close

#제네레이터
#제네레이터 객체는 함수의 코드를 조금씩 실행할 때 사용함
#next(제네레이터를 사용한 함수 이름)함수를 만날 때 마다 함수가 시작되고 함수 내 yield 객체까지 실행된다
#함수가 yield를 만나지 못하고 끝나면 오류가 난다.