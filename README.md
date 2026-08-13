# 🧠 Python Quiz Application

A console-based Quiz Application developed in Python.

This project started as a simple quiz program and was gradually improved by adding
functions, Object-Oriented Programming (OOP), JSON file handling, random questions,
multiple categories, a timer, score saving, and a leaderboard system.

---

## 📌 Project Overview

The Python Quiz Application allows a player to:

- Enter their name
- Select a quiz category
- Answer multiple-choice questions
- Get a limited amount of time for each question
- Receive immediate feedback
- Calculate correct and wrong answers
- Calculate percentage
- Get a grade
- Save quiz results into a JSON file
- View the overall leaderboard
- View a category-specific leaderboard
- Play the quiz multiple times

Questions and categories are stored separately in a JSON file, while quiz results
are stored in another JSON file.

=====================================================================================================

🐍 Python Terminal Quiz Application:

A feature-rich, object-oriented, interactive terminal quiz application built with Python. It features multiple programming categories, timed question prompts, dynamic score persistence, a competitive leaderboard, and comprehensive analytical statistics.

🌟 Key Features
🎮 Dynamic Main Menu: Clean navigation separating quiz execution, leaderboard viewing, and statistics inspection.

📂 Categorized Question Base: JSON-driven question structure supporting multiple categories (Python, Java, JavaScript, C++, HTML, CSS, SQL, Git).

⏳ Non-Blocking Countdown Timer: Smooth 10-second prompt timer per question powered by inputimeout to eliminate ghost threads.

🔀 Randomized Experience: Automatic shuffling of questions using random.sample() for every new attempt.

💾 Persistent Score Tracking: Automatically updates scores.json using non-destructive file reading/writing routines.

🏆 Competitive Leaderboard:

Overall Leaderboard: Ranks all past games globally based on highest percentage.

Category Leaderboard: Displays rankings filtered specifically by category.

📊 Analytics & Statistics:

Overall Stats: Total games played, unique players, high scores, overall average percentage, total correct/wrong answers, and most played category.

Personal Stats: Tracks active player performance history (games played, best score, average score, total correct/wrong answers).

🛡️ Bulletproof Input Validation: Built-in exception and type validation prevents crashing on invalid keyboard input.

📂 Project Architecture
Plaintext
01_Quiz_application_project/
│
├── main.py                             # Core application code (Quiz, Question, Menu, Stats)
├── diff_questions_category.json        # Categorized question bank
└── scores.json                         # Persistent player score records (Auto-generated)
🚀 Getting Started
Prerequisites
Python 3.8 or higher installed on your system.

inputimeout library for cross-platform timed terminal inputs.

Installation & Setup
Clone or Download the Repository:

Bash
git clone https://github.com/your-username/quiz-application.git
cd quiz-application
Install Required Packages:

Bash
pip install inputimeout
Run the Application:

Bash
python main.py
🎮 How to Play
Enter Player Name: Type your name when the application launches.

Main Menu Navigation:

Enter 1 to Start Quiz

Enter 2 to View Leaderboard

Enter 3 to Check Statistics

Enter 0 to Exit

Select a Category: Choose from the available topics (e.g., Python, Java, SQL).

Answer Questions: You have 10 seconds per question to enter A, B, C, or D.

Review Results: See your total score, percentage, grade, and automatically save your result to scores.json!

💻 Tech Stack & Concepts Applied
Language: Python 3

Data Storage: JSON (json module)

Design Pattern: Object-Oriented Programming (OOP)

Core Concepts Used:

Classes & Objects (Quiz, Question)

File Handling (json.load(), json.dump(), os.path.exists())

Data Processing & Sorting (lambda functions, list comprehensions, frequency dictionaries)

Error Handling (try...except, .isdigit())

Terminal String Formatting (F-Strings, width alignment)

📜 Example JSON Score Output
Scores are saved in scores.json structured as follows:

JSON
[
    {
        "name": "Hassam",
        "category": "Python",
        "correct": 8,
        "wrongs": 2,
        "percentage": 80.0,
        "Grade": "A"
    },
    {
        "name": "Ali",
        "category": "Python",
        "correct": 9,
        "wrongs": 1,
        "percentage": 90.0,
        "Grade": "A+"
    }
]
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.