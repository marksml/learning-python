# sys is a module which let's us access command line arguments via sys.argv
# docu: https://docs.python.org/3.13/library/sys.html

import sys
import random

# sys.argv[0] contains the scriptfile name "flashcards.py"
# print("sys.argv[0]: "+ sys.argv[0])

if len(sys.argv) < 2:
    print("Please supply a flash card file")
    exit(1)

flashcard_filename = sys.argv[1]
f = open(flashcard_filename,"r",encoding="UTF-8")

question_dictionary = {}

for line in f:
    line = line.strip()
    #print("line: '" + line + "' of type "+ str(type(line)))
    entry = line.split(",")
    question = entry[0]
    answer = entry[1]
    question_dictionary[question] = answer

f.close()

print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' as a answer in order to quit the quiz.")
print("")

questions = list(question_dictionary.keys())

while True:
    question = random.choice(questions)
    anser = question_dictionary[question]

    print("Question:" + question)
    user_input = input("Your guess: ")

    if user_input == "quit" :
        print("Thank you for playing. Bye.")
        break
    elif user_input == answer:
        print("Correct :-)!")
    else:
        print("Sorry - the answer was: " + answer)
