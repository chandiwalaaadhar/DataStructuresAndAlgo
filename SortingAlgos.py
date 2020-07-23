def insertionSort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j-=1
    return arr
