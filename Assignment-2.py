#Name:Jazim.J
#Reg.no:192210471

#Question 1:

# Function to read questions from Questions.txt
def read_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        current_question = None

        for line in lines:
            line = line.strip()
            if line:
                if line.startswith('Q:'):
                    if current_question:
                        questions.append(current_question)
                    current_question = {"question": line[2:], "options": []}
                elif line.startswith('A:'):
                    current_question["options"].append(line[2:])
        
        if current_question:
            questions.append(current_question)

    return questions

# Function to read correct answers from Answers.txt
def read_answers(file_name):
    answers = []
    with open(file_name, 'r') as file:
        answers = [line.strip() for line in file]

    return answers

# Function to display quiz questions and options
def display_quiz(questions):
    for i, question in enumerate(questions):
        print(f"{i + 1}. {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"   {chr(ord('A') + j)}. {option}")
        print()

# Function to display correct answers
def display_answers(questions, answers):
    print("Correct Answers:")
    for i, (question, correct_answer) in enumerate(zip(questions, answers)):
        print(f"{i + 1}. {question['question']}")
        print(f"   Correct Answer: {correct_answer}")
        print()

if __name__ == "__main__":
    questions_file = "Questions.txt"
    answers_file = "Answers.txt"

    quiz_questions = read_questions(questions_file)
    correct_answers = read_answers(answers_file)

    if len(quiz_questions) != len(correct_answers):
        print("Error: Number of questions and answers do not match.")
    else:
        print("Welcome to the Quiz!")
        display_quiz(quiz_questions)
        input("Press Enter to see the correct answers...")
        display_answers(quiz_questions, correct_answers)


#Question 2:

# Define custom exceptions
class ValueTooLarge(Exception):
    pass

class ValueTooSmall(Exception):
    pass

# Function to play the number guessing game
def play_game(target_number):
    while True:
        try:
            user_guess = int(input("Guess the number: "))
            if user_guess > target_number:
                raise ValueTooLarge
            elif user_guess < target_number:
                raise ValueTooSmall
            else:
                print("Congratulations! You guessed the correct number.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ValueTooLarge:
            print("Too large! Try again.")
        except ValueTooSmall:
            print("Too small! Try again.")

if __name__ == "__main__":
    try:
        target_number = int(input("Enter the number to be guessed: "))
        play_game(target_number)
    except ValueError:
        print("Invalid input. Please enter a valid number as the target.")

#Sample output:

Enter the number to be guessed: 3
Guess the number: 3
Congratulations! You guessed the correct number.

#Question 3:

d = {"R": 0, "G": 255, "B": 0, "other": {"opacity": 0.6}}

# (a) d["R"]
# Return value: 0
# Final value of d: {"R": 0, "G": 255, "B": 0, "other": {"opacity": 0.6}}
result_a = d["R"]

# (b) d.pop("R")
# Return value: 0
# Final value of d: {"G": 255, "B": 0, "other": {"opacity": 0.6}}
result_b = d.pop("R")

# (c) d["R"] = 255
# Return value: None (assignment)
# Final value of d: {"G": 255, "B": 0, "R": 255, "other": {"opacity": 0.6}}
result_c = d["R"] = 255

# (d) d["H"]
# This raises a KeyError because "H" is not in the dictionary, and d remains unchanged.
try:
    result_d = d["H"]
except KeyError as e:
    result_d = str(e)

# (e) d.keys()
# Return value: dict_keys(['R', 'G', 'B', 'other'])
# Final value of d: {"G": 255, "B": 0, "R": 255, "other": {"opacity": 0.6}}
result_e = d.keys()

# (f) d["other"]["blur"] = 0.1
# Return value: None (assignment)
# Final value of d: {"R": 0, "G": 255, "B": 0, "other": {"opacity": 0.6, "blur": 0.1}}
result_f = d["other"]["blur"] = 0.1

# (g) d[["H","S","L"]] = [120,98,5]
# This raises a TypeError because a list cannot be used as a dictionary key, and d remains unchanged.
try:
    result_g = d[["H", "S", "L"]] = [120, 98, 5]
except TypeError as e:
    result_g = str(e)

# (h) d["R","B","G"]
# This raises a TypeError because a tuple cannot be used as a dictionary key directly, and d remains unchanged.
try:
    result_h = d["R", "B", "G"]
except TypeError as e:
    result_h = str(e)

# Printing the results
print("(a) d[\"R\"]: ", result_a)
print("(b) d.pop(\"R\"): ", result_b)
print("(c) d[\"R\"] = 255: ", result_c)
print("(d) d[\"H\"]: ", result_d)
print("(e) d.keys(): ", list(result_e))
print("(f) d[\"other\"][\"blur\"] = 0.1: ", result_f)
print("(g) d[\"H\",\"S\",\"L\"] = [120,98,5]: ", result_g)
print("(h) d[\"R\",\"B\",\"G\"]: ", result_h)

#Question 4:

# Define the questions and answers as separate lists
questions = ["What is the capital of France?", "Who wrote the play 'Romeo and Juliet'?", "What is the largest planet in our solar system?"]
answers = ["Paris", "William Shakespeare", "Jupiter"]

# Create a quiz function using zip
def create_quiz(questions, answers):
    score = 0

    # Combine questions and answers using zip
    quiz = zip(questions, answers)

    for question, correct_answer in quiz:
        user_answer = input(f"{question}\nYour answer: ").strip()
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.\n")

    print(f"Quiz completed! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Quiz!")
    create_quiz(questions, answers)

#Sample output:

Welcome to the Quiz!
What is the capital of France?
Your answer: paris
Correct!

Who wrote the play 'Romeo and Juliet'?
Your answer: William Shakespeare
Correct!

What is the largest planet in our solar system?
Your answer: Jupiter
Correct!

Quiz completed! Your score: 3/3

#Question 5:

# Create a tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)

# Get the 4th element (index 3)
fourth_element = my_tuple[3]

# Get the 4th element from the end (index -4)
fourth_from_end = my_tuple[-4]

# Print the results
print("4th element:", fourth_element)
print("4th element from the end:", fourth_from_end)

#Sample output:

4th element: 4
4th element from the end: 5

