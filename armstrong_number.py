n = input("")
num = 0
for i in n:
    a = int(i)**int(len(n))
    num += a
if int(n) == num:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")