print(">>>> PIG LATIN TRANSLATOR <<<<")

lower_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
upper_vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
ponctuation = ['.', ',', '!', '?']

AY = 'ay'
YAY = 'yay'

COMMA = ','
DOT = '.'
EXCLAMATION = '!'
INTERROGATION = '?'


def validate_captalized_letter(first_letter, given_vowel):
    if first_letter.isupper():
        return given_vowel.upper()
    else:
        return given_vowel.lower()


def validate_ending_word(word):
    if len(word) <= 1:
        return YAY
    else:
        return AY


def validate_word_ponctuation(word):
    if word.__contains__(COMMA):
        return word.replace(COMMA, "") + COMMA

    elif word.__contains__(DOT):
        return word.replace(DOT, "") + DOT

    elif word.__contains__(EXCLAMATION):
        return word.replace(EXCLAMATION, "") + EXCLAMATION

    elif word.__contains__(INTERROGATION):
        return word.replace(INTERROGATION, "") + INTERROGATION


def translate_words(words):
    print("\nINFO: WORDS TRANSLATOR STARTED \n")
    for word in words:
        if word.isnumeric():
            print(word, end=" ")
        else:
            for letter in word:
                if (letter in lower_vowels or letter in upper_vowels):
                    index = word.index(letter)
                    end_word = validate_ending_word(word)
                    first_letter = validate_captalized_letter(word[0:1], letter)
                    prefix = word[0:index].lower()
                    steam = word[index + 1:len(word)].lower()
                    final_word = first_letter + steam + prefix + end_word
                    final_word = validate_word_ponctuation(final_word)
                    words[words.index(word)] = final_word
                    print(final_word, end=" ")
                    break
    print("\n\nINFO: WORDS TRANSLATOR PROCESS FINISHED \n")


def start_translator():
    sentence = input("Enter a word or sentence to translate: ")

    if sentence.isalpha():
        print("There is no word to translate \n")
    elif sentence.isnumeric():
        print(f"We can't translate the inputed value: {sentence} because it is only numbers! \n")

    words = sentence.split()
    translate_words(words)


start_translator()

print(">>>> END <<<<")
