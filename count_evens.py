def count_evens(nums):
  total = 0
  for num in nums:
    if num % 2 == 0:
      total += 1
  return total