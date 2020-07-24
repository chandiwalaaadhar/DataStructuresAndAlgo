def insertionSort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j-=1
    return arr


def mergeSort(arr):
    if (len(arr)>1):
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while (i<len(L) and j<len(R)):
            if (L[i]<R[j]):
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        
        while (i < len(L)): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while (j < len(R)): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

    return arr

def quicksort(arr, low, high):
    if low<high:
        pi=partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

def partition(arr, low, high):
    '''Helper Function for quickSort'''
    i=low-1
    pivot=arr[high]

    for j in range(low, high):
        if(arr[j]<=arr[high]):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
            