def main():
    test(6)
    test(10001)

def APrime(t,list):
    for i in list:
        if t % i==0 : #t not a prime
            return False
    return True

def PrimeNr(n):
    list=[2]
    t=3

    while len(list) < n:
        if APrime(t,list):
            list.append(t)
        t+=2
       
    return list[-1]


def test(n):
    print(f" Prime Nr of {n} is  {PrimeNr(n)}")

main()