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
def two_sum_index(x,k):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]+x[j]==k:
                return ([i,j])
    return ([-1,-1])

@timer
def two_sum_dict_idx(x,k):
    dict={}
    for i in range(len(x)):
        if k-x[i] not in dict:
            dict[x[i]]=i
        else:
            return ([dict[k-x[i]],i])
    print(dict)
    return ([-1,-1])

@timer
def two_sum_sort_idx(x,k):
    x.sort(reverse=True)
    i=0
    j=len(x)-1
    while i<j:
        sum=x[i]+x[j]
        if x[i]+x[j]==k:
            return([i,j])
        elif sum>k:
            i+=1
        else:
            j-=1
    return ([-1,-1])


x=[0]*10000
x[len(x)-1]=2
x[len(x)-2]=3
k=5

print(two_sum_index(x,k)) # using two for loops
print(two_sum_dict_idx(x,k)) #using hashmap 
print(two_sum_sort_idx(x,k)) #using sort and two pointer

#execution times to understand time complexity 

#Execution time of two_sum_index: 1.5926 seconds
#[9998, 9999]
#Execution time of two_sum_dict_idx: 0.0004 seconds
#[9998, 9999]
#Execution time of two_sum_sort_idx: 0.0007 seconds : if the list is already a sorted list it will still try to sort the list which will make it slower compared to other two mentods 
#[9998, 9999]


