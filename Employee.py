'''
@Author: Nikita
@Date: 2022-03-30 20: 25: 00
@Last Modified by: Nikita
@Last Modified time: 2022-03-30 : 20: 25:00
@Title: Calculating Employee Wage for a Month
'''

import random

def workingHr(check):

    """
Description:
      Function to Switch case
Parameter:
      check is to get the random number of working_hours in emply_wage_presence function
Return:
       returning the check variable
"""
    switcher={ 1: 8, 2: 4, 0: 0}
    return switcher[check]
def calculate_Hr():
    Rate_Per_Hour=20
    Max_Working_Days=20
    Max_Working_Hours_In_Month=100
    Total_Emp_Hours=0
    Total_Working_Days=0
    """
Description:
      Function to calculate Total Hr
Parameter:
      check Total Working Houur in a Month 
Return:
       returning the total Hour
"""
    while(Total_Working_Days<Max_Working_Days)and (Total_Emp_Hours<Max_Working_Hours_In_Month):
        
        Total_Working_Days+=1
        check=random.randint(0,2)
        working_hours=workingHr(check)
        Total_Emp_Hours=Total_Emp_Hours+working_hours

    employee_salary=(Rate_Per_Hour*Total_Emp_Hours)
    print("Total Working Hours is : ",Total_Emp_Hours)
    print("Employee's Monthly Wage is:",employee_salary)
    
calculate_Hr()



 