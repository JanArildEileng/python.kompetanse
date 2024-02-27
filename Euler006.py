def main():
    test(10)
    test(100)

def SumSquareDifference(size):
    
    squireSum=0
    sum=0
    for i in range(1,size+1):
        squireSum=squireSum+i*i
        sum+=i
   
    diff=sum*sum-squireSum
    return diff



def test(n):
    print(f" Sum Square Difference of {n} is  {SumSquareDifference(n)}")

main()
