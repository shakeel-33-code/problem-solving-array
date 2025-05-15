def topKFrequent(nums, k):
    # Step 1: Count the frequency of each number
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Step 2: Create buckets where index represents frequency
    # The size of the bucket array is len(nums) + 1 because the maximum frequency of any number cannot exceed len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    # Step 3: Gather the top k frequent elements from the buckets
    result = []
    for freq in range(len(buckets) - 1, 0, -1):  # Start from the highest frequency
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:  # Stop once we have k elements
                return result

# Example usage
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    k = int(input("Enter the value of k: "))
    print(topKFrequent(nums, k))