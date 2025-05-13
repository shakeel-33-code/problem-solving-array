#containsduplicates.py
def containsDuplicate(nums):
    seen = set()
    for num in nums:

        if num in seen:
            return True
        else:
            seen.add(num)
    return False
if __name__ == "__main__":
    array = input("Enter a list of numbers separated by spaces: ")
    nums = list(map(int, array.split()))
    print(containsDuplicate(nums))