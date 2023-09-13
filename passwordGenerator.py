import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

letters_size = len(letters) -1
numbers_size = len(numbers) -1
symbols_size = len(symbols) -1


for letter in range (0, nr_letters):
  randomLetter = random.randint(0, letters_size)
  password.append(letters[randomLetter])

for symbol in range (0, nr_symbols):
  randomSymbol = random.randint(0, symbols_size)
  password.append(symbols[randomSymbol])

for number in range (0, nr_numbers):
  randomNumber = random.randint(0, numbers_size)
  password.append(numbers[randomNumber])


password_size = len(password) -1
new_password = ""

for char in range (0, password_size):
  password_size = len(password) -1
  randomChar = random.randint(0, password_size)
  new_password += password[randomChar]
  password.pop(randomChar)


print(new_password)
