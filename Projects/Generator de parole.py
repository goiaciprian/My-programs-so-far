import random

chars = 'abcdefghijklmnopqrstuvwxyz123456789'

lenght = input('Password lenght?')
lenght = int(lenght)

for p in range(3):
  password = ''
  for c in range(lenght):
    password += random.choice(chars)
    print(password)