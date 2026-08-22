quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct_answer": "4"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Mercury"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "correct_answer": "Pacific Ocean"
    }
]


print("Welcome to the Quiz!")

print("Please answer the following questions:")


for question in quiz:
    print("\n" + question["question"])
    for index, option in enumerate(question["options"], start=1):
        print(f"{index}. {option}")
    user_answer = input("Your answer (1-4): ")
    if question["options"][int(user_answer) - 1] == question["correct_answer"]:
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["correct_answer"])


