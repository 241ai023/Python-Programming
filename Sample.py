import random as rd


# def get_choices():
#     option = ['rock', 'paper', 'scissor']
#     player_choice = input("Enter your choice rock paper scissor:")
#     computer_choice = rd.choice(option)
#     result = {"player": player_choice, 'computer': computer_choice}
#     return result

my_score = 0
com_score = 0


def check_win(player, computer):
    global my_score
    global com_score
    print(f"you chose {player} computer chose {computer}")
    if player == computer:
        return "It is tie"
    elif player == "rock":
        if computer == "scissor":
            my_score += 1
            return "rock smashes scissor! you win!"
        else:
            com_score += 1
            return "paper covers rock! you loss"

    elif player == "paper":
        if computer == "rock":
            my_score += 1
            return "paper covers rock!you win!"
        else:
            com_score += 1
            return "scissor cuts paper! you loss"

    elif player == "scissor":
        if computer == "paper":
            my_score += 1
            return "scissor cuts paper! you win!"
        else:
            com_score += 1
            return "rock smashes scissor! you loss"


# choice = get_choices()

# result = check_win(choice['player'], choice['computer'])
# print(result)
print("if you close the game type exit")
while True:
    player_choice = input("Enter your choice rock paper scissor :")
    option = ["rock", "paper", "scissor"]
    computer_choice = rd.choice(option)
    if player_choice == "exit" or player_choice == "0":
        print(f"Final score: you {my_score} : computer {com_score}")
        if my_score >= com_score:
            print("You win the match.")
        else:
            print("You loss the match")
        break
    else:
        result = check_win(player_choice, computer_choice)
        print(result)
