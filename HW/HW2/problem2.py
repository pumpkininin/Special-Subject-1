def main():
    date = str(input("Enter date in form mm/dd/yy: "))
    print_date(date)


def print_date(date):
    new_date = date.split("/")
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    string_date = ""
    string_date += months[int(new_date[0])-1]+' '
    string_date += new_date[1]
    string_date += ', '
    string_date += new_date[2]
    print(string_date)


main()
