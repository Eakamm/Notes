numbers = 10

while 1:
  if numbers % 2 == 0:
    continue
  print(numbers)
  numbers-=1
  if numbers < 0:
    break
