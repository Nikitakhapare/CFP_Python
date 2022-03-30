'''
@Author: Nikita
@Date: 2022-03-29 20: 56: 00
@Last Modified by: Nikita
@Last Modified time: 2022-03-30 : 03: 00
@Title: Calculating Employee Wage Using Case Statement
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
    
wage_per_hour = 20
full_time = 2
part_time = 1

check = random.randint(0,2)
empWorkingHr=workingHr(check)

totalWage=(wage_per_hour*empWorkingHr)
print("Employee Wage= ",totalWage)

 