a = [10,20,30,40,53]
for i in range(len(a)):
    for j in range(len(a)):
        print(a[i]+a[j])
a = [10,20,30,40,53]
for num in a:
    print(num+num)
a = [10,20,30,40,53]
sum1 = 0
for i in range(len(a)):
    sum1 += a[i]
print(sum1)
a = [10,20,30,40,53]
print(sum(a)) 
a=[]
for i in range(10):
    a.append(i*i)
print(a)
a = print([i*i for i in range(10)])
#2.Find the maximum number in a list of numbers.
a = [10,20,30,40,53]
max_num = a[0]
for num in a:
    if num > max_num:
        max_num = num
print(max_num)
a = [10,20,30,40,53]