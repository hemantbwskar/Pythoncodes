a=[5,6,3,1,3,56,45,1345,1,346,6,5,546,5,345,3,7,9,6]

def sort(arr):
    def is_sorted(arr):
        for i in range(1, len(arr)):
            j = i - 1
            if arr[j] > arr[i]:
                return False

    while is_sorted(arr) == False:
        for i in range(1, len(arr)):

            j=i-1
            if arr[j]>arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp

sort(a)
print(a)