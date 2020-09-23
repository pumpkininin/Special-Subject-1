# The display_name method receives a string name and display this name as initial name.
def display_name(name):
    # Separate name by space and store in list separate_name
    separate_name = name.split(" ")
    # Declare a variable initials_name to store first letter of each attribute
    initials_name = ''
    # Get first letter of each attribute and add to initials_name
    for name in separate_name:
        # Add initial name and separate them by a dot
        initials_name += name[0].upper() + "."
    print("Your name is " + name + "and your initials is " + initials_name)


def main():
    # Ask users to enter first name
    first_name = str(input("Enter your first name: "))
    # Ask user to enter middle name
    middle_name = str(input("Enter your middle name: "))
    # Ask user to enter last name
    last_name = str(input("Enter your last name: "))
    # Combine first name, middle name and last name to get full name
    name = first_name + " " + middle_name + " " + last_name
    # Call the display_name function
    display_name(name)


# Call the main function
main()
