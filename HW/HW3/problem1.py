#function create_question can be use to create a text file to store all question and answer
def create_question():
        question_file = open("question.txt","w+")
        correct_answer = open("correct_answer.txt","w+")
        question_number = 1
        #ask user to put question, answer and correct answer
        #this text cannot have more than 20 question
        while question_number <= 20:
                question = input("Enter the question: ")
                question_file.writelines(str(question_number)+'. '+question + '\n')
                question_number +=1
                question_file.writelines('A.' + str(input("enter the answer A."))+ '\n')
                question_file.writelines('B.' + str(input("enter the answer B."))+ '\n')
                question_file.writelines('C.' + str(input("enter the answer C."))+ '\n')
                question_file.writelines('D.' + str(input("enter the answer D."))+ '\n')
                #Ask user to add correct answer then store it in a text file
                correct_answer.writelines(str(input("Enter the correct answer: ")))
                continue_box = input("continue? (y/n)")
                if(continue_box.lower().__contains__("n")):
                        break
#function load question loads a text file containing question then return a list of question and answer
def load_question():
        question_file = open("question.txt", "r")
        questions = question_file.readlines()
        return questions
#function do test print question and answer then ask user put their answer then store in a text file
def do_test():
        answer_file = open("myanswer.txt","w+")
        questions = load_question()
        print(len(questions))
        print(questions[5])
        for question_no in range(len(questions)):
                print(questions[question_no])
                if(question_no % 5 == 4):
                        answer = str(input("Enter your answer: "))
                        answer_file.write(str(question_no) + '.' + answer)
        return answer_file

#function mark_answer read 2 file, first one is the file contain answer of examiner other contain correct answer
#then calculate score based on correct answer
def mark_answer():
        count = 0
        answer_file = open("myanswer.txt","r")
        correct_answer_file = open("correct_answer.txt","r")
        answers = answer_file.readlines()
        correct_answer = correct_answer_file.readlines()
        for i in range(len(answers)):
                if answers[i] == correct_answer[i]:
                       count += 1
        mark = float(count/20 * 10)
        print("Your mark: {0:3.2f}".format(mark))








def main():
        create_question()
        do_test()
        mark_answer()


main()





