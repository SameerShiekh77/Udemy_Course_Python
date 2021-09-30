import json,pprint, requests
import  time as t
r = requests.get("https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=multiple")
# print(r.status_code)
# print(r.text)
# print(type(r.text))


# convert into json dictionary
questions = json.loads(r.text)

# print(questions)
# print(type(questions))

# print(pprint.pprint(questions))

