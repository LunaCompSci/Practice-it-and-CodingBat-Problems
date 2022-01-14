def count_hi(str):
  hi = 0
  for i in range(len(str)-1):
    if str[i] == "h" and str[i+1] == "i":
      hi += 1
  return hi