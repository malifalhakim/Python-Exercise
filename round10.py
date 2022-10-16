def round10(num):
  num = round((num +1)/10) * 10
  return int(num)

def round_sum(a, b, c):
  a_after = round10(a)
  b_after = round10(b)
  c_after = round10(c)
  return a_after + b_after + c_after

print(round_sum(16,17,18))