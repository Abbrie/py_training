# number=int(input("Enter number; " ))
# if Number % 3 == 0:
    # print("number is divisibe by 3")
# else:
    # print("number is not divisible by 3")

# number=int(input("Enter number: "))
# if number % 2 == 0:
    # print("it is an even number")
# else:
    # print("it is an odd number")



password="warigzzz"
password2=input("Enter password: ")
if len(password2)>0:
    if password==password2:
        print("Correct!")
    else:
        print("Incorrect password")
else:
    print("Please enter your password")


temperature=int(input("Enter temp in degrees celsius; "))
#if temperature>=0 and temperature