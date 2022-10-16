


def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  check_1 = a.endswith(b)
  check_2 = b.endswith(a)
  
  if check_1 or check_2 :
    return True
  else:
    return False

print(end_other( '12' , '12'))