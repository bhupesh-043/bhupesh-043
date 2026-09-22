def target_sum(arr, target):

    arr.sort()
    left = 0
    right = len(arr)-1

    while(left<right):

        if arr[left]+arr[right] > target:
            right = right-1
        elif arr[left]+arr[right] < target:
            left = left+1
        elif arr[left]+arr[right] == target:
            print("Both the no ", arr[left], "&", arr[right])
            right = right-1
            left = left+1


arr = [1,4,1,3,6,5,4,0,3]
target = 8
target_sum(arr, target)