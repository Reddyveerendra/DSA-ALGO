def search(arr, target) :
    # Write your code here.
    i,j = 0,len(arr)-1
    while i<=j:
        mid = (i+j)//2
        if arr[mid]==target:
            return mid
        elif arr[i]<=arr[mid]:
            if arr[i]<=target and arr[mid]>=target:
                j = mid-1
            else:
                i = mid+1
        else:
            if arr[mid]<=target and target<=arr[j]:
                i = mid+1
            else:
                j = mid-1
    return -1