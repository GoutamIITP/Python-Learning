# 1. Positive Numbers Only: Use a sliding Window (two Pointer) Approach
# Time Complexity: O(N), Space Complexity: O(1)

#2. Handling Negative Numbers Too:
# Prfix Sum + Hash Map
# Time Complexity: O(N)
# Space Complexity: O(N)

# 3.Subaaray Sum "Divisible" by K: Use Prefix Sum + Modulus + Hash Map
# Logic: If (prefixSum[i] - prefixSum[j]) % k == 0 => prefixSum[i] % k == prefixSum[j] % k
# Time Complexity: O(N)     


# SIMPLIFIED VERSION (No "T" loop, just 1 array)
def find_all_sum(nums, target):
# Dictionary to store {cumulative_sum: [list_of_indices]}
    # We initialize with {0: [-1]} to handle subarrays starting from index 0
    prefix_sum_map = {0: [-1]}
    
    current_sum = 0
    results = []
    
    for i, num in enumerate(nums):
        current_sum += num
        
        # We are looking for a previous sum such that:
        # current_sum - previous_sum = target
        needed_sum = current_sum - target
        
        # If that 'needed_sum' exists in our map, it means 
        # the subarray from that old index + 1 to current index 'i' sums to target
        if needed_sum in prefix_sum_map:
            for start_index in prefix_sum_map[needed_sum]:
                # Found a valid subarray!
                # It starts at start_index + 1 and ends at i
                subarray = nums[start_index + 1 : i + 1]
                results.append(subarray)
        
        # Add the current sum to the map for future checks
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = []
        prefix_sum_map[current_sum].append(i)
        
    return results

# Driver Code
try:
    # Read N and Target (e.g., "8 7")
    line1 = input().split()
    if not line1: exit()
    N = int(line1[0])
    Target = int(line1[1])
    
    # Read Array (e.g., "3 4 -7 1 3 3 1 -4")
    arr = list(map(int, input().split()))

    found_subarrays = find_all_sum(arr, Target)

    if not found_subarrays:
        print("No subarrays found")
    else:
        for sub in found_subarrays:
            print(*(sub))
except Exception as e:
    print("Error in input formatting. Please use spaces between numbers.")
