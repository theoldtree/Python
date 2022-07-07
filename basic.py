print("abc") #주석
name = input("your name: ")
print("your name is "+name)

n = int(input("input number for sum : "))
sum = 0
for i in range(1, n+1):
    sum += i
print("result of sum is :" + str(sum))

a = [1,2,3,4] #리스트, 수정/슬라이싱 가능
a[3] = 16
b= (10,11,12) # 튜블, 슬라이싱 가능, 수정 불가능
# b[2] = 13 -> 불가능한 연산
a = {1,2,3,4,5} # 집합 자료 형 -> 중복 허용 x , 순서가 없는 나열혈
greet = "hello" # 문자열은 튜플과 성질이 비슷하다
list(greet) # ['h','e','l','l','o']

#숫자의 연산
c = 3/2 # 정수/정수의 연산 결과가 실수가 됨 ㅋㅋ
print(type(c))
print(c) # 1.5 
e = 4/2
print(type(e))
print(e)
d = 3 ** 4 # 거듭제곱의 표현
print(d) # 81

#형 변환
float(), int(), tuple(), list(), str()

#문자열의 분리와 합치기
friends_list = "홍춘향 이몽룡 이도령"
print(', '.join(friends_list.split()))

# 조건문
age = int(input("나이를 입력하세요: "))
if age>10:
    print("청소년이야!") # 들여 쓰기를 해야 함 ㅋㅋ
elif age>5: # else if 의 줄임말, 그 외의 경우 else if 를 elif라 함 ㅋㅋ
    print("그렇지 않아!")
else:
    print("완전 유아야")