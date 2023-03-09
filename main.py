def twoSum(nums:list[int],target:int) -> list[int]:
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]], i]
        dict[target - nums[i]] = i


        
