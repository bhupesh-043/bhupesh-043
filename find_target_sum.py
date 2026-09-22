def target_sum(arr, target):

    arr.sort()
    left = 0
    right = len(arr)-1

    while(left<right):

        #It's condition that when the target get greater than the actual target
        
        if arr[left]+arr[right] > target:
            right = right-1
        # It's condition that the target less that the actual one so that we will do push one step forward
        elif arr[left]+arr[right] < target:
            left = left+1
            
        elif arr[left]+arr[right] == target:
            print("Both the no ", arr[left], "&", arr[right])
            right = right-1
            left = left+1


arr = [1,4,1,3,6,5,4,0,3]
target = 8
target_sum(arr, target)
