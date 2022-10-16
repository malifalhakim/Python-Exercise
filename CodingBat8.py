'''xyz there'''

def xyz_there(str):
  
  new_str = str.replace('.xyz','')

  print(new_str)
  count = 0
  if 'xyz' in new_str:
    count += 1
  else :
    count += 0
  
  if count >= 1 :
    return True
  else :
    return False

print(xyz_there('1.xyz.xyz2.xyz'))