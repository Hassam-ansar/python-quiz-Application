
import json as js
import random
import os
# import threading
from inputimeout import TimeoutOccurred, inputimeout


# Load questions from json file..
with open("PYTHON-QUIZ-APPLICATION\diff_questions_category.json", "r") as file:
    diff_questions_category = js.load(file)

print(f"Type of questions:{type(diff_questions_category)}")


class Question:

    def __init__(self, dict_question, i, total_questions):
        self.dict_question = dict_question
        self.i = i
        self.total_questions = total_questions

    def display_question(self):
        print(f"Question:{self.i}/{self.total_questions}: {self.dict_question['Question']}")
        print(f"A : {self.dict_question['A']}")
        print(f"B : {self.dict_question['B']}")
        print(f"C : {self.dict_question['C']}")
        print(f"D : {self.dict_question['D']}\n")


class Quiz:

    def __init__(self,player_name, cat_name, questions,corrects=0,wrongs=0,percentage=0,grade="",time_limit=10):
        self.player_name = player_name
        self.cat_name = cat_name
        self.questions = questions
        self.corrects = corrects
        self.wrongs = wrongs
        self.percentage = percentage
        self.grade = grade
        self.time_limit = (
            time_limit  # Version 6: Time limit per question in seconds
        )

    def welcome(self):
        # print(f"======================================\n\tPYTHON QUIZ APPLICATION\n======================================")
        print(f"======================================\n\tQUIZ START\n======================================")
        print(f"welcome ! ")
        print(f"Note: You have {self.time_limit} seconds per question!\n")
        input("Press enter to start...")
        print("\n")

    def get_answer_with_timer(self):
        while True:
            try:
                your_answer = (inputimeout(prompt=f"Enter your answer (A/B/C/D) [{self.time_limit}s]: ",timeout=self.time_limit,).strip().upper())

                if your_answer in ["A", "B", "C", "D"]:
                    return your_answer
                else:
                    print("Please enter a valid option from (A / B / C / D):\n")
 
            except TimeoutOccurred:
                print("\n⏰ Time's Up!")
                return None

        

    def check_answer(self, your_answer, correct_answer):

        if(your_answer is None):
            self.wrongs = self.wrongs + 1
            print(f"Correct answer was : {correct_answer}\n")

        elif(your_answer == correct_answer):
            self.corrects = self.corrects + 1
            print(f"Correct !\n")

        else:
            self.wrongs = self.wrongs + 1
            print(f"Wrong !")
            print(f"Correct answer was : {correct_answer}\n")

    # Calculate percentage
    def cal_percentage(self):
        self.percentage = ((self.corrects) / len(self.questions)) * 100

    # Calculate grade
    def cal_grade(self):

        if (self.percentage >= 85):
            self.grade = "A+"

        elif(self.percentage < 85 and self.percentage >= 80):
            self.grade = "A"

        elif(self.percentage < 80 and self.percentage >= 75):
            self.grade = "B+"

        elif(self.percentage < 75 and self.percentage >= 70):
            self.grade = "B"

        elif(self.percentage < 70 and self.percentage >= 65):
            self.grade = "C+"

        elif(self.percentage < 65 and self.percentage >= 60):
            self.grade = "C"

        elif(self.percentage < 60 and self.percentage >= 55):
            self.grade = "D+"

        elif(self.percentage < 55 and self.percentage >= 50):
            self.grade = "D"

        else:
            self.grade = "Fail!"

    def show_result(self):
        print(f"======================================\n\tQUIZ FINISHED\n======================================")
        print(f"Player name : {self.player_name}")
        print(f"Category : {self.cat_name}")
        print(f"Correct answers = {self.corrects}")
        print(f"Wrong answers = {self.wrongs}")
        print(f"Your percentage = {self.percentage}%")
        print(f"Grade : {self.grade}")


    # Version 8: Method to save player score without overwriting previous results
    def save_result(self):
        file_path = r"PYTHON-QUIZ-APPLICATION \scores.json"

        scores_data = []

        # step 1: Read existing scores if file exists
        if(os.path.exists(file_path)):
            try:
                with open(file_path ,"r") as file:
                    scores_data = js.load(file)
            except Exception:
                scores_data = []

        # step 2 :Create dictionary for current match result
        new_scores = {
            "name" : self.player_name,
            "category" : self.cat_name,
            "correct" : self.corrects,
            "wrongs" : self.wrongs,
            "percentage" : self.percentage,
            "Grade" : self.grade
        }

        # step 3: Append new score to existing scores list
        scores_data.append(new_scores)

        # step 4: Write updated list back to scores.json
        with open(file_path, "w") as file:
            js.dump(scores_data, file, indent=4)

        print("\n[Result successfully saved to scores.json!]\n")
        

    # Reset score for playing again
    def reset_quiz(self):
        self.corrects = 0
        self.wrongs = 0
        self.percentage = 0
        self.grade = ""

    def run_quiz_loop(self):
        # Reset counts before starting questions
        self.reset_quiz()

        # Version 5: Shuffle questions
        shuffle_questions = random.sample(self.questions, len(self.questions))

        for i in range(1, len(shuffle_questions) + 1):
            dict_question = shuffle_questions[i - 1]

            # Question class object and methods
            ques_obj = Question(dict_question, i, len(shuffle_questions))
            ques_obj.display_question()

            # Version 6: Get answer with timer limit
            your_answer = self.get_answer_with_timer()
            self.check_answer(your_answer, dict_question["Answer"])

        self.cal_percentage()
        self.cal_grade()
        self.show_result()
        self.save_result()


