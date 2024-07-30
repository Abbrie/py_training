

#number3
def sum_and_average(x,y):
    values=list(range(x,y+1))
    
    total_sum=sum(values)
    average=total_sum/len(values)
    return total_sum,average
#print(sum_and_average(10,41)


#number5
def multiplication_table(number):
    table=[]
    for  i in range(1,11):
        table.append(f"{number} x {i}={number * i}")
        return table
#numbers=int(input("Enter number: "))
#print(multiplication_table(numbers))

#number6
number=list(range(1,51))
def even_numbers(number):
    if number%2==0:
        print(even_numbers)
    return even_numbers



#functions question
def calculate_total(maths,eng,kisw,sci,soc):
    return maths+eng+kisw+sci+soc

def calculate_average(total):
    return total/5

def grade(average):
    if average>79:
        return "A"
    elif 60<= average< 79:
        return "B"
    elif 50<=average<60:
        return "C"
    elif 40<= average< 50:
        return "D"
    else:
        return "E"
    

def main():
    maths=int(input("Enter marks for Maths: "))
    eng=int(input("Enter marks for English:"))
    kisw=int(input("Enter marks for Kiswahili: "))
    sci=int(input("Enter marks for Science:"))
    soc=int(input("Enter marks for Social Studies:"))

    total=calculate_total(maths,eng,kisw,sci,soc)
    average=calculate_average(total)
    grades=grade(average)

    print(f"Total Marks:{total}")
    print(f"Average Marks:{average}")
    print(f"Grade: {grade}")












