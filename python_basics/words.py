import scrabble

# Print all words containing 'uu'.
print("----- all words with uu -----start-")
for word in scrabble.wordlist:
    if "uu" in word:
        print(word)
print("----- all words with uu -----end-")

# Print all words containing 'uu'.
print("----- all words with yy -----start-")
for word in scrabble.wordlist:
    if "yy" in word:
        print(word)
print("----- all words with yy -----end-")

print("----- all words with a and y-----start-")
for word in scrabble.wordlist:
    if "a" in word and "y" in word:
        print(word)
print("----- all words with a and y-----end-")

print("----- all words that have double letters-----start-")
letters = "abcdefghijklmnopqrsxyz"

def has_a_double(letter):
    for word in scrabble.wordlist:
        if letter + letter in word:
            return True
    return False

for letter in letters:
    if not has_a_double(letter):
        print("letter '"+letter+"' never appears doubled.")

print("----- all words that have double letters-----end-")

print("----- all words that contain all vowels-----start-")
vowels = "aeiou"

def has_all_vowels(word):
    for vowel in vowels:
        if not vowel in word:
            return False
    return True

words_with_all_vowels = []

for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)
        words_with_all_vowels.append(word)
    
print("There were "+str(len(words_with_all_vowels))+" words found in "+str(len(scrabble.wordlist))+".")
print("----- all words that contain all vowels-----end-")