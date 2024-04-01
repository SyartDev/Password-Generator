import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Willkommen beim PyPasswort-Generator!")
nr_letters = int(input("Wie viele Buchstaben möchten Sie in Ihrem Passwort?\n")) 
nr_symbols = int(input(f'Wie viele Symbole möchten Sie?\n'))
nr_numbers = int(input(f'Wie viele Zahlen möchten Sie?\n'))



passwort_liste = []
for char in range(1, nr_letters + 1):
  passwort_liste.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  passwort_liste += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  passwort_liste += random.choice(numbers)
  
random.shuffle(passwort_liste)

passwort = ""
for char in passwort_liste:
  passwort += char

print(f"Dein generiertes Passwort ist: {passwort}")
