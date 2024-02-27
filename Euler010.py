import math

def main():
    test(2000000)

def APrime(t,list):
    max=math.sqrt(t)
    for i in list:
        if i > max:
            return True   
        if t % i==0 : #t not a prime
            return False
        
    return True

def SummationofPrimes(n):
    list=[2]
    t=3

    while t < n:
        if APrime(t,list):
            list.append(t)
        t+=2
       
    sum=0
    for p in list:
        sum+=p

    print(f" Antallf Primes < {n} is  {len(list)}")
    return sum


def test(n):
    print(f" Summation of Primes {n} is  {SummationofPrimes(n)}")

main()