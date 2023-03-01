#quick sort O(nlogn),O(1)
def partition(array, low, high):
    pivot = array[high] #last as pivot 
    i = low - 1         #pointer
    for j in range(low, high):
	    if array[j] <= pivot:
	        i = i + 1   #incementing the pointer
	        (array[i], array[j]) = (array[j], array[i])  #swapping the pointer(i) and curr ele(j)
    (array[i + 1], array[high]) = (array[high], array[i + 1])   #swaping 
    return i + 1
def quick_sort(array, low, high):
    if low < high:
	    pi = partition(array, low, high)
	    quick_sort(array, low, pi - 1)
	    quick_sort(array, pi + 1, high)
array = [ 10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(array)