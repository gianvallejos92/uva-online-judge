#import sys
#sys.stdin = open("D:\\Repositories\\uva-online-judge\\10324 - Zeros and Ones\\input.txt", "r")
#sys.stdout = open("D:\\Repositories\\uva-online-judge\\10324 - Zeros and Ones\\output.txt", "w")

def order_min_max(x, y):
  if x > y:
    x, y = y, x
  return [int(x), int(y)]

def validate_zeros_ones(my_str):
  if my_str.count('0') == len(my_str) or my_str.count('1') == len(my_str):
    return 'Yes'
  return 'No'

cases = 1
while True:  
  try:
    my_str = input()
  except EOFError:
    break

  n = int(input())
  
  print("Case " + str(cases) + ":")
  cases += 1
  for _ in range(n):
    x, y = input().split()[:2]
    x, y = order_min_max(x, y)    
    print(validate_zeros_ones(my_str[x:y+1]))

  

    
    
    




  