def convert(string):
    #store code in a dict
    code = {',':'--..--','.':'.-.-.-','?':'..--..','0':'-----',
            '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
            '6':'-....','7':'--...','8':'---..','9':'----.',
            'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',
            'f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-',
            'l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-',
            'r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
            'y':'-.-','z':'--..'}

    stringOutput = ""
    # Step through each character in the string
    for i in string:
        #add morse code to stringOutput
        if(i == ' '):
            stringOutput += i
        else:
            stringOutput += code[i] + ' '
    #return a string store morse code
    return stringOutput
def main():
    #Ask user to enter a string
    string = str(input("Enter a string: "))
    #call convert function then print
    print("The morse code of this string is "+convert(string))


main()
