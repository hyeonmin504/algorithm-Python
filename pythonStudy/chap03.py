#chap03 조건문

#범위구하기 중겁 비교 가능
print(10<14<15)

#not 연산자 == (!) //java ver
print(not True)

#and 연산자 == (&&) // java ver
print(True and True)

#or 연산자 == || // java ver
print(True or False)

#if 표현식:
# 조건문에 None, 0, 0.0,빈 컨테이너(빈 문자열, 빈 리스트, 빈 튜플 등...) -> False
# 그 외에는 전부 True로 반환
if True:
    print("Trueeeee")
    print(False)
elif True:
    print("elif")
else:
    print("else")
str = input()

#마지막 데아터 값
print(str[-1])
print(str.isalpha())
print(str.isdecimal())
print(str[-1].isdecimal())
print(str[-1].isalpha())

#pass
#아무것도 안하고 넘어감
if int(input()) > 0:
    pass

#raise NotImplementError
#강제 오류를 통해 미구현을 의미
if int(input()) > 0:
    raise NotImplementedError