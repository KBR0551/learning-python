import time
import random

# Decorator to measure the execution time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate the time taken
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result  # Return the result of the function
    return wrapper

@timer
def getSecondLargest1(arr):
    if len(arr)==1:
           return -1
    arr=sorted(arr,reverse=True) #using sort method to sort from greatest to smallest
    fl=0
    sl=0#Index of first greatest element
    for i in range(1,len(arr)):
            if arr[fl]!=arr[i]:
                sl=i #index for second largets element if found break 
                break
    if sl!=0: # if the index changes then there exists second largest element if not return -1
           return arr[sl]
    else:
            return -1
@timer
def getSecondLargest2(arr):
       l=len(arr)
       if l==1:
         return -1
       max_1=arr[0]
       for i in range(1,l):   # find the first largest element
            if arr[i]>max_1:
                max_1=arr[i]
       max_2=-1              #default to -1 for second max
       for i in range(0,l):  #find the second largest element by considering the first largest element !=first
            if arr[i]>max_2 and arr[i]!=max_1:
                max_2=arr[i]
       return max_2

@timer
def getSecondLargest3(arr):
        l=len(arr)
        if l==1:
            return -1
        max_1=arr[0]
        max_2=-1
        for i in range(0,l):
            if arr[i] >max_1:
                max_2=max_1
                max_1=arr[i]
            if arr[i]>max_2 and arr[i]!=max_1:
                max_2=arr[i]
        return max_2

random_int_list = [random.randint(1, 10000000) for _ in range(10000000)]

print(getSecondLargest1(random_int_list))

print(getSecondLargest2(random_int_list))

print(getSecondLargest3(random_int_list))
