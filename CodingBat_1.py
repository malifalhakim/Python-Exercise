def front_back(str):
  if len(str)>2:
    new_str = str[-1] + str[1 : -1 : ] + str[0]
  elif len(str) == 2 :
    new_str = str[-1]+str[0]
  else:
    pass
  
  return new_str

x = front_back("ab")
print(x)