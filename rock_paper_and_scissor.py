import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'player'
    else:
        return 'computer'

def play_round():
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            break
        print("Invalid choice, please try again.")
        
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    winner = get_winner(player_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'player':
        print("You win this round!")
    else:
        print("Computer wins this round!")

    return winner

def play_game():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while player_score < 2 and computer_score < 2:
        winner = play_round()
        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        print(f"Score - You: {player_score}, Computer: {computer_score}\n")

    if player_score == 2:
        print("Congratulations! You won the best-of-three game!")
    else:
        print("The computer won the best-of-three game. Better luck next time!")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
