# WAP to accept basic salary from user and Give 10% of DA on basic salary 
# ,12% HRA on basic salary  to employee if the salary is more than 50000 .calculate total salary.

name=str(input("Enter a Employee name:"))
basic_salary = float(input("Enter the basic salary of employee: "))

DA = 0  
HRA = 0 

if( basic_salary > 50000):
    DA = 0.10 * basic_salary
    HRA = 0.12 * basic_salary

total_salary = basic_salary + DA + HRA

print("Employee name:",name)
print(f"Basic Salary:" ,basic_salary)
print(f"Dearness Allowance (DA):" ,DA)
print(f"House Rent Allowance (HRA):",HRA)
print("Name of Employee is",name,"Total Salary of Employee is: ",total_salary)
