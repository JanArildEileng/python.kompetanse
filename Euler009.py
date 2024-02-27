def main():
    test(1000)
  

def SpecialPythagoreanTriplet(n):
    for a in range(1,n):
        for b in range(a,int((n-a)/2)-1):
            c =n-a-b
            if (a*a+b*b)==(c*c):
                return a*b*c     






def test(n):
    print(f" Special Pythagorean Triplet {n} is  {SpecialPythagoreanTriplet(n)}")

main()