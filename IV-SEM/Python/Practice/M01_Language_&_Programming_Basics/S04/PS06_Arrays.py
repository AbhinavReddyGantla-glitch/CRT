'''
Docstring for IV-SEM.Python.Practice.M01_Language_&_Programming_Basics.S04.PS06_Arrays
Arrays:
1.List 
'''
'''
list = [1,12.5,True,1,"Python",2+5j]
print(list,type(list))
print(len(list))
list[2] = False
print(list)
list.append(100)
print(list)
list.insert(1,100)
print(list)
list.insert(20,200)
print(list)
list.insert(-20,300)
print(list)
list.extend([300,400,500])
print(list)
list.pop()
print(list)
list.pop(1)
print(list)
#list.pop(20)
#print(list)
list.remove(100)
print(list)
list.clear()
print (list)
l1 = [1,2,3]
l2 = l1
l3 = l1.copy()
print(l1,l2,l3)
l1.append(4)
print(l1,l2,l3)
'''
from array import array
arr = array('i',[10,20,30])
print(arr,type(arr))
arr.append(12)