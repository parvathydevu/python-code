def largest_prime_factor(n):
    max_prime=-1
    while n%2==0:
        max_prime=2
        n//2
    for i in range(3,int(n**0.5)+1.2):
        while n%i==0:
            max_prime=i
            n//2
    if n>2:
        max_prime=n
    return max_prime
def solve(L,R,P):
    count=0
    for num in range(L,R+1):
        if largest_prime_factor(num)<=P:
            count+=1
    return count

#input
T=int(input())
results=[]
for _ in range(T):
    L,R,P=map(int,input().split())
    results.append(solve(L,R,P))
#output
for result in results:
    print(result)