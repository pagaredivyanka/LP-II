def selection_sort(arr):
 s
   n = len(arr)

   
    for i in range(n):

        # Initially assume the ith element is the smallest

        min_index = i


        # Find element smaller than current minimum 

        for j in range(i+1, n):
 
           if arr[j] < arr[min_index]:

                min_index = j
     
   
        # Swap the smallest element to current i index
 
       arr[i], arr[min_index] = arr[min_index], arr[i]


    return arr


arr = [20,12,50,45,10]


sorted_arr = selection_sort(arr)

print(sorted_arr)
