
def main():
    test(100)
    test(1000)
    
def ReverseString(string):
   length = len(string)
   emp = ""
   for i in range(length-1,-1,-1):
       emp += string[i]
   return emp

def ReverseInt(n):
    return  int(ReverseString(str(n)))

def largestPalindrome(size):
    max=0
    for i in range(size):
        for j  in range(size):
            prod=i*j
            if str(prod)==str(ReverseInt(prod)):
                if  prod >max:
                    max=prod
    return max



def test(n):
    print(f" largestPalindrome of {n} is  {largestPalindrome(n)}")

main()

