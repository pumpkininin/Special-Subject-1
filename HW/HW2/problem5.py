# Function conut_number_vowels take a string as an input and return number of vowels in this string
def count_number_vowels(string):
    count = 0
    vowels = 'ueoai'
    for ch in string:
        if ch in vowels:
            count += 1
    return count

# Function count_number_consonant take a string as input and return number of consonants in this string
def count_number_consonant(string):
    count = 0
    consonants = 'qwrtpsdfghjklzxcvbnm'
    for ch in string:
        if ch in consonants:
            count += 1
    return  count

def main():
    string = input("Enter a string")
    vowels = count_number_vowels(string)
    consonants = count_number_consonant(string)
    print("Number of vowels in this string is: ", str(vowels))
    print("Number of consonants in this string is: ", str(consonants))

main()
