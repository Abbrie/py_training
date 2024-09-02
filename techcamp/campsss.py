#task 15
basic_salary=int(input("Enter basic salary; "))
benefits=int(input("Enter benefits; "))
def gross_salary(a,b):
    gross=a+b
    return gross

grosss=gross_salary(basic_salary,benefits)
print(grosss)
def nhif(grosss):
    
        if grosss <= 5999:
            nhif=150
        elif grosss >=6000 and  grosss <=7999:
            nhif=300
        elif grosss>=8000 and grosss<=11999:
            nhif=400
        elif grosss>=12000 and grosss<=14999:
            nhif=500
        elif grosss>=15000 and grosss<=19999:
            nhif=600
        elif grosss>=20000 and grosss<=24999:
            nhif=750
        elif grosss>=25000 and grosss<=29000:
            nhif=850
        elif grosss>=30000 and grosss<=34999:
            nhif=900
        elif grosss>=35000 and grosss<=39999:
            nhif=950
        elif grosss>=40000 and grosss<=44999:
            nhif=1000
        elif grosss>=45000 and grosss<=49999:
            nhif=1100
        elif grosss>=50000 and grosss<= 59999:
            nhif=1200
        elif grosss>=60000 and grosss<= 69999:
            nhif=1300
        elif grosss>=70000 and grosss <= 79999:
            nhif=1400
        elif grosss>= 80000 and grosss<= 89999:
            nhif=1500
        elif grosss>= 90000 and grosss<= 99999:
            nhif=1600
        else:
            nhif=1700
        return nhif
        


total_nhif=nhif(grosss)
print(total_nhif)

#task 16
def nssf(grosss):
        
        if grosss  >=18000:
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
    
        if total_tax_income>=24000:
            tax=0.1* total_tax_income
        elif total_tax_income>24000 and total_tax_income<=32333:
            tax=0.25* total_tax_income
        elif total_tax_income>32333 and total_tax_income<=500000:
            tax=0.3* total_tax_income
        elif total_tax_income>500000 and total_tax_income<=800000:
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




