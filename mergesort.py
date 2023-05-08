def merge_sort(arr):
    merge_sort2(arr,0,len(arr)-1)
def merge_sort2(A,first,last):
    if first<last:
        mid=(first+last)/2
        merge_sort2(A,first,mid)
        merge_sort2(A,mid+1,last)
        merge(A,first,mid,last)
def merge(A,first,middle,last):
    L=A[first:middle]
    R=A[middle+1:last+1]
    i=0;j=0;k=0
    for k in range(first,last+1):
        if L[i]<=R[i]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
arr_test=[99,88,77,66,55,44,33,22,11]
print(merge_sort(arr_test))