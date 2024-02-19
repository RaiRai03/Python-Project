import random

def spin_reels():
    reel1 = random.randint(1, 9)
    reel2 = random.randint(1, 9)
    reel3 = random.randint(1, 9)
    return reel1, reel2, reel3

def check_win(reel1, reel2, reel3):
    if reel1 == reel2 == reel3:
        return True
    else:
        return False

def main():
    while True:
        print("Welcome to the Slot Machine!")
        reel1, reel2, reel3 = spin_reels()
        print("Reel 1:", reel1)
        print("Reel 2:", reel2)
        print("Reel 3:", reel3)
        if check_win(reel1, reel2, reel3):
            print("CONGRATULATIONS! You won!")
        else:
            print("SORRY! You lost!")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

main()