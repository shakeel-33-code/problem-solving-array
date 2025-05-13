def twosum(nums,target):
    num_dict = {}
    for i,num in enumerate(nums):
        diff= target - num
        if diff in num_dict:
            return [num_dict[diff],i]
        else:
            num_dict[num] = i
    return[]
if __name__ == "__main__":
    array = input("Enter a list of numbers separated by spaces: ")
    nums = list(map(int, array.split()))
    target = int(input("Enter the target number: "))
    print(twosum(nums,target))
    