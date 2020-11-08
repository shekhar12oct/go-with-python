def binarySearch(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
         mid = (first + last)//2

         if arr[mid] == ele:
             found = True

         else:
             if ele < arr[mid]:
                 last = mid -1
             else:
                 first = mid + 1

    return found

a = [4,6,7,8,4,5,6,2]

print(binarySearch(a, 4))