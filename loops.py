numbers=list(range(1,51))
print(numbers)

#number 3
values=list(range(10,41))
sum_of_values=sum(values)
print(sum_of_values)
average_of_values=sum_of_values/len(values)
print(average_of_values)

#number 4
#number 5
#number 6
even_numbers= 0
for i in range(1,51):
    if i % 2==0:
        even_numbers+=1
print(even_numbers) 

#number 7
ls1=[("Jay",20),("Mo", 30),("Mya", 32)]
total_quantity=sum(quantity for name,quantity in ls1 )
print(total_quantity)

    
