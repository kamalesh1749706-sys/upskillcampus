# Quiz Game - Python Project
# UpskillCampus Internship Project

questions = [
    {"question": "Which language is used for this quiz game?",
     "options": ["A. Java", "B. Python", "C. C++", "D. HTML"], "answer": "B"},
    {"question": "Which keyword defines a function in Python?",
     "options": ["A. func", "B. function", "C. def", "D. define"], "answer": "C"},
    {"question": "Which data type stores True or False?",
     "options": ["A. String", "B. Integer", "C. Boolean", "D. List"], "answer": "C"},
    {"question": "Which symbol starts a comment in Python?",
     "options": ["A. //", "B. #", "C. /*", "D. --"], "answer": "B"},
    {"question": "Which function gets input from the user?",
     "options": ["A. scan()", "B. read()", "C. input()", "D. get()"], "answer": "C"}
]

score = 0

print("=" * 45)
print("             PYTHON QUIZ GAME")
print("=" * 45)

for number, item in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {item['question']}")
    for option in item["options"]:
        print(option)

    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer in {"A", "B", "C", "D"}:
            break
        print("Invalid input. Please enter A, B, C, or D.")

    if user_answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {item['answer']}.")

print("\n" + "=" * 45)
print(f"Quiz completed! Your score: {score}/{len(questions)}")
percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 50:
    print("Good job! Keep practicing.")
else:
    print("Keep practicing and try again.")
print("=" * 45)
