# Binary Search is a searching technique.
# Developing Binary Search Iterative Function.
def binarySearch(arra, low, high, x):
    while low <= high: # Iterative Condition
        mid = low + (high - low) // 2 # mid value calculation

        if arra[mid] == x:
            return mid # data is perfectly in the middle.
        elif arra[mid] < x:
            low = mid + 1 # data is at right side.
        else:
            high = mid - 1 # data is at left side.
    
    return -1


arra = [23, 45, 67, 77, 89, 91, 96, 98]
x = 91
result = binarySearch(arra, 0, len(arra)-1, x)

# Result Analysis
if result != -1:
    print("Data Found")
    print("Location: ", result+1)
else:
    print("Not Found")