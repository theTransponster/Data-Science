#Basic code to find the interquartile range in python without using libraries
#The objective of this code is to understand the concept of interquartile range from scratch 

#Interquartil: (Q3-Q1)

#Reads from STDIN, prints on STDOUT


n  =  int(input())  #number  of  elements  of  the  array
numbers  =  list(map(int,  input().split('  ')))
frequency  =  list(map(int,  input().split('  ')))

arr  =  []

for  x,y  in  zip(numbers,frequency):
        for  i  in  range(0,y):
                arr.append(x)

arr  =  sorted(arr)
#print(arr)


def  lower_half  (numbers):
        low=[]
        n=  len(numbers)
        if  n%2  ==  0:
                low.append(numbers[0:int(n/2)])
        else:
                low.append(numbers[0:int(n/2)])
        
        return  low

def  upper_half(numbers):
        up=[]
        n  =  len(numbers)
        if  n%2  ==  0:
                up.append(numbers[int(n/2):n])
        else:
                up.append(numbers[int(n/2)+1:n])

        return  up

def  median(lista):
        median1  =  0
        n1  =  0
        n2  =  0
        nn  =  len(lista)
        if  nn%2  ==  0:
                n1  =  lista[int(nn/2)-1]
                n2  =  lista[int(nn/2)]
                median1  =  ((n1  +  n2)/2)
        else:  
                n1  =  lista[int(nn/2)]
                median1  =  n1

        return  median1


L  =  lower_half(arr)
U  =  upper_half(arr)

Q1  =  median(L[0])
Q2  =  median(arr)
Q3  =  median(U[0])


#print(Q1)
#print(Q2)
#print(Q3)
print('{:.1f}'.format(Q3-Q1)) 


