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

#숫자의 연산
c = 3/2 # 정수/정수의 연산 결과가 실수가 됨 ㅋㅋ
print(type(c))
print(c) # 1.5 
e = 4/2
print(type(e))
print(e)
d = 3 ** 4 # 거듭제곱의 표현
print(d) # 81
