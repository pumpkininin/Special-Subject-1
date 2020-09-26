def main():
    string = input("Enter a string as an argument: ")
    # Call the function capitalize_string
    capitalized_string = capitalize_string(string)
    print("String after capitalizing: ",capitalized_string)
# Function capitalize_string take a string as input and return a new string with first character is capitalized
def capitalize_string(string):
    # Split a string by a comma and space
    string_array = string.split('. ')
    result = ''
    for word in string_array:

        result += word.capitalize() +'. '
    return result

main()