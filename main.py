import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  result_text = ''

  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == 'encode':
        new_position = (position + shift) % 26
      elif direction == 'decode':
        new_position = (position - shift) % 26
      result_text += alphabet[new_position]
    else:
      result_text += letter

  print(f"The {direction}d text is {result_text}")

should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)
  
  continue_result = input("Do you want to continue? yes or no?").lower()
  if continue_result == 'no':
    should_end == True
    print("Goodbye")