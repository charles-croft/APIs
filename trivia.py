import requests
import random
import html

EDUCATION_CATEGORY_ID = 11
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"

def fetch_trivia_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        questions = data.get('results', [])
        return questions
    else:
        print("Failed to fetch trivia questions.")
        return []

def run_quiz():
    questions = fetch_trivia_questions()
    if not questions:
        return

    score = 0
    for index, question in enumerate(questions):
        print(f"\nQuestion {index + 1}: {html.unescape(question['question'])}")
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)
        for i, q in enumerate(questions, 1):
            question = html.unescape(q['question'])
            correct = html.unescape(q['correct_answer'])
            incorrects = [html.unescape(a) for a in q['incorrect_answers']]
            options = incorrects + [correct]
            random.shuffle(options)
            print(f"\nQuestion {i}: {question}")
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")
            while True:
                try:
                    choice = int(input("Your answer (1-4): "))
                    if 1 <= choice <= 4:
                        break
                except ValueError:
                    pass
                print("Invalid input. Please enter a number between 1 and 4.")
            if options[choice - 1] == correct:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {correct}")
        print(f"\nYour final score is: {score}/{len(questions)}")
        print(f"Percentage: {score / len(questions) * 100:.2f}%")
if __name__ == "__main__":
    print("Welcome to the Trivia Quiz!")
    run_quiz()