#inputing List as list

import math
import random
import numpy as np
from statsmodels import robust


n=10

input_list=[random.randint(1,100) for i in range(n)]

List = []

for ele in input_list:

    List.append(int(ele))

n = len(List)

sum = 0

sum_var = 0

#!!!!!!!!!!!!!!!!!!!! mean computing !!!!!!!!!1

for ele in List:

    sum = sum + ele    

mean = sum/n

print('='*10,'MEAN value is:','='*10)
print(mean)

#1!!!!!!!!!!!!!!!!!!!!!Variance Computing

for ele in List:

     sum_var = sum_var + (ele - mean)**2

variance = sum_var/n

print('='*10,'variance is:','='*10)

print(variance)

#!!!!!!!!!!!!!!!!!!!!!1computing the standard deviation

#std_dev = (variance)**1/2
std_dev=math.sqrt(variance)

print('='*10,'standard deviation:','='*10)

print(std_dev)

#!!!!!!!!!!!!!!!!!!!!!!!!computing median

#sorting the List  to compute median

def sorted_List(List):

    for i in range(1,n):

        Key = List[i]

        j = i-1

        while j >= 0 and Key < List[j]:

            List[j+1] = List[j]

            j = j-1

            List[j+1] = Key

    return List
sorted_Listval = sorted_List(List)



def median_List(sorted_Listval):

    if n%2 == 1:

        median = sorted_Listval[n//2]

    else:

        x1,x2 = sorted_Listval[n//2],sorted_Listval[n//2 -1]

        median = (x1+x2)/2

    return median      

median_value = median_List(sorted_Listval)

print('='*10,'median','='*10)

print(median_value)


#!!!!!!!!!!!!!!!!!!!!!!!!!1calculating mean absolute deviation

absolute_list = []

for ele in sorted_Listval:

    absolute_list.append(abs(ele-median_value))



sorted_abs_value = sorted_List(absolute_list)

print('sorted_abs_value:',sorted_abs_value)

jar = median_List(sorted_abs_value)

print('='*10,'median abs deviation','='*10)

print(jar)



#!!calcultaing IQR (Inter-Quartile Range)

#Q1- 25th Quartile Range

#Q2 - 50th Quartile Range

#Q3 - 75th Quartile Range

#Q4 - 100th Quartile Range



value_Q1 = (len(sorted_Listval)-1)* 25/100.0

value_Q1 = int(value_Q1)

Q1 = sorted_Listval[value_Q1]


Q2 = median_value



value_Q3 = (len(sorted_Listval)-1)* 75/100.0

value_Q3 = int(value_Q3)

Q3 = sorted_Listval[value_Q3]



Q4 = max(sorted_Listval)


IQR = Q3 - Q1

print('='*10,'Inter-Quartile Range:','='*10)

print(IQR)



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1calculating 90th and 99th percentile

value_90 = (len(sorted_Listval)-1)* 90/100.0

value_90 = int(value_90)

percentile_90 = sorted_Listval[value_90]

print('='*10,'90th Quartile Range is:','='*10)

print(percentile_90)

value_99 = (len(sorted_Listval)-1)* 99/100.0

value_99 = int(value_99)

percentile_99 = sorted_Listval[value_99]

print('99th Quartile Range is:',percentile_99)

#!!!!!!!!!!!!!!!!!!! Metrics using Libraries!!!!!!!!!!!!!!!!

print('='*30, "Finding mean Using Library",'='*30)

print(np.mean(List))

print('='*30, "Finding Variance Using Library",'='*30)

print(np.var(List))

print('='*30, "Finding Standard Deviation Using Library",'='*30)

print(np.std(List))


print('='*30, "Finding Median Using Libaray",'='*30)

print(np.median(List))

print('='*30, "Finding 90th Percentile Using Library",'='*30)

print(np.percentile(List,90))


print('='*30, "Finding 91th Percentile Using Library",'='*30)

print(np.percentile(List,91))

print('='*30, "Inter-QuartileRange Using Library",'='*30)

print((np.percentile(List,75))-(np.percentile(List,25)))

print('='*30, "Median Absolute Deviation Using Library",'='*30)

print(robust.mad(List,c=1))