# Helper to load scores safely
def load_score_data():
    file_path = r"PYTHON-QUIZ-APPLICATION \scores.json"
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as file:
            return js.load(file)
    except Exception:
        return []


# Version_9 : Leaderboard function 
def show_leaderboard(all_categories):

    file_path = r"PYTHON-QUIZ-APPLICATION \scores.json"

    if not os.path.exists(file_path):
        print("\n======================================\n\t🏆 LEADERBOARD\n======================================")
        print("No quiz results available yet. Play a quiz first!\n")
        input("Press Enter to return to menu...")
        return

    try:
        with open(file_path, "r") as file:
            score_data = js.load(file)
    except Exception:
        score_data = []

    if not score_data:
        print("\n======================================\n\t🏆 LEADERBOARD\n======================================")
        print("No quiz results available yet. Play a quiz first!\n")
        input("Press Enter to return to menu...")
        return
    
    category_list = list(all_categories.keys())

    # Filter menu
    while True:
        print(f"\n======================================\n\t🏆 LEADERBOARD MENU\n======================================")
        print(f"1. Overall Leaderboard")
        print(f"2. Category-Specific Leaderboard")
        print(f"0. Back to Main Menu")

        lead_choice = input("\nChoose an option: ").strip()

        if(lead_choice == "0"):
            return

        elif(lead_choice == "1"):
            filter_cat = None
            title = "🏆 OVERALL LEADERBOARD"
            break

        elif(lead_choice == "2"):
            print("\nSelect Category for Leaderboard:")
            for i in range(len(category_list)):
                print(f"{i + 1}. {category_list[i]}")

            cat_choice = input("Enter number: ").strip()
            if(cat_choice.isdigit()):
                idx = int(cat_choice) - 1
                if(idx >= 0 and idx < len(category_list)):
                    filter_cat = category_list[idx]
                    title = f"🏆 {filter_cat.upper()} LEADERBOARD"
                    break
            print("Invalid choice!")
        else:
            print("Invalid choice!")

    # Step 7: Filter results by category if selected
    if filter_cat:
        filtered_scores = [
            s for s in score_data if s.get("category") == filter_cat
        ]
    else:
        filtered_scores = list(score_data)

    if not filtered_scores:
        print(f"\nNo scores recorded for category '{filter_cat}' yet.")
        input("Press Enter to continue...")
        return

    # Step 4: Sort scores by percentage from highest to lowest
    filtered_scores.sort(key=lambda x: x["percentage"], reverse=True)

    # Step 5 & 6: Display leaderboard table with rankings
    print(f"\n==================================================\n\t{title}\n==================================================")
    print(f"{'Rank':<6}{'Player':<15}{'Category':<15}{'Percentage':<12}{'Grade':<6}")
    print("-" * 54)

    for rank in range(1, len(filtered_scores) + 1):
        s = filtered_scores[rank - 1]
        print(f"{rank:<6}{s['name']:<15}{s['category']:<15}{s['percentage']:<11.1f}% {s['Grade']:<6}")

    print("=" * 54)
    input("\nPress Enter to return to menu...")


