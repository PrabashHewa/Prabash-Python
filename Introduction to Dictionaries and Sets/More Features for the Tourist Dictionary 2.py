"""
This program is a tourist dictionary that allows users to add,
remove, print, and translate words between English and Spanish.

Author:Prabash
"""




def print_dictionary(dictionary):
    ''' Prints the English-Spanish dictionary sorted by the English words.
    Creates a new dictionary  where the keys are the Spanish words and the 
    values are the English words.
    '''
    print("\nEnglish-Spanish")
    for english, spanish in sorted(dictionary.items()):
        print(f"{english} {spanish}")
    print()
    
    spanish_english = {spanish: english for english, spanish in dictionary.items()}
    
    print("Spanish-English")
    for spanish, english in sorted(spanish_english.items()):
        print(f"{spanish} {english}")
    print()

def main():
    dictionary = {
        "hey": "hola",
        "home": "casa",
        "thanks": "gracias"
    }

    # Initial print of dictionary contents
    print("Dictionary contents:")
    print(", ".join(sorted(dictionary.keys())))
    
    while True:
        action = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ").strip().upper()

        if action == 'A':
            english_word = input("Give the word to be added in English: ").strip()
            spanish_word = input("Give the word to be added in Spanish: ").strip()
            dictionary[english_word] = spanish_word
            print("Dictionary contents:")
            print(", ".join(sorted(dictionary.keys())))
        elif action == 'R':
            english_word = input("Give the word to be removed in English: ").strip()
            dictionary.pop(english_word, None)
            print("Dictionary contents:")
            print(", ".join(sorted(dictionary.keys())))
        elif action == 'P':
            print_dictionary(dictionary)
        elif action == 'T':
            english_word = input("Give the word to be translated in English: ").strip()
            translation = dictionary.get(english_word)
            if translation:
                print(f"The Spanish word for '{english_word}' is '{translation}'.")
            else:
                print(f"The word '{english_word}' is not in the dictionary.")
        elif action == 'Q':
            print("Adios!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
