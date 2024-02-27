import math

def main():
    test(6857*3*5)
    test(218458081)
    test(600851475143)
   

def Reduce(p,n):
    while ( p % n==0):
        p/=n
    return int(p)


def LargestPrime(p):
    p=Reduce(p,2)
    t=3;
    while t <=math.sqrt(p):
        p= Reduce(p,t)
        t+=2
    return p;    

def test(n):
    print(f" LargestPrime of {n} is  {LargestPrime(n)}")

main()