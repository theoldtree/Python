print("abc") #주석
name = input("your name: ")
print("your name is "+name)

n = int(input("input number for sum : "))
sum = 0
for i in range(1, n+1):
    sum += i
print("result of sum is :" + str(sum))