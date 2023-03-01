#bubble sort O(n^2)
def bubblesort(arr,n):
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp 
    return arr 
arr=[8,4,6,2,1,3,7,9,8]
n=len(arr)
print(bubblesort(arr,n))