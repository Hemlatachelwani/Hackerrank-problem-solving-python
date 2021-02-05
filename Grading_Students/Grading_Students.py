Question:
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
Examples

 round to  (85 - 84 is less than 3)
 do not round (result is less than 40)
 do not round (60 - 57 is 3 or higher)
Given the initial value of  for each of Sam's  students, write code to automate the rounding process

Solution:


#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Write your code here
  for i in range(0,len(grades)):
    # print(grades[i]) 
    g=grades[i] 
    if grades[i]>=38:
      if (grades[i]+1)%5==0:
        grades[i]+=1
      elif (grades[i]+2)%5==0:
        grades[i]+=2
    else:
      pass

  return(grades)    
      
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
        
    # print(grades)
    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
