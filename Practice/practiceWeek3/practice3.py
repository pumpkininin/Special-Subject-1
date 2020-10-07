def convert_to_text(number):
    list_number = [int(i) for i in str(number)]
    sublist = [0 for i in range(len(list_number))]


    text_number = ['một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
    text = {0: 'trăm',1:' ',2:'mươi',3:'trăm',4:'nghìn',7:'triệu',10:'tỷ'}
    result = ''
    i= len(list_number)
    while i > 0:

        if 1 < i <= 3:
            result += text_number[list_number[-i]-1]+ ' ' + text[i] + ' '
        else:
            if i % 3 == 1:
                result += text_number[list_number[-i]-1]+ ' ' + text[i] + ' '
            else:
                result += text_number[list_number[-i]-1]+ ' ' + text[i % 3] + ' '
        i -= 1
    return result

def main():
    number = int(input("Enter amuont of money: "))
    a = convert_to_text(number)
    print(a)

main()
