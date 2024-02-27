
def main():
    x=getInt("X")
    print(f"{x}")
    y=getInt("Y")
    print(f"{y}")
    print(f"Sum={x+y}")
    



def getInt(v):
    while True:
        try:
            return int(input(f"{v}="))
        except ValueError :
            print("ValueError")


main()