#selection sort  )(n^2)
def selectionsort(arr,n):
    for i in range(n):
        min_=i #assigning the 1st index element to the min_ variable 
        for j in range(i+1,n):
            if arr[j]<arr[min_]:
                min_=j   #assigning the min value to min_
        #swapping
        temp=arr[i]
        arr[i]=arr[min_]
        arr[min_]=temp 
    return arr 
arr=[2,5,3,4,1,6,7,9,8]
n=len(arr)
print(selectionsort(arr,n))


