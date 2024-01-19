
first_number = int(input(''))
if first_number > 0:
  print(first_number)

number = 1234

digit1 = number % 10
number //= 10
digit2 = number % 10
number //= 10
digit3 = number % 10
number //= 10
digit4 = number % 10


print(digit4)
print(digit3)
print(digit2)
print(digit1)

