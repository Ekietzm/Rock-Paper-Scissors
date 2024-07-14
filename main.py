import random


def main():
    game_loop = True

    while game_loop:

        rock = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
        
        paper = '''
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)
        '''
        
        scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''

        choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
        if choice == "0":
            choice = rock
        elif choice == "1":
            choice = paper
        elif choice == "2":
            choice = scissors
        else:
            print(f"Error. {choice} is an invalid choice.")

        comp_choice = random.randint(0, 2)

        if comp_choice == 0:
            comp_choice = rock
        elif comp_choice == 1:
            comp_choice = paper
        elif comp_choice == 2:
            comp_choice = scissors
        else:
            print(f"Error. {comp_choice} is an invalid choice.")

        if choice == rock and comp_choice == rock:
            print(rock)
            print('Player1 chose: ' + str("rock"))
            print(rock)
            print('Player2 chose: ' + str("rock"))
            print("Tie!")
        elif choice == rock and comp_choice == paper:
            print(rock)
            print('Player1 chose: ' + str("rock"))
            print(paper)
            print('Player2 chose: ' + str("paper"))
            print("You Lose!")
        elif choice == rock and comp_choice == scissors:
            print(rock)
            print('Player1 chose: ' + str("rock"))
            print(scissors)
            print('Player2 chose: ' + str("scissors"))
            print("You Win!")
        elif choice == paper and comp_choice == rock:
            print(paper)
            print('Player1 chose: ' + str("paper"))
            print(rock)
            print('Player2 chose: ' + str("rock"))
            print("You Win!")
        elif choice == paper and comp_choice == paper:
            print(paper)
            print('Player1 chose: ' + str("paper"))
            print(paper)
            print('Player2 chose: ' + str("paper"))
            print("Tie!")
        elif choice == paper and comp_choice == scissors:
            print(paper)
            print('Player1 chose: ' + str("paper"))
            print(scissors)
            print('Player2 chose: ' + str("scissors"))
            print("You Lose!")
        elif choice == scissors and comp_choice == rock:
            print(scissors)
            print('Player1 chose: ' + str("scissors"))
            print(rock)
            print('Player2 chose: ' + str("rock"))
            print("You Lose!")
        elif choice == scissors and comp_choice == paper:
            print(scissors)
            print('Player1 chose: ' + str("scissors"))
            print(paper)
            print('Player2 chose: ' + str("paper"))
            print("You Win!")
        elif choice == scissors and comp_choice == scissors:
            print(scissors)
            print('Player1 chose: ' + str("scissors"))
            print(scissors)
            print('Player2 chose: ' + str("scissors"))
            print("tie!")

        play_again = input("Play again? (y/n)")
        if play_again.lower() == "y" or play_again.lower() == "yes":
            game_loop = True
        else:
            game_loop = False


if __name__ == '__main__':
    main()
