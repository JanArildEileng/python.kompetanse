# https://projecteuler.net/problem=1

def main():
    test(10)
    test(1000)


def multi(n):
    sum=0
    for i in range(n):
        if i % 3 ==0 or i % 5==0:
            sum+=i
    return sum

def test(n):
    print(f" Sum of {n} is  {multi(n)}")

main()

