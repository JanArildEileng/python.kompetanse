

def main():
    print("Hello Python")
    s=input("String=")
    print("s=",s)
    x=int(input("x="))
    print(f"x={x} x*x={sqr(x)}")

def sqr(x):
    return x*x


main()