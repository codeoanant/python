def mergSort(arr1,n, arr2, m):
    ans = (n+m)*[0]
    i = 0
    j = 0
    k = 0
    while i<n and j<m:
        if arr1[i] < arr2[j]:
            ans[k] = arr1[i]
            k+=1
            i+=1
        else:
            ans[k] = arr2[j]
            k+=1
            j+=1
    while i<n:
        ans[k] = arr1[i]
        k+=1
        i+=1
    while j<m:
        ans[k] = arr2[j]
        k+=1
        j+=1
    return ans
arr1 = [1,3,6,9,10,12,19]
arr2 = [2,5,7,9,11]
print(mergSort(arr1,7,arr2,5))