# Version_ 10 : show statistics func
def show_statistics(player_name):

    score_data = load_score_data()

    if(not score_data):
        print("\n======================================\n\t📊 STATISTICS\n======================================")
        print("No quiz results available yet. Play a quiz first!\n")
        input("Press Enter to return to menu...")
        return

    print("\n==================================================\n\t📊 APPLICATION STATISTICS\n==================================================")

    # --- 1. OVERALL STATS ---
    total_games = len(score_data)
    unique_players = len(set(s["name"] for s in score_data))
    all_percentages = [s["percentage"] for s in score_data]
    highest_score = max(all_percentages)
    avg_score = sum(all_percentages) / total_games
    total_correct = sum(s["correct"] for s in score_data)
    total_wrongs = sum(s["wrongs"] for s in score_data)

    # Find most played category
    cat_counts = {}
    for s in score_data:
        c = s["category"]
        cat_counts[c] = cat_counts.get(c, 0) + 1
    most_played_cat = max(cat_counts, key=cat_counts.get)

    print("--- OVERALL STATS ---")
    print(f"Total Games Played     : {total_games}")
    print(f"Total Unique Players   : {unique_players}")
    print(f"Highest Score          : {highest_score:.1f}%")
    print(f"Average Score          : {avg_score:.1f}%")
    print(f"Total Correct Answers  : {total_correct}")
    print(f"Total Wrong Answers    : {total_wrongs}")
    print(f"Most Played Category   : {most_played_cat} ({cat_counts[most_played_cat]} games)")


    # --- 2. PLAYER STATS ---
    # player_scores = [
    #     s for s in score_data if s["name"].lower() == player_name.lower()
    # ]

    # --- 2. PLAYER STATS ---
    player_scores = []
    for s in score_data:
        if(s["name"].lower() == player_name.lower()):
            player_scores.append(s)

    print(f"\n--- {player_name.upper()}'S STATS ---")
    if player_scores:
        p_games = len(player_scores)
        p_percentages = [s["percentage"] for s in player_scores]
        p_best = max(p_percentages)
        p_avg = sum(p_percentages) / p_games
        p_correct = sum(s["correct"] for s in player_scores)
        p_wrong = sum(s["wrongs"] for s in player_scores)

        print(f"Games Played           : {p_games}")
        print(f"Best Score             : {p_best:.1f}%")
        print(f"Average Score          : {p_avg:.1f}%")
        print(f"Total Correct Answers  : {p_correct}")
        print(f"Total Wrong Answers    : {p_wrong}")
    else:
        print(f"No games recorded for {player_name} yet. Play a quiz to see personal stats!")

    print("==================================================")
    input("\nPress Enter to return to menu...")
            

# Version_7 : Select category ques..
def selected_category(all_categories):

    category_names = list(all_categories.keys())

    while True:
        print(f"======================================\n\tQuiz Menu\n======================================")

        # for idx, category in enumerate(category_names, 1):
        #     print(f"{idx}. {category}")
        
        # Above enumerate func convert into simple for loop..
        for i in range(0,len(category_names)):
            print(f"{i + 1}. {category_names[i]}")

        print(f"0.Exit")

        # choice = input("\nChoose a category (Enter a number): ").strip()
        choice_input = input("\nChoose a category (Enter a number): ").strip()

        # Fix ValueError with exception handling / isdigit validation
        if not choice_input.isdigit():
            print("\n❌ Invalid input! Please enter a valid number.\n")
            continue

        choice = int(choice_input)

        if(choice == 0):
            # print(f"exits !")
            # print(f"Thank you..")
            # exit()
            return None, None    # Go back to main menu

        elif(choice >= 1 and choice <= len(category_names)):
            selected_cat = category_names[choice-1]
            print(f"\nCategory Selected: {selected_cat}\n")
            return selected_cat, all_categories[selected_cat]

        else:
            print(f"Invalid choice! Please select a number between 0 and {len(category_names)}.\n")


# Version 8: Ask for Player Name at application launch and 
# VERSION 10: MAIN MENU & PROGRAM ENTRY
print(f"======================================\n\tPYTHON QUIZ APPLICATION\n======================================")
player_name = input("Enter your name: ").strip()

while True:

    print(f"\n======================================\n\tMAIN MENU\n======================================")
    print(f"Welcome, {player_name}!\n")
    print("1. 🎮 Start Quiz")
    print("2. 🏆 Leaderboard")
    print("3. 📊 Statistics")
    print("0. ❌ Exit")

    menu_choice = input(f"\nChoose an option :").strip()

    if(menu_choice == "1"):
        cat_name, selected_questions = selected_category(diff_questions_category)

        if(selected_questions is None):
            continue  # User selected 0 (Back to Main Menu)

        # Time limit per question set to 10 seconds (changeable as needed)
        quiz_obj = Quiz(player_name, cat_name, selected_questions, 0, 0, 0, "", time_limit=10)
        quiz_obj.welcome()

        quiz_obj.run_quiz_loop()

        # Loop specifically for asking play again until valid answer
        while True:
            again_play_choice = input("Do you want to play again (Y/N):")

            if(again_play_choice == "Y" or again_play_choice == "y"):
                break  # Break inner loop to let outer while loop run run_quiz_loop() again

            elif(again_play_choice == "N" or again_play_choice == "n"):
                print(f"exits !")
                print(f"Thank you..")
                exit()  # Stops the program cleanly

            else:
                print(f"enter from these Y / N.")

    elif(menu_choice == "2"):
        show_leaderboard(diff_questions_category)

    elif(menu_choice == "3"):
        show_statistics(player_name)

    elif(menu_choice == "0"):
        print(f"\nExiting application... Thank you for playing!")
        exit()

    else:
        print(f"\n❌ Invalid choice! Please select 1, 2, 3, or 0.")
