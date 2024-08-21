
secret_word = "jello"
guess = "" 
guess_count = 0
guess_limit = 3
out_of_guesses = False


# # WHILE LOOP
# # ============================================================

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True


# if out_of_guesses:
#     print("Out of Guesses, YOU LOST!")
# else:
#     print("Champ")


# FOR LOOP
# ============================================================

def translator(phrase):
    translation = ""
    vowel_map = {
        'a': 'z', 'e': 'x', 'i': 'c', 'o': 'v', 'u': 'b',
        'A': 'Z', 'E': 'X', 'I': 'C', 'O': 'V', 'U': 'B'
    }

    for letter in phrase:
        if letter in vowel_map:
            translation += vowel_map[letter]
        else:
            translation += letter

    return translation

print(translator(input("Enter word: ")))
