import json, requests,html,pprint
import random
import  time as t
# r = requests.get("https://opentdb.com/api.php?amount=2&category=18&difficulty=easy&type=multiple")
# r = requests.get("https://opentdb.com/api.php?amount=15&category=18&difficulty=medium&type=multiple")
r = requests.get("https://opentdb.com/api.php?amount=10&category=19&difficulty=medium&type=multiple")

# convert into json dictionary
questions = json.loads(r.text)
# print(pprint.pprint(questions))
score = 0
# Create Quiz Game
i = 0
print("Let's Play Quiz....")
# starting loop
while i<10:
    # print questions
    print("Q" + str(i+1), html.unescape(questions['results'][i]['question'] + "\n"))
    answers = html.unescape(questions['results'][i]['incorrect_answers'])
    correct_answers = html.unescape(questions['results'][i]['correct_answer'])
    answers.append(correct_answers)
    # shuffle choices
    random.shuffle(answers)

    answer_number = 1
    # print options
    for answer in answers:
        print(str(answer_number) + ". " + html.unescape(answer))
        answer_number += 1

    # take input from user
    userAnswer = input("\nWrite Your Answer: ")

    # check answer
    if(correct_answers.lower() == userAnswer.lower()):
        print("Correct Answer!")
        score += 10
    else:
        print("Incorrect Answer!. The correct answer is: "+ html.unescape(correct_answers) )
    i += 1

print("\nQuiz Has completed!!")
print("Just Wait a mint we show your result")
t.sleep(3)
print("Your Score is: "+ str(score)+ " out of " ,i*10)
