def string_match(a, b):
  count = 0
  if len(a) > len (b):
    for i in range(len(b)):
      a = a[i : i + 2 : ]
      print(a)
      b = b[i : i + 2 : ]
      print(b)
      if a in b :
        count += 1
  else:
    for i in range(len(a)):
      a = a[i : i + 2 : ]
      print(a)
      b = b[i : i + 2 : ]
      print(b)
      if a == b :
        count += 1
      
  return count

print(string_match('xxcaazz', 'xxbaaz'))


