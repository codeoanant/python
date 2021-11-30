def pushZeroToEnd(arr,n):
    ans = n*[0]
    i = 0
    k = 0
    while i<n:
        if arr[i] !=0:
            ans[k] = arr[i]
            i+=1
            k+=1
    else:
        i+=1
    j = 0
    while j<n and arr[j] == 0:
        ans[k] = arr[j]
        j+=1
        k+=1

    return ans
print(pushZeroToEnd([0,1,2,0,4],5))
