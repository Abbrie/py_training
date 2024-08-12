#TASK 1
base=float(input("Enter base: "))
height=float(input("Enter height:"))
def area_of_triangle(x,y):
    area=x*y/2
    return area

full_area=area_of_triangle(base,height)
print(full_area)

#TASK 2
number=int(input("Enter number:"))
def either_odd_or_even(number):
    for i in number:
        if i %2==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd") 
    return i

num=either_odd_or_even(number) 
print(num)


#TASK 3
#phone_number=int(input("Enter phone number:"))
#def phonenumber(x):
    #if [:3] in x== +254:
       # pass
    #elif [:]
        




#TASK 4
email=input("Enter email:")
def valid_email(x):
    if "@" in x and "." in email:
        print(f"{x} is a valid email")
    else:
        print(f"{x} is an invalid email")
    return x

valid_mail=valid_email(email)
print(valid_mail)



#TASK 5
input_1=int(input("Enter number: "))
input_2=int(input("Enter number: "))
input_3=int(input("Enter number: "))
def check_largest_input(a,b,c):
    if a>=b and a>=c:
        answer=(f"{a} is the largest")
    elif b>=a and b>=c:
        answer=(f"{b} is the largest")
    else:
        answer=(f"{c} is the largest")
    return answer
largest=check_largest_input(input_1,input_2,input_3)
print(largest)


#TASK 6
correct_password="admin@123"
password=input("Enter password:")
def input_password(x):
    attempts=4
    for attempt in range(attempts):
        if password==correct_password:
            print((f"password is granted!"))
            break
        else:
            print((f"password is not granted!"))
        
        if attempt==attempts -1:
            print((f"Account is blocked!"))
    return input

password2=input_password(correct_password)
print(password2)


#TASK 7
marks=float(input("Enter marks"))
def grade_marks(x):
    if x>79:
        grade="A"
    elif x>=60 and x<=79:
        grade="B"
    elif x>=49 and x<=59:
        grade="C"
    elif x>=40 and x<49:
        grade="D"
    else:
        grade="E"
    
    return grade

graded_marks=grade_marks(marks)
print(graded_marks)


#TASK 8
speed=float(input("Enter speed: "))
def check_speed(x):
    speed_limit=70
    if x<=speed_limit:
        check="ok"
    else:
        demerit_points=(x-speed_limit)//5
        check=(f"points are: {demerit_points}")
    return check

points=check_speed(speed)
print(points)

#TASK 9
rows=int(input("Enter number of rows: "))
def star_rows(x):
    for i in range(1,x+1):
        final="*" * i
    return final

star=star_rows(rows)
print(star)
        
#TASK 10
prods=[['omo', '30kshs','300'],['milk', '50kshs', '200'],['bread', '45kshs','359'],['coffee','5kshs','79']]
def calculate_total_stock(x):
    total_stock=0
    for i in prods:
        stock=int(i[-1])
        total_stock+=stock
    return total_stock

total=calculate_total_stock(prods)
print(total)


#TASK 11






        



        


    
    



