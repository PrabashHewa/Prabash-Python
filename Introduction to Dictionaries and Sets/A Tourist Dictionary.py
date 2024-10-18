"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():
    """ This code is translating given words to spanish. furthmore this code is allow to add or remove words from the list """
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            english_spanish[english_word] = spanish_word

        elif command == "R":
            word_to_remove = input("Give the word to be removed: ")
            if word_to_remove in english_spanish:
                del english_spanish[word_to_remove]
            else:
                print("The word", word_to_remove, "could not be found from the dictionary.")

        elif command == "P":
            for english_word in sorted(english_spanish.keys()):
                print(english_word, english_spanish[english_word])

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            translated_sentence = translate_sentence(sentence, english_spanish)
            print("The text, translated by the dictionary:")
            print(translated_sentence)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

def translate_sentence(sentence, dictionary):
    """ This code is translating given words to spanish. furthermore this code is allow to add or remove words from the list """
    words = sentence.split()
    translated_sentence = []
    for word in words:
        if word in dictionary:
            translated_sentence.append(dictionary[word])
        else:
            translated_sentence.append(word)
    return ' '.join(translated_sentence)

if __name__ == "__main__":
    main()
