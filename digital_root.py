#Digital Root
#Keep summing digits until a single digit remains. 
n = int(input())  
m = str(n)
sum_digits = 0

for i in range(len(m)):
    if len(m) - 1 != i:
        sum_digits += int(m[i])
print(sum_digits)