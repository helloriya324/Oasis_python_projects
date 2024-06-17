import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
  """Generates a random password based on user-specified criteria.

  Args:
      length: Desired password length (integer).
      include_letters: True to include lowercase and uppercase letters (default: True).
      include_numbers: True to include numbers (default: True).
      include_symbols: True to include symbols (default: True).

  Returns:
      A randomly generated password (string).
  """
  characters = ""

  if include_letters:
    characters += string.ascii_letters
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  if not characters:
    raise ValueError("At least one character type must be included (letters, numbers, symbols).")

  password = "".join(random.choices(characters, k=length))
  return password

def main():
  """Prompts the user for desired password length and character set preferences.
     Generates and prints a random password based on the user's input.
  """
  try:
    length = int(input("Enter desired password length: "))
    include_letters = input("Include lowercase and uppercase letters (y/n)? ").lower() == "y"
    include_numbers = input("Include numbers (y/n)? ").lower() == "y"
    include_symbols = input("Include symbols (y/n)? ").lower() == "y"

    password = generate_password(length, include_letters, include_numbers, include_symbols)
    print(f"Your generated password: {password}")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()