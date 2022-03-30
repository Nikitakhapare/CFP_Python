'''
@Author: Nikita
@Date: 2022-03-29 20: 56: 00
@Last Modified by: Nikita
@Last Modified time: 2022-03-30 19: 57: 00
@Title: Calculating Employee Wage
'''

import random

print("Welcome to Employee Wage Computation Programs")
fullTime=1
partTime=2
wagePerHr=20
employeeWage=0
Present=1
rand=random.randint(0,1)

if rand==Present:   
    print("Employee is Present")
    empchack=random.randint(0,1)
    if empchack==fullTime:
           empHr=8
    elif empchack==partTime:
            empHr=4   
    employeeWage=empHr*wagePerHr
    print("Daily Employee Wage for Employee is ",+employeeWage)

else:
    print("Employee is Absent")
    empHr=0