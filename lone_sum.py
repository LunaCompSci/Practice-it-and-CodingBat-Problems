def lone_sum(a, b, c):
  if a == b == c:
    result = 0
    return result
  elif a != b and a != c and b != c:
    result = (a + b + c)
    return result
  elif a == b:
    result =  c
    return result
  elif a == c:
    result = b
    return result
  elif b == c:
    result = a
    return result