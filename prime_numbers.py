#Prime Numbers in a Range (2 to N)
#Print all primes using nested loops.
n = int(input())
prime_list = []
for i in range(2,n+1):
    if i in (2,3,5,7):
        prime_list.append(i)
    else:
        is_prime = True
        for j in range(2,8):
            if i% j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
print(prime_list)