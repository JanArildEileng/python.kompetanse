def main():
    test(10)
    test(20)

def SmallestMultiple(size):
    t=1
    multi=False

    while  multi==False:
       
       multi=True
       for i in range(1,size+1):
            if   t % i !=0:
                multi=False
                t+=1
                break

    return t



def test(n):
    print(f" Smallest Multiple of {n} is  {SmallestMultiple(n)}")

main()