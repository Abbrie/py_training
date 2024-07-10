# year=(input("Enter year: "))
#if len(year)==4:
    # if int(year) % 4==0:
    #    if int(year) % 100==0:
            # print(f"{year} is a leap year")
# else:

    # print("invalid")

speed=int(input("Enter speed; "))
if speed<70:
    print("ok")
else:
    demerit_points=(speed- 70) / 5
    if demerit_points>12:
        print(demerit_points)
        print("License suspended")
        
    else:
        print(demerit_points)   




