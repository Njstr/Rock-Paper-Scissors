import random
import time

print("Welcome to the game!")
time.sleep(0.6)
print("You have 4 chances to play")
time.sleep(0.6)
print("The player scoring 4 points will win")
time.sleep(0.6)

user_Score = 0
computerScore = 0
chances = 4

while True:
    if chances <= 4 and computerScore <= 3 and user_Score <= 3:
        def game():
            global user_Score
            global computerScore
            global chances

            list = ["Rock", "Paper", "Scissor"]
            a = random.choice(list)

            user = str(input("Enter one choice(Rock, Paper, Scissor): "))
            time.sleep(0.6)
            print(f"Computer's choice: {a}")

            if user == "Rock" and a == "Paper":
                computerScore += 1
                time.sleep(0.6)
                print("Computer won. Score: ", computerScore)
                chances = chances - 1
                time.sleep(0.6)
                print(f"You have {chances} chance(s) left")
                if chances <= 0 and computerScore == 4:
                    print("Oops!! You lost it!😥")
                    return

            elif a == "Rock" and user == "Paper":
                user_Score += 1
                time.sleep(0.6)
                print("You won. Your Score: ", user_Score)
                if user_Score == 4:
                    time.sleep(0.6)
                    print("Yeyyy, You won the game!!!😍")
                    return

            elif user == "Paper" and a == "Scissor":
                computerScore += 1
                time.sleep(0.6)
                print("Computer won. Score: ", computerScore)
                chances = chances - 1
                time.sleep(0.6)
                print(f"You have {chances} chance(s) left")
                if chances <= 0 and computerScore == 4:
                    time.sleep(0.6)
                    print("Oops!! You lost it!😥")
                    return   

            elif a == "Paper" and user == "Scissor" :
                user_Score += 1
                time.sleep(0.6)
                print("You won. Your Score: ", user_Score)
                if user_Score == 4:
                    time.sleep(0.6)
                    print("Yeyyy, You won the game!!!😍 ")
                    return

            elif user == "Scissor" and a == "Rock":
                computerScore += 1
                time.sleep(0.6)
                print("Computer won. Score: ", computerScore)
                chances = chances - 1
                time.sleep(0.6)
                print(f"You have {chances} chance(s) left")
                if chances <= 0 and computerScore == 4:
                    print("Oops!! You lost it!😥")
                    return

            elif a == "Scissor" and user == "Rock":
                user_Score += 1
                time.sleep(0.6)
                print("You won. Your Score: ", user_Score)
                if user_Score == 4:
                    time.sleep(0.6)
                    print("Yeyyy, You won the game!!!😍")
                    return

            if user == a:
                time.sleep(0.6)
                print("It's a tie 😬")

        game()

    else:
        break

print("Thank you for playing!!;)")
