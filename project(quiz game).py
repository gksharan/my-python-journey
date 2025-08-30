# Simple Quiz Game 🎮
# Author: gk

# List of quiz questions
questions = [
    {"question": "What is the largest planet in our Solar System?", "answer": "Jupiter"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"question": "Which programming language is symbolized by a snake?", "answer": "Python"},
    {"question": "Who is the founder of Microsoft?", "answer": "Bill Gates"},
]

score = 0  # Keep track of points

print("🎉 Welcome to the Quiz Game! 🎉\n")

for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer.strip().lower() == q["answer"].lower():
        print("✅ Correct!\n")
        score += 2
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.\n")
        score -= 1

print(f"🏆 Your Final Score: {score}")
