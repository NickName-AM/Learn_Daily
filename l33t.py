# Convert Text into 1337
# The l33t_letters map is not complete, 
# try not to repeat same codes for multiple characters.

import random

# Map
l33t_letters = {
    'a': ('@','4','/-\\', '/\\', '^'),
    'b': ('8', '|3', '6', '13', ']3'),
    'c': ('(', '<', '{'),
    'd': ('|)', '[)', '])', '|>', 'c|'),
    'e': ('3', '&', '[-'),
    'f': ('|=', ']='),
    'g': ('6', '9'),
    'h': ('|-|', '#', ']-[', ')-(', '}{'),
    'i': ('!', '1'),
    'k': ('|<',),
    'l': ('|', '|_'),
    'm': ('/\\/\\', '|\\/|', '|V|','|Y|'),
    'n': ('|\\|', '/\\/', ']\\['),
    'o': ('0', '()', '[]'),
    'p': ('|*', '|"'),
    'r': ('|2', '/2', '|~', '12'),
    's': ('5', '$'),
    't': ('7', '+'),
    'u': ('|_|', '(_)', '\\_/','/_/', '\\_\\'),
    'v': ('\\/', ),
    'w': ('|/\\|', '\\/\\/', 'vv', '\\^/', '\\_|_/'),
    'x': ('><', '*'),
    'y': ('j', '`/'),
    'z': ('2', '7_')
}

# To decide whether to convert or not.
def will_randomise():
    return random.choice((True, False))

# The meat
def l33t(word):
    l33t_word = ''
    # For each letter in the word
    for letter in word:
        l_letter = letter.lower()
        # If the letter has a corresponding 1337 code
        if l_letter in l33t_letters.keys():
            # Decide whether to change it or not.
            # Not every potential character should be changed. 
            # If you are wonderting why, change the 'will_randomise()' below this to 'True'
            if will_randomise():
                # if true, convert(map) the character to its corresponding l33t code and
                # append it to the 'l33t_word' variable
                l33t_word += random.choice(l33t_letters[l_letter])
            # if false (decided not to change), append the unchanged letter
            else:
                l33t_word += l_letter
        # If the letter is not even in the map (l33t_letters),
        # Append the unchanged character
        else:
            l33t_word += l_letter
    # Return the word that has been mapped to l33t codes
    return l33t_word
