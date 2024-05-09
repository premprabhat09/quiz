import time

def quiz():
    # Initialize score
    score = 0
    
    # List of questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion"],
            "answer": "B"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. Wa", "B. Wt", "C. W", "D. H2O"],
            "answer": "D"
        }
        # Add more questions here
    ]
    
    # Timer
    total_time = 60  # 60 seconds for the whole quiz
    start_time = time.time()
    
    # Ask questions
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        # Check if time is up
        if time.time() - start_time > total_time:
            print("Time's up!")
            break
        
        # Check answer
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!\n")
    
    # Display final score
    print("Quiz completed!")
    print("Your final score is:", score)
    
# Run the quiz
quiz()