def fact(number):
  temp = number
  if temp == 1:
    return 1
  else:
    return number * fact(number-1)
  
number = [i for i in range(1,11)]
for i in number:
  print(f'{i} is {fact(i):>10}')