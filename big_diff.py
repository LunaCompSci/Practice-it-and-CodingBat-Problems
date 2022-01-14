def big_diff(nums):
  numMax = nums[0]
  numMin = nums[0]

  for oneNum in nums:
    if oneNum > numMax:
      numMax = oneNum
    if oneNum < numMin:
      numMin = oneNum

  result = numMax - numMin
  return result