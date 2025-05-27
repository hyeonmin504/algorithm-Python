#리스트와 반복문

#리스트
#배열의 음수 인덱스
list = [1,2,3,4,5,6,7,8,9,0]
print(list[-1] == 4)
print(list[-2] == 3)

#배열의 출력 형식
#모든 배열 값이 출력된다
print("list =", list)

#append
#리스트명.append(요소) 한 번에 한 개

#insert
#리스트명.insert(위치, 요소)

#extend
#리스트명.extend(리스트) 리스트명 뒤에 리스트를 붙여 이음

#리스트 요소 제거하기 2가지
#1. 인덱스로 제거하기
#del, pop
del list[0]
list.pop(0) #default = -1

#범위 제거 가능
del list[0:2]

#2. 값으로 제거하기
#remove
#값이 없으면 에러
print(list.remove(5))

#in
#배열 내부에 값 있는지 확인
print(8 in list)
print(8 not in list)

print(list)

#반복의 여러 형태
for i in range(3):
    print(i)

for q in list:
    print(q)
# ==
k = 0
for j in list:
    print(list[k])
    k += 1

#딕셔너리(키: 값)와 반복문
dict = {
    "name": "이름",
    "type": "타입",
    "ingre": ["a","b","c"]
}
print(dict["ingre"][2])
#딕셔너리 추가, 제거
dict["price"]=5000
del dict["type"]
print(dict)
#키에 값이 없는 경우 접근 시 keyError 발생
# 해결 방법 2가지
#1. if로 따라서 확인 먼저 하기
one = input()
if one in dict:
    print(dict[one])
else:
    print("키가 존재하지 않음")
#2. get() -> 키가 없는 경우 None 반환
if dict.get("name"):
    print("key")
else:
    print("no key")

for secondary in dict:
    print(secondary,":",dict[secondary])

#범위 range()
#0~10
range(10)
#10~15
range(10,16)
# 2 4 6 8
for a in range(2,10,2):
    print(a)

#rang 내부에 / 사용 시 float로 변환되기 때문에 에러
range(0,8//4)

#일반적으로 많이 사용하는 방식
for i in range(len(list)):
    print(i,":",list[i])
print("------------")
#역순
for i in range(len(list)-1,-1,-1):
    print(i,":",list[i])
print("------------")
#역순2
for i in reversed(range(len(list))):
    print(i,":",list[i])
print("------------")
#역순3
print(list[::-1])

#enumerate()
#리스트에서 현재 인덱스를 쉽게 사용하기
for i, value in enumerate(list):
    print(i,":",value)

#items()
#딕셔너리에서 현재 인덱스를 쉽게 사용하기
for key,value in dict.items():
    print(key,":",value)

#리스트 내포
#리스트 이름 = [포현식 for 반복자 in 반복할 수 있는 것]
array = [i*i for i in range(0,20,2)]
print(array)
#리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
array2 = [j for j in array if j != 4]
print(array2)