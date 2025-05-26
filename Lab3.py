print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1



def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    n = len(arr_result)

    for s in arr:
        if type(s) is not int:
            return 2

    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING: #REQ-01
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING: #REQ-02
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = 0
    else:   #REQ-03
        arr_result = 1

    return arr_result


def main():
    # Driver code to test above
    arr = [-1, 2 , 13 , 4 , 5]
    
    result = input("Enter sorting order (0 for ascending, 1 for descending): ")
    if result == '0':   # Sort in ascending order
        if len(arr)==0 :  # REQ-04
            print(0)
        elif bubble_sort(arr, SORT_ASCENDING) == 2 : #REQ-05 
            print(2)
        else :
            result = bubble_sort(arr, SORT_ASCENDING)
            print("\nSorted array in ascending order: ")
            print(result)
    elif result == '1': # Sort in descending order
        if len(arr)==0 :    # REQ-04
            print(0)    
        elif bubble_sort(arr, SORT_ASCENDING) == 2 : #REQ-05 
            print(2)
        else :
            print("Sorted array in descending order: ")
            result = bubble_sort(arr, SORT_DESCENDING)
            print(result)
    else: 
        if len(arr)==0 :
            print(0)
        elif bubble_sort(arr, SORT_ASCENDING) == 2 : #REQ-05 
            print(2) 
        else :
            print("Invalid sorting order. Please enter 0 for ascending or 1 for descending.")
            
        

    
if __name__ == "__main__":
    main()


