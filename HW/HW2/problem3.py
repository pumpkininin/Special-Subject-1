
def main():
    stringPhone = str(input("Enter the phone number: "))
    translated_phone = translate(stringPhone)
    print(translated_phone)
# Function spilt take input as a string and return list of character of that string
def split(word):
    return [char for char in word]

# Function translate take a phone number as input and translate it to standard number
def translate(stringPhone):
    # Call split function to get a list of char
    letters = split(stringPhone)
    result = ''
    for letter in letters:
        if '0'<=letter <='9' or letter == '-' :
            result +=letter
        elif 'a' <= letter <= 'c':
            result += str(2)
        elif 'd' <= letter <= 'f':
            result += str(3)
        elif 'g' <= letter <= 'i':
            result += str(4)
        elif 'j' <= letter <= 'l':
            result += str(5)
        elif 'm' <= letter <= 'o':
            result += str(6)
        elif 'p' <= letter <= 's':
            result += str(7)
        elif 't' <= letter <= 'u':
            result += str(8)
        elif 'w' <= letter <= 'z':
            result += str(9)
    return result


main()