class Solution:
    # Counter
    def majorityElementCounter(self, nums: List[int]) -> int:
        count = Counter(nums)
        return count.most_common(1)[0][0]
    # Sorting method: sort the array and return the middle element, which will be the majority element
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    # Hash Map method: create a hash map to count the occurrences of each element, then return the element with the highest count
    def majorityElementHashMap(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return max(count, key=count.get)
    
    # Boyer-Moore Voting Algorithm: this algorithm works by maintaining a count of the current candidate for majority element and updating it as we iterate through the array
    def majorityElementBoyerMoore(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

    # Divide and Conquer method: this method works by dividing the array into two halves, finding the majority element in each half, and then combining the results to find the overall majority element
    def majorityElementDivideAndConquer(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        left_majority = self.majorityElementDivideAndConquer(nums[:mid])
        right_majority = self.majorityElementDivideAndConquer(nums[mid:])
        if left_majority == right_majority:
            return left_majority
        left_count = nums.count(left_majority)
        right_count = nums.count(right_majority)
        return left_majority if left_count > right_count else right_majority

        # Boyer-Moore Voting Algorithm is the most efficient method with O(n) time complexity and O(1) space complexity, while the other methods have higher time and space complexities.
        # Sorting method has O(n log n) time complexity and O(1) space complexity, Hash Map method has O(n) time complexity and O(n) space complexity, and Divide and Conquer method has O(n log n) time complexity and O(log n) space complexity.
        # In practice, the Boyer-Moore Voting Algorithm is often the preferred method for finding the majority element due to its efficiency and simplicity.

        
