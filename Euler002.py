
def main():
    test(4000000)
   

def FibonacciEven(n):
    n1=0
    n2=1
    sumEven=0

    while n2 < n:
        (n1,n2)=(n2,n1+n2)
      
        if n2 % 2 ==0:
            sumEven+=n2
    return sumEven

def test(n):
    print(f" Sum of {n} is  {FibonacciEven(n)}")

main()