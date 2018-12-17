import re
#EXERCISE 1
print(5/3) #five divided by 3
#this statement takes two ints and does math on them and then returns a double value with decimals
print(5%3) #five mod three returns the remainder
# this statement takes two ints and outputs the remainder of the division
print(5.0/3) #five divided by 3
# takes a double and an int and returns a double
print(5/3.0) #five divided by 3
# takes a double and an int and returns a double
print(5.2%3) #five divided by 3
# takes a double and an int and returns a double

#EXERCISE 2
# print(2000.3**200)#2000.3 to the 200th power
#this takes a double and an int but cannot return anything because it is too big
print(1.0+1.0-1.0)#1+1-1
#takes three doubles and returns a double
print(1.0 + 1.0e20 - 1.0e20)#when you add 1 to a very large number it goes out of the range
#so therefore the result is 0

#EXERCISE 3
x = float(123)
print(x)
x = float('123')
print(x)
x = float('123.23')
print(x)
x = int(123.23)
print(x)
#x = int('123.23') #gets an error cannot convert that much all at once
#print(x)
x = int(float('123.23')) #does not get an error
print(x)
x = str(12)
print(x)
x = str(12.2)
print(x)
#for bool anything that is empty or null or nothing or 0 is False
#otherwise it is true
x = bool('a') #true
print(x)
x = bool(0) #false
print(x)
x = bool(0.1) #true
print(x)

#EXERCISE 4
print(range(5))#the range is from 0 to five
print(type(range(5)))#this is its own type called range

#EXERCISE 5
countFound = 0
x = 11
while countFound < 20:
    if x % 5 is 0 or x%7 is 0 or x%11 is 0:
        print(x)
        countFound+=1
    x+=1

#EXERCISE 6
def is_prime(n):
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
            break
    return True

print(is_prime(13))
print(is_prime(10))

def is_prime_better(n):
    if n is 2 or n is 3:
        return True
    elif (n-1)%6 is 0 or (n+1)%6 is 0:
        if(is_prime(n)):
            return True
        else:
            return False
    else:
        return False

print(is_prime_better(13))
print(is_prime_better(10))
print(is_prime_better(25))

def get_primes(n):
    l=[]
    for x in range(n):
        if(is_prime_better(x)):
            l.append(x)
    return l

print(get_primes(100))

def get_n_primes(n):

    if n <= 0:
        return []
    elif n is 1:
        return [2]
    elif n is 2:
        return [2,3]
    else:
        x=2
        l = [2,3]
        num = 5
        while x < n:
            if(is_prime_better(num)):
                l.append(num)
                x+=1
            num += 2
    return l

print(get_n_primes(10))

#EXERCISE 7
def print_list(l):
    str = ""
    for each in l:
        str = str + "%d, " % each
    print(str)

print_list([2,4,1,3,2])

def print_list_reverse(l):
    str = ""
    for each in l[::-1]:
        str = str + "%d, " % each
    print(str)

print_list_reverse([2,4,1,3,2])

def len(l):
    count = 0;
    for each in l:
        count += 1;
    return count;

print(len([1,4,3,2]))

#EXERCISE 8
a = [3,2,5,4,8,7,1]
b=a

b[0] = 10
print(a[0])
#when I changed b[0], a[0] was also updated

c = a[:]
c[2] = 10
print_list(a)
#when I changed c, a was not updated

def set_first_elem_to_zero(l):
    l[0] = 0
    return l

set_first_elem_to_zero(a)
print_list(a)

#EXERCISE 9
def concat(A):
    l = []
    for each in A:
        l += each
    return l

print(concat([[1,2,3],[3,2,1],[2]]))

#EXERCIES 10
import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return(np.sin(x-2)**2)*(np.e**(-x**2))

x = np.arange(0.0, 2.0, 0.01)
y = f(x)

plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("f(x)= sin^2(x-2) * e^-x^-2")
plt.grid(True)
plt.show()

#EXERCISE 11
def product_loop(l):
    p = 1
    for each in l:
        p *= each;
    return p

print(product_loop([1,2,3,4]))

def product_rec(l):
    if(len(l)==1):
        return l[0];
    else:
        return l[0]*product_rec(l[1:])

print(product_rec([1,2,3,4]))

#EXERCISE 12
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))

#EXERCISE 13

file  = open("emails.txt", "r")

print(re.search('[a-zA-Z]*@[a-zA-Z]*\.[a-zA-Z]*', 'asdfd@asfsd.afs'))


for line in file:
    match = re.search('[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+', line)
    print(match)
