def read_file():
    rating_file = open("ratings.txt")
    #store rating of book
    data = []
    #store username
    users = []
    #return a list containing each line in the file
    f= rating_file.readlines()
    #back to the first line of file to read
    rating_file.seek(0)
    for i,line in enumerate(rating_file):
        if(i%3==1):
            data.append(line.rstrip())
        if(i%3 == 0):
            users.append(line.rstrip())
    data = list(list(dict.fromkeys(data)))
    users = list(list(dict.fromkeys(users)))
    rating_file.seek(0)
    #a dictionary to store user and score they rated
    rating_data = {}
    #s dictionary to store book name and a list which contain a total of rating score and number of rate
    averages = {}
    for d in data:
        averages[d] = [0,0]
    for u in users:
        rating_data[u] = [ 0 for i in range(len(data))]
    for i, line in enumerate(rating_file):
        for d in range(len(data)):
            if(data[d] == line.rstrip()):
                rating_data[f[i-1].rstrip()][d] = int(f[i+1].rstrip())
                averages[data[d]][0] += int(f[i+1].rstrip())
                averages[data[d]][1] += 1
    #from this step averages is a dict contain only book name and it's average rating score
    for key in averages:
        averages[key] = averages[key][0]/averages[key][1]
    return data, users, rating_data, list(averages.items())


def recommed():
    users = read_file()[1]
    rating_data = read_file()[2]
    data = read_file()[0]
    user = str(input("user?")).capitalize()
    # a list cointain a lot of tuple. Each tuple contain other user and similarity score between user and others
    similarity = []
    #if typing wrong username, display average rating, else display recommendation
    if not user in users:
        averages()
    else:
        for key, value in rating_data.items():
            if( key == user):
                continue
            else:
                sim = 0
                for i in range(len(value)):
                    sim += rating_data[user][i] * rating_data[key][i]
                similarity.append((sim, key))
                #sort by value first then sort by name
                similarity.sort(key = lambda  x:x[0], reverse=True)
        most_similar = similarity[:3]
        average_rating = [0 for i in range(len(data))]
        for j in range(len(average_rating)):
            count = 0
            for i in most_similar:
                rating = rating_data[i[1]][j]
                if(rating != 0):
                    average_rating[j] += rating
                    count +=1
            if count == 0:
                average_rating[j] = 0
            else:
                average_rating[j] = average_rating[j]/count
        book_rating = []
        for i in range(len(average_rating)):
            book_rating.append((average_rating[i], data[i], ))
        #sort by rating score of book then sort by name
        book_rating.sort(key = lambda x:(x[0],x[1]), reverse=True)
        print("----------------------------------------------------")
        print("Recommendation: ")
        for i in book_rating:
            print(i[1] + ":" + str(i[0]))
def averages():
    averages = read_file()[3]
    # sort by average rating score of book then sort by name
    averages.sort(key=lambda x: (x[1],x[0]), reverse=True)
    print("----------------------------------------------------")
    print("Recommendation: ")
    for i in averages:
        print(i[0] + " " + str(i[1]))


def main():
    while True:
        print("=============================================================")
        choice = str(input("Welcome to the CSC110 Book Recommender. "
                           "Type the word in the left column to do the ation on the right. "
                            "\n recommend  : recommend books for a particuler user"
                            "\n averages   : output the average ratings of all books in the systen"
                            "\n quit       : exit the program"
                            "\n next task?\n"))

        if choice == "recommend":
            recommed()
        elif choice  == "averages":
            averages()
        elif choice == "quit":
            break


main()