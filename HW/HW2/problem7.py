def separate_word(string):
    new_string = string[0]
    for ch in string[1:]:
        if ch.isupper():
            new_string += ' ' + ch.lower()
        else:
            new_string += ch
    return new_string


def main():
    string = input("Enter a string: ")
    new_string = separate_word(string)
    print("New sentence: ", new_string)


main()