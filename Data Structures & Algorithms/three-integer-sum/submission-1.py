class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        fixed = set()
        output = []
        nums = sorted(nums)

        for i, num in enumerate(nums[:-2]):
            if num in fixed:
                continue

            fixed.add(num)

            j = i + 1
            k = len(nums) - 1

            for l in range(i, len(nums)):
                if j >= k:
                    break

                if num + nums[j] + nums[k] == 0:
                    if [num, nums[j], nums[k]] not in output:
                        output.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1

                elif num + nums[j] + nums[k] > 0:
                    k -= 1

                else:
                    j += 1

        return output