def driver_license_exam():
        count = 0
        correct_answer = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
        answer_file = open("answer.txt","r+")
        answer_string = answer_file.read()
        print(answer_string)
        answer_list = []
        wrong_answer_list = []
        for i in range(len(answer_string)):
                if answer_string[i] == '.' or answer_string[i] == '. ':
                        answer_list.append(answer_string[i+1])
        print(answer_list)
        for i in range(len(answer_list)):
                if answer_list[i] == correct_answer[i]:
                        count += 1
                else:
                        wrong_answer_list.append(str(i+1))
        if(count >= 15):
                print("Passed!")
                print("Score: "+count)
        print("Total number of correct answer is ", count, "and the total of wrong answer is",str(20-count))
        print("List of question that incorrect: ", wrong_answer_list)


def main():
        string = '1    2 5 124'
        print(string.split(' '))
        driver_license_exam()

main()
