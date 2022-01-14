def has22(nums):
  for idx in range(len(nums) - 1):
    if nums[idx] == 2 and nums[idx + 1] == 2:
      return True
  return False