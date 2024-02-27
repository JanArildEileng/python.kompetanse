

for i in [0,1,2]:
    if ( i % 2):
        print(f"Even: {i}")
    else:
        print(f"Odd: {i}")
        


for i in range(3):
    print(f"{i}")

for i in range(3):
    match(i) :
        case 1:
            print(f"1={i}")
        case 2:
            print(f"2={i}")
        


i =0

while(i<3):
    print(f"{i}")
    i+=1   
