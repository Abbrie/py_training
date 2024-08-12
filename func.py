#question 2
numbers=list(range(1,51))
def divisible_by_5_or_7(list):
    for i in list:
        if i%7==0 and i%5==0:
            return i
            
        
div_num=divisible_by_5_or_7(numbers)
print(div_num)


#question 3
number=list(range(10,41))
def total(number):
    total=0
    for i in number:
        total+=number(i)
        return total
    
       

def average(total_sum):
    average=total_sum/len(number)
    return average

ttl_sum=total(number)
print(ttl_sum)
avg=average(ttl_sum)
print(avg)





#number 4
num=list(range(10,51))
odd_numbers=[]
def first_odd_numbers(num):
    for i in num:
        if i%2 !=0:
          odd_numbers.append(i)
    return odd_numbers

odd=first_odd_numbers(num)
print(odd[:10])


#number 5
numm=int(input("Enter number:"))
def multiplication_table(num):
    for i in range(1,11):
        product=num *i
        print(table(f"{num} x {i}={product}"))

        return product
    
table=multiplication_table(num)
print(table)


    
    











    
    
    



