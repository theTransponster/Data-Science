#This is a basic code to compute the standard deviation from a vector of numbers, without using libraries
#The objective of this exercise is to understand the concept of standard deviation from scratch 

#Read from STDIN, prints on STDOUT 


import  math

n  =  int(input())
numbers  =  list(map(int,  input().split('  ')))

def  average(numbers):
        sum1  =  0
        n  =  len(numbers)
        avr  =  0
        for  i  in  range(0,  len(numbers)):  
                sum1  =  sum1  +  numbers[i]  
        avr  =  sum1  /  n

        return  avr

def  dif(numbers,  average):
        dif  =  0
        dif1  =  []
        square1  =  0
        n  =  len(numbers)


        for  i  in  range  (0,  n):
                dif  =  (numbers[i]-average)
                square  =  dif**2
                dif1.append(square)
        
        return  sum(dif1)

def  s_deviation(dif,  n):
        div  =  dif  /  n
        st  =  math.sqrt(div)

        return  st

av  =  average(numbers)
dif2  =  dif(numbers,  av)
s_t  =  s_deviation(dif2,  n)

print('{:.1f}'.format(s_t))


