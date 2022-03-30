'''
@Author: Nikita
@Date: 2022-03-30 20: 25: 00
@Last Modified by: Nikita
@Last Modified time: 2022-03-30 : 20: 25:00
@Title: Calculating Employee Wage for a Month
'''

import random
Rate_Per_Hour=20
Max_Working_Days=20
Total_Emp_Hours=0
Total_Working_Days=0
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

while(Total_Working_Days<Max_Working_Days):
    Total_Working_Days+=1
    check=random.randint(0,2)
    working_hours=workingHr(check)
    Total_Emp_Hours=Total_Emp_Hours+working_hours

employee_salary=(Rate_Per_Hour*Total_Emp_Hours)
print("Employee's Monthly Wage is:",employee_salary)
 