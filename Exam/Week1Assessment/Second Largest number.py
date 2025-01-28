def findSecondLargest(arr):
    # arr.sort(reverse=True)
    # return arr[1]
    max1=max2=-1e9+7
    for i in arr:
        if(max1<i):
            max2=max1
            max1=i
        # we are checking i!=max1 because if the element is same as max1 then we dont want to update max2
        # arr: 3 2 3 2 
        # max1=3 max2=2
        if(max2<i and i!=max1):
            max2=i
            
    return max2

def main():
    try:
        print("Enter List of numbers: ")
        arr=list(map(int,input().split()))
        print(f"Second largest element in the list is :{findSecondLargest(arr)}")

    except ValueError as e:
        print(f"Invalid Input {e}")
        return

if __name__ == "__main__":
    main()







