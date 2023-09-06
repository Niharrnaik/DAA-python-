def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i 
    return -1
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key=int(input("Enter the key element to be searched"))
result = linear_search(arr,key)
if result != -1:
    print("Element found at index",result)
else:
    print("Element not found in the list")
