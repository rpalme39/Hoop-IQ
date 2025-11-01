#!/usr/bin/env python3
"""
NBA Trivia Quiz Game - Test your Hoop IQ across different decades!
"""

def print_banner():
    """Display the game banner"""
    print("\n" + "=" * 60)
    print("          🏀 WELCOME TO HOOP IQ - NBA TRIVIA QUIZ 🏀")
    print("=" * 60)
    print()

def get_2000s_questions():
    """Return NBA trivia questions for the 2000s decade"""
    return [
        {
            "question": "Which team won the NBA Finals in 2000?",
            "options": ["A) Los Angeles Lakers", "B) Indiana Pacers", "C) Portland Trail Blazers", "D) San Antonio Spurs"],
            "answer": "A",
            "type": "multiple_choice"
        },
        {
            "question": "Who won the NBA MVP award in 2001?",
            "options": ["A) Shaquille O'Neal", "B) Allen Iverson", "C) Tim Duncan", "D) Kobe Bryant"],
            "answer": "B",
            "type": "multiple_choice"
        },
        {
            "question": "The Detroit Pistons won the NBA championship in 2004.",
            "options": ["True", "False"],
            "answer": "True",
            "type": "true_false"
        },
        {
            "question": "Who led the NBA in scoring during the 2005-06 season?",
            "options": ["A) LeBron James", "B) Kobe Bryant", "C) Allen Iverson", "D) Dwyane Wade"],
            "answer": "B",
            "type": "multiple_choice"
        },
        {
            "question": "Kobe Bryant scored 81 points in a single game in 2006.",
            "options": ["True", "False"],
            "answer": "True",
            "type": "true_false"
        }
    ]

def get_2010s_questions():
    """Return NBA trivia questions for the 2010s decade"""
    return [
        {
            "question": "Which team won the NBA Finals in 2011?",
            "options": ["A) Miami Heat", "B) Dallas Mavericks", "C) Los Angeles Lakers", "D) Boston Celtics"],
            "answer": "B",
            "type": "multiple_choice"
        },
        {
            "question": "LeBron James won back-to-back MVP awards in 2012 and 2013.",
            "options": ["True", "False"],
            "answer": "True",
            "type": "true_false"
        },
        {
            "question": "Which team did the Golden State Warriors defeat in the 2015 NBA Finals?",
            "options": ["A) Cleveland Cavaliers", "B) San Antonio Spurs", "C) Oklahoma City Thunder", "D) Miami Heat"],
            "answer": "A",
            "type": "multiple_choice"
        },
        {
            "question": "Who won the NBA MVP award in 2017?",
            "options": ["A) LeBron James", "B) James Harden", "C) Russell Westbrook", "D) Kawhi Leonard"],
            "answer": "C",
            "type": "multiple_choice"
        },
        {
            "question": "The Toronto Raptors won their first NBA championship in 2019.",
            "options": ["True", "False"],
            "answer": "True",
            "type": "true_false"
        }
    ]

def get_2020s_questions():
    """Return NBA trivia questions for the 2020s decade"""
    return [
        {
            "question": "Which team won the NBA Finals in the 2020 bubble season?",
            "options": ["A) Miami Heat", "B) Los Angeles Lakers", "C) Boston Celtics", "D) Milwaukee Bucks"],
            "answer": "B",
            "type": "multiple_choice"
        },
        {
            "question": "Nikola Jokic won the NBA MVP award in 2021.",
            "options": ["True", "False"],
            "answer": "True",
            "type": "true_false"
        },
        {
            "question": "Which team won the NBA championship in 2021?",
            "options": ["A) Phoenix Suns", "B) Milwaukee Bucks", "C) Los Angeles Lakers", "D) Brooklyn Nets"],
            "answer": "B",
            "type": "multiple_choice"
        },
        {
            "question": "Who won the NBA MVP award in 2023?",
            "options": ["A) Giannis Antetokounmpo", "B) Nikola Jokic", "C) Joel Embiid", "D) Jayson Tatum"],
            "answer": "C",
            "type": "multiple_choice"
        },
        {
            "question": "The Golden State Warriors won the NBA championship in 2022.",
            "options": ["True", "False"],
            "answer": "True",
            "type": "true_false"
        }
    ]

def display_question(question_data, question_num, total_questions):
    """Display a single question with its options"""
    print(f"\nQuestion {question_num}/{total_questions}")
    print("-" * 60)
    print(f"{question_data['question']}")
    print()
    
    if question_data['type'] == 'multiple_choice':
        for option in question_data['options']:
            print(f"  {option}")
    else:  # true_false
        print("  True or False?")
    print()

def get_user_answer(question_data):
    """Get and validate user's answer"""
    while True:
        if question_data['type'] == 'multiple_choice':
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        else:  # true_false
            answer = input("Your answer (True/False): ").strip().capitalize()
            if answer in ['True', 'False']:
                return answer
            else:
                print("Invalid input. Please enter True or False.")

def check_answer(user_answer, correct_answer):
    """Check if the user's answer is correct"""
    return user_answer == correct_answer

def play_quiz(decade):
    """Play the quiz for the selected decade"""
    print(f"\n🏀 Starting {decade} NBA Trivia Quiz!")
    print("Let's test your Hoop IQ!\n")
    
    # Get questions based on decade
    if decade == "2000s":
        questions = get_2000s_questions()
    elif decade == "2010s":
        questions = get_2010s_questions()
    else:  # 2020s
        questions = get_2020s_questions()
    
    score = 0
    total_questions = len(questions)
    
    # Ask each question
    for i, question_data in enumerate(questions, 1):
        display_question(question_data, i, total_questions)
        user_answer = get_user_answer(question_data)
        
        if check_answer(user_answer, question_data['answer']):
            print("✓ Correct! Great job!")
            score += 1
        else:
            print(f"✗ Incorrect. The correct answer was: {question_data['answer']}")
    
    # Display final score
    print("\n" + "=" * 60)
    print(f"           QUIZ COMPLETE - {decade} NBA TRIVIA")
    print("=" * 60)
    print(f"\nYour Score: {score}/{total_questions}")
    
    # Calculate percentage and give feedback
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%\n")
    
    if percentage == 100:
        print("🏆 PERFECT SCORE! You're a true NBA expert!")
    elif percentage >= 80:
        print("🌟 Excellent! You have great NBA knowledge!")
    elif percentage >= 60:
        print("👍 Good job! You know your NBA history!")
    elif percentage >= 40:
        print("📚 Not bad, but there's room for improvement!")
    else:
        print("💪 Keep studying! Your Hoop IQ will improve!")
    
    print("=" * 60)

def select_decade():
    """Let the user select which decade to play"""
    print("\nSelect a decade to test your Hoop IQ:")
    print("  1) 2000s - The Shaq & Kobe Era")
    print("  2) 2010s - The Big Three & Warriors Dynasty")
    print("  3) 2020s - The Modern Era")
    print("  4) Quit")
    print()
    
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            return "2000s"
        elif choice == '2':
            return "2010s"
        elif choice == '3':
            return "2020s"
        elif choice == '4':
            return None
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def main():
    """Main game loop"""
    print_banner()
    
    while True:
        decade = select_decade()
        
        if decade is None:
            print("\n👋 Thanks for playing Hoop IQ! See you next time!")
            break
        
        play_quiz(decade)
        
        print("\n" + "=" * 60)
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing Hoop IQ! See you next time!")
            break

if __name__ == "__main__":
    main()
