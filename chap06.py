#Chap06 예외 처리
#try - except - else 구문
try:    #예외가 일어날 확률이 높은 코드
    print("try")
except ValueError as e: #예외 처리
    print(e)
except Exception as e: #예외 처리
    print(e)
else:   #예외가 없을 때 try - else 순으로 실행
    print("else")
finally:#무조건 실행하는 코드
    print("finally")

#예외 고급