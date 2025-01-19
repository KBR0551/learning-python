

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
def sort_zeros_ones_tows(x): #o(n)+0(n)
     j=0 
     for i in range(len(x)): #sort o's first
        if x[i]==0:
            x[i],x[j]=x[j],x[i]
            j+=1
     for i in range(j,len(x)): # sort 1's using the end last swap of O 
          if x[i]==1:
            x[i],x[j]=x[j],x[i]
            j+=1
     return x

@timer
#Dutch National flag algorithm
@timer
def sort_zeros_ones_tows_using_three_pointers(x):  # storting is done in single iteration o(n)
    low,mid=0,0
    high=len(x)-1
    while mid<=high:
        if x[mid]==0:
            x[mid],x[low]=x[low],x[mid]
            mid+=1
            low+=1
        elif x[mid]==1:
            mid+=1
        else:
            x[mid],x[high]=x[high],x[mid]
            high-=1
    return x

print(sort_zeros_ones_tows(x))
print(sort_zeros_ones_tows_using_three_pointers(y))

x=[random.choice([0,1,2]) for _ in range(10000)]
y=x

# Execution time of sort_zeros_ones_tows: 0.0008 seconds

# Execution time of sort_zeros_ones_tows_using_three_pointers: 0.0000 seconds
