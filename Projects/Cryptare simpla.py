alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = int(input('Enter the number for encryption:'))

character = input('Please enter a character:')

position = alphabet.find(character)

newPosition = (position + key) % 26

newCaracther = alphabet[newPosition]
print('The new character is ',newCaracther)