# TODO create a random quize for a times table/divide
# TODO create 40 qustions as a mixture of combination
# TODO write the quiz to a text file - named the quiz and the date
# TODO write an answersheet to another file to compare answers
# TODO add a countdown timer for 4 min - press enter to start

# example question 5 X 5 = 
# store the questions and answers in a dict
# call open, write and close for the quiz and answer key text fields
# use random.shuffle() to randomise the order of the questions 

import random, itertools, os
from datetime import datetime
# List containing the common numbers
oneTooTwelve = [1,2,3,4,5,6,7,8,9,10,11,12]
# List containing the questions
oneTimesQuestions = []
twoTimesQuestions = []
threeTimesQuestions = []
fourTimesQuestions = []
fiveTimesQuestions = []
sixTimesQuestions = []
sevenTimesQuestions = []
eightTimesQuestions = []
nineTimesQuestions = []
tenTimesQuestions = []
elevenTimesQuestions = []
twelveTimesQuestions = []

class TimesTableQuestion():

    def __init__(self, common_value, multiplyer, output_list):
        self.common_value = common_value
        self.multiplyer = multiplyer
        self.output_list = output_list

    def generateQuestion(self):
        for number in self.common_value:
            ans1 = (str(number) + ' X ' + str(self.multiplyer) + ' = ' + str(number * self.multiplyer))
            ans2 = (str(self.multiplyer) + ' X ' + str(number) + ' = ' + str(number * self.multiplyer))
            ans3 = (str(number * self.multiplyer) + ' / ' + (str(self.multiplyer) + ' = ' + (str(int((number * self.multiplyer) / self.multiplyer)))))
            # TODO add a line to include the divide questions - answer/common_value
            self.output_list.append(ans1)
            self.output_list.append(ans2)
            self.output_list.append(ans3)
            # TODO add the divide questions to the list
        return self.output_list

def initialiseLists():
    # Generate lists holding all the questions (and answers)
    # The TimesTableQuestion takes the numbers 1-12 as a list, the multiplyer, and the empty list name to put the result in as attributes
    oneTimesTable = TimesTableQuestion(oneTooTwelve,1,oneTimesQuestions)
    oneTimesTable.generateQuestion()

    twoTimesTable = TimesTableQuestion(oneTooTwelve,2,twoTimesQuestions)
    twoTimesTable.generateQuestion()

    threeTimesTable = TimesTableQuestion(oneTooTwelve,3,threeTimesQuestions)
    threeTimesTable.generateQuestion()

    fourTimesTable = TimesTableQuestion(oneTooTwelve,4,fourTimesQuestions)
    fourTimesTable.generateQuestion()

    fiveTimesTable = TimesTableQuestion(oneTooTwelve,5,fiveTimesQuestions)
    fiveTimesTable.generateQuestion()

    sixTimesTable = TimesTableQuestion(oneTooTwelve,6,sixTimesQuestions)
    sixTimesTable.generateQuestion()

    sevenTimesTable = TimesTableQuestion(oneTooTwelve,7,sevenTimesQuestions)
    sevenTimesTable.generateQuestion()

    eightTimesTable = TimesTableQuestion(oneTooTwelve,8,eightTimesQuestions)
    eightTimesTable.generateQuestion()

    nineTimesTable = TimesTableQuestion(oneTooTwelve,9,nineTimesQuestions)
    fiveTimesTable.generateQuestion()

    tenTimesTable = TimesTableQuestion(oneTooTwelve,10,tenTimesQuestions)
    tenTimesTable.generateQuestion()

    elevenTimesTable = TimesTableQuestion(oneTooTwelve,11,elevenTimesQuestions)
    elevenTimesTable.generateQuestion()

    twelveTimesTable = TimesTableQuestion(oneTooTwelve,12,twelveTimesQuestions)
    twelveTimesTable.generateQuestion()

def printAnswerSheet(question_list, folder_name):
    random.shuffle(question_list) # shuffle the question list
    infinate_loop = itertools.cycle(question_list) # continuously cycle the list
    question_set = itertools.islice(infinate_loop, 0, 40) # take the first 40 questions
    current_directory = os.getcwd()

    answer_file = open(current_directory + '/' + folder_name + '/Answer_Sheet.txt', 'w+')
    for question in question_set:# print the output
        # print(question + '\n')
        answer_file.write(question + '\n')
    answer_file.close()

def printQuestionSheet(answer_sheet):
    # TODO get the answer file, make a copy, remove the answers
    # TODO should have 2 seperate sheets, qustion and answer
    # TODO create a new folder each time a test is done with the date as the name
    pass

def makeNewFolder(testingTable):
    name = datetime.now()
    dt_string = name.strftime('%d_%m_%Y-%H.%M.%S')
    complete_string = dt_string + ' ' + testingTable
    os.mkdir(complete_string)
    return complete_string

def userChoice(choice):
    folder_title = choice + ' times table practice'
    if choice == '1':
        folder_name_one = makeNewFolder(folder_title)
        printAnswerSheet(oneTimesQuestions, folder_name_one)   
    if choice == '2':
        folder_name_two = makeNewFolder(folder_title)
        printAnswerSheet(twoTimesQuestions, folder_name_two) 
    if choice == '3':
        folder_name_three = makeNewFolder(folder_title)
        printAnswerSheet(threeTimesQuestions, folder_name_three)
    if choice == '4':
        folder_name_four = makeNewFolder(folder_title)
        printAnswerSheet(fourTimesQuestions, folder_name_four)
    if choice == '5':
        folder_name_five = makeNewFolder(folder_title)
        printAnswerSheet(fiveTimesQuestions, folder_name_five)
    if choice == '6':
        folder_name_six = makeNewFolder(folder_title)
        printAnswerSheet(sixTimesQuestions, folder_name_six)
    if choice == '7':
        folder_name_seven = makeNewFolder(folder_title)
        printAnswerSheet(sevenTimesQuestions, folder_name_seven)
    if choice == '8':
        folder_name_eight = makeNewFolder(folder_title)
        printAnswerSheet(eightTimesQuestions, folder_name_eight)
    if choice == '9':
        folder_name_nine = makeNewFolder(folder_title)
        printAnswerSheet(nineTimesQuestions, folder_name_nine)
    if choice == '10':
        folder_name_ten = makeNewFolder(folder_title)
        printAnswerSheet(tenTimesQuestions, folder_name_ten)
    if choice == '11':
        folder_name_eleven = makeNewFolder(folder_title)
        printAnswerSheet(elevenTimesQuestions, folder_name_eleven)
    if choice == '12':
        folder_name_twelve = makeNewFolder(folder_title)
        printAnswerSheet(twelveTimesQuestions, folder_name_twelve)
        
def userInput():
    user_choice = (input('Please enter a number between 1 & 12 of a times table you want to practice: \n'))
    return user_choice

def main():
    initialiseLists()
    choice = userInput()
    userChoice(choice)
    

main()