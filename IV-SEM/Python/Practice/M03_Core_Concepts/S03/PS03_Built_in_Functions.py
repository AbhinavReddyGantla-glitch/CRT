#1.Large no. using max function
arr = [1, 2, 3, 4, 5]
print(max(arr))
#2.Check Planidrome using reversed function
word = "madam"
if word == ''.join(reversed(word)):
    print("Palindrome")
else:    
    print("Not a Palindrome")
#3.Count Even no. using filter function
arr = [1, 2, 3, 4, 5, 6]
even_count = len(list(filter(lambda x: x % 2 == 0, arr)))
print(even_count)
#4.remove duplicates using set function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr = list(set(arr))
print(unique_arr)
#5.Sum of Digits using sum function
num = 12345
digit_sum = sum(int(digit) for digit in str(num))
print(digit_sum)
#6.Sort Words Alphabetically using sorted function
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words)
print(sorted_words)
#7.find Common Elements using set intersection
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
common_elements = list(set(arr1) & set(arr2))
print(common_elements)
#8.index with value(using enumerate)
arr = [10, 20, 30, 40]
for index, value in enumerate(arr):
    print(f"Index: {index}, Value: {value}")
#9.Pair Two lists(using zip)
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item1, item2 in zip(list1, list2):
    print(f"Item1: {item1}, Item2: {item2}")
#10. Find Second Largest using sorted function
arr = [10, 20, 30, 40, 50]
sorted_arr = sorted(arr, reverse=True)
second_largest = sorted_arr[1]
print(second_largest)