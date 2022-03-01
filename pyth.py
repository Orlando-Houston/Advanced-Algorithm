
#import the libraries
import numpy as py
import matplotlib.pyplot as plt
import pandas as pd



#Constant Complexity (O(C))
def constant_algo(items):
    result = items[0] * items[0]
    print ()

constant_algo([4, 5, 6, 8])


x = [2, 4, 6, 8, 10, 12]
y = [2, 2, 2, 2, 2, 2]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Constant Complexity')
plt.show()



#Linear Complexity (O(n))
def linear_algo(items):
    for item in items:
        print(item)

linear_algo([4, 5, 6, 8])

x = [2, 4, 6, 8, 10, 12]

y = [2, 4, 6, 8, 10, 12]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Linear Complexity')
plt.show()


#Quadratic Complexity (O(n^2))
def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ' ,item)

quadratic_algo([4, 5, 6, 8])

x = [2, 4, 6, 8, 10, 12]

y = [4, 16, 36, 64, 100, 144]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Quadratic Complexity')
plt.show()


#Logarithmic Time — O(log n)
def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')
    
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(data, 8))



x = [10, 100, 1000, 10000, 100000, 1000000]
y = [2, 4, 6, 8, 10, 12]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Logarithmic Time')
plt.show()



#Quasilinear Time — O(n log n)
def merge_sort(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    merge_sort(left_data)
    merge_sort(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
    
if __name__ == '__main__':
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    merge_sort(data)
    print(data)

x = [20, 200, 2000, 20000, 200000, 2000000]
y = [2, 4, 6, 8, 10, 12]



plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Quasilinear Time')
plt.show()

#Quadratic Time — O(n²)
def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
    
if __name__ == '__main__':
    data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
    bubble_sort(data)
    print(data)

x = [2, 4, 6, 8, 10, 12]

y = [20, 40, 60, 80, 100, 120]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Quadratic Time')
plt.show()


#Factorial — O(n!)
def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
    
if __name__ == '__main__':
    data = [1, 2, 3]
    heap_permutation(data, len(data))
    
x = [5, 10, 15, 20, 25, 30]

y = [2, 24, 720, 40320, 3628800, 479001600]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Factorial')
plt.show()

#Exponential Time — O(2^n)
def fibonacci(num):
    if (num <= 1):
       return num
    return  fibonacci(num - 2) + fibonacci(num - 1)

fibonacci(10)

x = [5, 10, 15, 20, 25, 30]

y = [5, 55, 610, 6765, 75025, 832040]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Exponential Time')
plt.show()