''''
1. factotial code
n=int(input("enter n))
fact=1
for i in range(1,n+1):
    fact *= i
    print(fact)
2. armstrong number
n=int(input("enter n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==n:
    print("armstrong number")
else:
     print("not armstrong number")
3.no is prime or not
n=int(input("enter n))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime number")
4.print all prime numbers in a range
lower=int(input("enter lower limit))
upper=int(input("enter upper limit))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


#5.monotonic of an array
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing
arr = [1, 2, 3, 4, 5]
print(is_monotonic(arr))

#6.reverse a number
n=int(input("enter n:"))  
sign = 1
if x < 0:
    sign = -1
    x = -x
rev = 0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print("reversed number:", rev)

#7.Roman to Integer
def roman_to_integer(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

s = input("Enter a Roman numeral: ")
result = roman_to_integer(s)
print(f"The integer value of {s} is: {result}") 
'''
##8.Happy number
n=int(input("enter n:"))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    sum_sq = 0
    while n > 0:
        digit = n % 10
        sum_sq += digit ** 2
        n //= 10
    n = sum_sq
if n == 1:
    print("Happy number")
else:   
    print("Not a happy number")

