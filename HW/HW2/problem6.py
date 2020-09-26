# Function cal_frequency take a string as input and return character that appear most
def cal_frequency(string):
    # Creat a dictionary that its keys are character of string and value is the times it appears
    frequency_dict = dict.fromkeys(string,0)
    char_appear_most = ''
    count_frequency = 0
    for ch in string:
        frequency_dict[ch] += 1
    for key in frequency_dict:
        if frequency_dict[key] >= count_frequency:
            count_frequency = frequency_dict[key]
            char_appear_most = key
    print(frequency_dict)
    return char_appear_most


def main():
    string = input("Enter a string: ")
    # Call cal_frequency function to get character appear most frequently
    char_appear_most = cal_frequency(string)
    print("The character that appear most frequently is ", char_appear_most)


main()


