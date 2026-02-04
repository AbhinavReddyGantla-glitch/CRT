'''
#1)Print n natural numbers?
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i)

#2)Print n even numbers?
for i in range(2, n+1, 2):
    print(i)

#3)Print n odd numbers?
for i in range(1, n+1, 2):
    print(i)

#214)Print n Fibonacci numbers?
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b
#5)Print multiplication table of n?
n = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")'''
#6)Print the squares of first n natural numbers?
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i**2)