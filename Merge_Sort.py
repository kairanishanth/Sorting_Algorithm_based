#MERGE SORT Algorithm
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Sort the two halves
        mergeSort(left_arr)
        mergeSort(right_arr) 
        i=0
        j=0
        k=0
        while i < len(left_arr) and j< len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k+=1
            else:
                arr[k] = right_arr[j]
                j += 1
                k+=1
        while i< len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j< len(right_arr):
            arr[k] = right_arr[j]
            j+= 1
            k+= 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print() 
arr = [0,1,3,5,7,9,2,4,6,8] 
mergeSort(arr) 
print("Sorted array is: ")
printList(arr) 
        
                

        