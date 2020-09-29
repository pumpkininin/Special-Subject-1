def convert_pig(sentence):
    words = sentence.split(' ')
    converted_words = []
    for word in words:
        if word[-1].isalpha():
            converted_words.append(word[1:] + word[0] + 'AY')
        else:
            converted_words.append(word[1:-1] + word[0] + "AY" +word[-1])
    converted_sentence = ' '.join(converted_words)
    return converted_sentence


def main():
    sentence = input("Enter a sentence: ")
    converted_sentence = convert_pig(sentence.upper())
    print(converted_sentence)


main()
