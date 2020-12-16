def sieve_erat(m):
    k = 0
    sieve = [i for i in range(n)]
    for i in range(2, n):
        if sieve[i] != 0:
            k += 1
            if k == m:
                return i
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i


def is_prime(p):
    i = 2
    while p % i != 0:
        i += 1
    return i == p


def find_prime(m):
    k = 0
    for p in range(2, n):
        if is_prime(p):
            k += 1
            if k == m:
                return p


n = 1000000

print(sieve_erat(100))
print(find_prime(100))
