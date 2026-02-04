'''
Docstring for IV-SEM.Python.Practice.M02_Logic_Building_and_patterns.S02.PS05_Basic_Patterns
#Square star Pattern
n = 4
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

#Right angle triangle star pattern
n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
    
#Inverted right angle triangle star pattern
n=int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*", end="")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print()

#Number Triangle 
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
#repeated number triangle
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()

#Alphabet Triangle
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end="")
    print()

#Floyd's Triangle
n=int(input())
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print()
#Hollow Square
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''

