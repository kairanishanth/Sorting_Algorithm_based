#insortion sort: here we take sorted and unsorted arr & comparing the sorted and unsorted 
def insortiosort(arr,n):
    for i in range(n):
        j=i 
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr 
arr=[5,1,2,3,6,4,79,8]
n=len(arr)
print(insortiosort(arr,n))

