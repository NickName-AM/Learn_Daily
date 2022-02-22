import random
import os, sys
from time import sleep

hangman = [['''
  O
''',
'''
  .
  O
''',
'''
  .
  .
  O
''',
'''
  .
  .
  O
_____
''',
'''
  .
  .
  .  
_____
'''],
'''
  O
  |
''',
'''
  O
 /|
''',
r'''
  O
 /|\
''',
r'''
  O
 /|\
  |
''',
r'''
  O
 /|\
  |
 /
''',
r'''
  O
 /|\
  |
 / \
'''
]

def clear():
  if sys.platform == "win32":
    os.system("CLS")
  elif sys.platform == "linux":
    os.system("clear")

  
def to_print():
  # Print the doll to be hanged
  print(hangman[man])

  # Print the "_ _ _ ..."
  print(' '.join(letters))
  print("\nLetters typed so far: {0}".format(''.join(already_typed)))

# Index of multiple characters in a string
def indices(word, letter):
    char_list = list(word.lower())
    indexs = list()
    for i in char_list:
        if i == letter.lower():
            indexs.append(char_list.index(i))
            char_list[char_list.index(i)] = "0X"
    return indexs

def lost_animation():
  a = 0
  while a <= 4:
    clear()
    print(hangman[0][a])
    a+=1
    sleep(0.4)
  print("Correct word(s): {0}".format(random_word))
  sleep(2)
  exit()

# Main
def final(word):
    global man
    man = 6           # For 'hangman'
    while True:
        clear()

        # If all chances are lost.
        if man == 0:
          lost_animation()

        to_print()

        # Win condition
        if ''.join(letters) == word:
          print("You win!")
          sleep(2)
          exit()

        letter_input = ""
        
        # If the input has more or less than 1 characters or if the given letter has already been typed before, loop
        while (len(letter_input) != 1) or (letter_input in already_typed):
          letter_input = input("\nA letter : ").lower()
          clear()
          to_print()

        already_typed.append(letter_input)
        already_typed.append(" ")
        # There might be multiple spaces that might have same characters
        indices_ = indices(word, letter_input)

        if indices_ != []:
            # Replace the "_" with the given letter if true
            for i in indices_:
              if i == 0:
                letters[i] = letter_input.upper()
              else:
                letters[i] = letter_input
        else:
            # Chop a part of the body
            man -= 1

# Add more if you want
word_list = ["volley", "table tennis", "yeet", "heat", "beach", "watch", "sakura flower", "sakura tree", "saber", "kujou sara", "ganyu", "zhongli", "xinqiu", "morax", "azdaha", "pogchamp", "rickroll", "never gonna give you up", "never gonna let you down", "mouse", "wind", "shadow", "yanfei", "football", "tartaglia", "underworld", "truth", "word", "keyboard", "laptop", "curtain", "mecha", "shogun"]

# Choose a random word from word_list
random_word = random.choice(word_list).lower().capitalize()


# length of the random word
word_len = len(random_word)

letters = ["_"] * word_len

if " " in random_word:
  space_index = indices(random_word, " ")
  for i in space_index:
    letters[i] = " "

# To check if the input letter has been entered before
already_typed = list()

# Call the main function
final(random_word)
