def merge_sort(Arr,start,end):
    if(start<end):
        mid = (start+end)//2
        merge_sort(Arr,start,mid)
        merge_sort(Arr,mid+1,end)
        merge(Arr,start, mid, end)

def merge(Arr, start, mid, end):
  #temp arrays to copy the elements of subarr
  leftArr_size = (mid-start)+1
  rightArr_size = (end-mid)
  leftArr = [0]*leftArr_size
  rightArray = [0]*rightArr_size
  for i in range(0, leftArr_size):
    leftArr[i] = Arr[start+i]
  for i in range(0, rightArr_size):
    rightArray[i] = Arr[mid+1+i]
  i=0
  j=0
  k=start
  while (i < leftArr_size and j < rightArr_size):
    if (leftArr[i] < rightArray[j]):
      #filling the orig arr with the smaller ele
      Arr[k] = leftArr[i]
      i = i+1
    else:
      #filling the orig arr with the smaller ele
      Arr[k] = rightArray[j]
      j = j+1
    k = k+1
  # copying remaining elements if any
  while (i<leftArr_size):
    Arr[k] = leftArr[i]
    k = k+1
    i = i+1
  while (j<rightArr_size):
    Arr[k] = rightArray[j]
    k = k+1
    j = j+1
if __name__ == '__main__':
  Arr = [2,14,1,9,10,5,6,18,11]
  merge_sort(Arr, 0, 8)
  print(Arr)
