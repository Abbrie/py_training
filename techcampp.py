#task 15
basic_salary=int(input("Enter basic salary; "))
benefits=int(input("Enter benefits; "))
def gross_salary(a,b):
    gross=a+b
    return gross

grosss=gross_salary(basic_salary,benefits)
print(grosss)
def nhif(grosss):
    for i in grosss:
        if i <= 5999:
            nhif=150
        elif i >=6000 and  i <=7999:
            nhif=300
        elif i>=8000 and i<=11999:
            nhif=400
        elif i>=12000 and i<=14999:
            nhif=500
        elif i>=15000 and i<=19999:
            nhif=600
        elif i>=20000 and i<=24999:
            nhif=750
        elif i>=25000 and i<=29000:
            nhif=850
        elif i>=30000 and i<=34999:
            nhif=900
        elif i>=35000 and i<=39999:
            nhif=950
        elif i>=40000 and i<=44999:
            nhif=1000
        elif i>=45000 and i<=49999:
            nhif=1100
        elif i>=50000 and i<= 59999:
            nhif=1200
        elif i>=60000 and i<= 69999:
            nhif=1300
        elif i>=70000 and i <= 79999:
            nhif=1400
        elif i>= 80000 and i<= 89999:
            nhif=1500
        elif i>= 90000 and i<= 99999:
            nhif=1600
        else:
            nhif=1700
    return nhif
        


total_nhif=nhif(grosss)
print(total_nhif)

#task 16
def nssf(grosss):
    for i in grosss:
        if i  >=18000:
            nssff=0.6*i
        else:
            nssff="invalid"
    return nssff

nsssf=nssf(grosss)
print(nsssf)

#task 17
def nhdf():
    nhdf=grosss*0.015
    return nhdf

total_nhdf=nhdf
print(total_nhdf)

#task 18
def  total_taxable_income(a,b,c,d):
    taxable_income=a-(b+c+d)
    return taxable_income

total_tax_income=total_taxable_income(grosss,nsssf,total_nhdf,total_nhif)
print(total_tax_income)

#task 19
def total_payee(total_tax_income):
    for i in total_tax_income:
        if i>=24000:
            tax=0.1* total_tax_income
        elif i>24000 and i<=32333:
            tax=0.25* total_tax_income
        elif i>32333 and i<=500000:
            tax=0.3* total_tax_income
        elif i>500000 and i<=800000:
            tax=0.325 *total_tax_income
        else:
            tax=0.35* total_tax_income
    return tax
    
payeee=total_payee(total_tax_income)
payeeeh=payeee-2400
print(payeeeh)


#task 20
def total_salary(x,z,e,w,y):
    net_salary=x-(z+e+w,y)
    return net_salary 

total_net=total_salary(grosss,total_nhdf,nsssf,total_nhif,payeeeh)
print(total_net)




