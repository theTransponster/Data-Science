#This is a very basic code that computes quartiles (Q1, Q2, Q3) from a vector of numbers without using Scipy, numpy or other libraries
#The objective is to understand the concept of quartiles from scratch
#The program reads from the console and prints in it (STDIN, STDOUT) 


#Begin the implementation of functions

#Function1 to find the lower half
def lower_half(numbers): 
  low=[]
  if n%2 == 0:
    low.append(numbers[0:int(n/2)])
  else:
    low.append(numbers[0:int(n/2)])
 return low
#End of Function1

#Function2 to find the upper half
def upper_half(numbers):
  up=[]
  if n%2 == 0:
    up.append(numbers[int(n/2):n])
  else:
    up.append(numbers[int(n/2)+1:n])
 return up
#End of function2

#Function3: to calculate the median
def median(lista):
  median1 = 0
  n1 = 0
  n2 = 0
  nn = len(lista)
  if nn%2 == 0:
    n1 = lista[int(nn/2)-1]
    n2 = lista[int(nn/2)]
    median1 = int((n1 + n2)/2)
  else: 
    n1 = lista[int(nn/2)]
    median1 = n1
  return median1  
#End of Function3 

def main():
  n = int(input('Enter the number of elements on the array: ')) #this input can be optional
  numbers = list(map(int, input('Enter the array of numbers in a single line separated by spaces: ').split(' '))) 

  numbers = sorted(numbers) #arrange the numbers from min to max
  
  L = lower_half(numbers)
  U = upper_half(numbers)

  Q1 = median(L[0])
  Q2 = median(numbers)
  Q3 = median(U[0])


  print(Q1)
  print(Q2)
  print(Q3)
 
if __name__=='__main__':
  main()


#End of code 


