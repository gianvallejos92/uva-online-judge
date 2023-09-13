#import sys
#sys.stdin = open("10324 - Zeros and Ones\input.txt", "r")
#sys.stdout = open("10324 - Zeros and Ones\output.txt", "w")

def order_min_max(x, y):
  if x > y:
    x, y = y, x
  return [int(x), int(y)]

def init_zeros_ones(my_str):
  zeros = [0] * len(my_str)
  ones = [0] * len(my_str)

  zeros[0] = 1 if my_str[0] == '0' else 0
  ones[0] = 1 if my_str[0] == '1' else 0

  for ind in range(1, len(my_str)):
    if my_str[ind] == '0':
      zeros[ind] = zeros[ind-1] + 1
      ones[ind] = ones[ind-1]
    else:
      ones[ind] = ones[ind-1] + 1
      zeros[ind] = zeros[ind-1]
  
  return [zeros, ones]

def count_zeros_ones(zeros, ones, x, y):
  cntZeros = 0
  cntOnes = 0    
  if (x > 0):
    cntZeros = zeros[y] - zeros[x-1]
    cntOnes = ones[y] - ones[x-1]
  else:
    cntZeros = zeros[y]
    cntOnes = ones[y]

  return [cntZeros, cntOnes]

cases = 1
while True:  
  try:
    my_str = input()
  except EOFError:
    break
  
  zeros, ones = init_zeros_ones(my_str)  
  n = int(input())
  
  print("Case " + str(cases) + ":")
  cases += 1
  for _ in range(n):
    x, y = input().split()[:2]
    x, y = order_min_max(x, y)    
    
    cntZeros, cntOnes = count_zeros_ones(zeros, ones, x, y)
    
    rangeLenght = (y-x) + 1
    if (cntZeros == rangeLenght and cntOnes == 0) or (cntOnes == rangeLenght and cntZeros == 0):
      print("Yes")
    else:
      print("No")
