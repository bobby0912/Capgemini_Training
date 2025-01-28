def max_min_arr(arr):
    maximum_num=minimum_num=arr[0]
    for i in arr:
        if(maximum_num<i):
            maximum_num=i
        if(minimum_num>i):
            minimum_num=i
    return maximum_num,minimum_num

def main():
    arr=[int(input(f"Enter numbers {i+1}: ")) for i in range(5)]
    print("maximum and minimum in arr are: ",max_min_arr(arr))
    # print("minimum in arr: ",min_arr(arr))

if __name__=="__main__":
    main()