#fibonacci series- start with 0 and 1, each succeeding number is sum of two preceding number
num = int(input("enter a number "))
first_num = 0 #1
second_num = 1 #2
sum = first_num + second_num
list = [first_num,second_num,sum]
for i in range(1,num +1):
    first_num = second_num
    second_num = sum
    sum = first_num + second_num
    list.append(sum)