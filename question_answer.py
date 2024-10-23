import random

# Define your 100 questions, answers, and options in a list of dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["George Orwell", "Harper Lee", "J.K. Rowling", "Ernest Hemingway"],
        "answer": "Harper Lee"
    }
    # Add your remaining questions here
]

def quiz_game():
    score = 0  # Initialize score
    random.shuffle(questions)  # Shuffle the questions for randomness

    # Loop over each question
    for q in questions:
        print("\n" + q["question"])  # Display the question

        # Display the answer options
        for idx, option in enumerate(q["options"], 1):
            print(f"{idx}. {option}")

        # Get user's choice (input as a number)
        try:
            user_choice = int(input("Choose the correct option (1-4): "))
            if user_choice < 1 or user_choice > len(q["options"]):
                print("Invalid choice, skipping this question.")
                continue
        except ValueError:
            print("Invalid input, please enter a number. Skipping this question.")
            continue

        # Get the chosen option based on the user's input
        chosen_option = q["options"][user_choice - 1]

        # Check if the selected option is correct
        if chosen_option == q["answer"]:
            print("Correct!")
            score += 1  # Increase score if correct
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")

    # Display final score
    print(f"\nQuiz finished! You got {score} out of {len(questions)} correct.")

# Run the quiz game
quiz_game()