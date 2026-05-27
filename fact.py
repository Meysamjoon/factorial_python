def fact(number):
  temp = number
  if temp == 1:
    return 1
  else:
    return number * fact(number-1)
  
print(fact(5))