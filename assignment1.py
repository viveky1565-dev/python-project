value = input("Enter some comma separated number :")
list=value.split(",")
tuple=tuple(list)
print("list:",list)
print("tuple",tuple)



num = [13,25,33,76,93,25,54,35,99,75,35,234,58,33]
mx=max(num)
mn=min(num)
sm=sum(num)
avg=int(sum(num)/len(num))
print("the maximum number is =", mx)
print("the minimum number is =", mn)
print("total sum number of list =", sm)
print("the mean of the list element =", avg)



    # * use choose how much elements wants to print *

num = []
size=int(input("Enter the size of the list"))
print("Enter" , size , "Element")
for i in range(size):
    ele=int(input())
    num.append(ele)
mx=max(num)
mn=min(num)
sm=sum(num)
avg=int(sum(num)/len(num))
print("the maximum number is =", mx)
print("the minimum number is =", mn)
print("total sum number of list =", sm)
print("the mean of the list element =", avg)



num = [23,24,56,3,111,73,65,98,7,76,34,2,3456,7,3]
for x in num:
    if x % 2 == 0:
        print(x)


def check_number(numbers):
    for num in numbers:
        if num % 2 ==0:
            print(num, "is Even")
        else:
            print(num, "is odd")

numbers = [23,24,56,75,9,70,53,23,14,32]
check_number(numbers)