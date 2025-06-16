#chap2. 자료형
#정수 나누기 연산자 //
#몫을 반환한다
print("3 // 2=", 3 // 2)

#제곱 연산자 **
#값의 제곱을 나타낸다
print("2 ** 3=", 2 ** 3)

#input()
#값을 입력받는다. 이때 모든 값은 문자열
str = input()

#int(), float()
#문자열 -> int, float
a = "1"
b = "1.0"
int(a), float(b)

#format()
#숫자 -> 문자열
"{}".format(10)

#isOO
#문자열 구성 파악, 반환 값은 boolean
#.isalnum() -> 문자열이 알파벳 or 숫자
#.isalpha() -> 문자열이 알파벳
#.isdigit() -> 문자열이 숫자
#.isdecimal() -> 문자열이 정수

#.strip()
#문자열 양옆의 공백제거 .strip() == .trim() -> java

#.find(), rfind()
#문자열의 왼, 오른 쪽에서 시작해 처음 등장하는 위치를 찾고 숫자로 반환한다.
#없을 시 -1 반환

#split()

