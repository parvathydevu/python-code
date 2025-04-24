def largest_prime_factor(n):
    max_prime = -1
    # Divide n by 2 to remove all even factors
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    # Check for odd factors from 3 onwards
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    # If n is still greater than 2, then n itself is a prime factor
    if n > 2:
        max_prime = n
    return max_prime

def solve(L, R, P):
    count = 0
    for num in range(L, R + 1):
        if largest_prime_factor(num) <= P:
            count += 1
    return count

# Input
T = int(input())
results = []
for _ in range(T):
    L, R, P = map(int, input().split())
    results.append(solve(L, R, P))

# Output
for result in results:
    print(result)