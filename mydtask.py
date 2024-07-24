pin=8028
for attempt in range(4):
    new_pin=input("Please enter pin: ")
    if new_pin==pin:
        print("Login successful!")
        break
    else:
        print("Incorrect pin!")

        if attempt==4:
            print("Maximum attempts reached.Access denied! ")

     

    




