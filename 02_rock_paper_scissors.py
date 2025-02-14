import random

def AI_move():
    return random.choice(["rock","paper","scissors"])

def game(score_AI=0, score_player=0):
    valid_choices = ["rock", "paper", "scissors"]
    
    while True:
        player_move = input("What's your move? (rock/paper/scissors): ").lower()
        if player_move in valid_choices:
            break
        print(f"Your choice {player_move} is invalid, please ensure you select from the list (rock/paper/scissors)")

    AI_choice = AI_move()
    print(f"AI chose {AI_choice}")
    if (AI_choice == "rock" and player_move == "scissors") or (AI_choice == "paper" and player_move == "rock") or (AI_choice == "scissors" and player_move == "paper"):
        print("AI wins this round!")
        score_AI += 1
    elif (AI_choice == "rock" and player_move == "paper") or (AI_choice == "paper" and player_move == "scissors") or (AI_choice == "scissors" and player_move == "rock"):
        print("You win this round!")
        score_player += 1
    else:
        print("You both chose the same - noone wins the round")
    print(f"Your score is {score_player}, AI score is {score_AI}")
    play_again = input("Do you wish to continue playing? (y/n)").lower()
    if play_again == "y":
        game(score_AI,score_player)
    else:
        print("Thanks for playing!")

game()
