def buble_sort(arr):
    isSorted = False
    while(not isSorted):
        for i in range(len(arr)-1):
            isSorted = True
            if arr[i] >= arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = False
    return arr


def main():
    arr = list()
    string = input("Enter a list of number separate by comma: ")
    arr = string.split(', ')

    print(buble_sort(arr))


main()
