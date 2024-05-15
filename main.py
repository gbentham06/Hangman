from random import choice
import re


# finds the indexes of all correct letters
def matches(letter, string):
    return [m.start() for m in re.finditer(letter, string)]


# runs the main game loop
def game(target) -> bool:
    # makes a line of underscores to represent the unknown word and sets up guesses
    base = ['_' for i in target]
    guesses = int(input("how many guesses? "))
    while True:
        print(f'{guesses} guesses left')
        print(''.join(base))
        guess = input()[0]
        # guard clause for no matches & loss condition
        if not matches(guess, target):
            guesses -= 1
            if guesses <= 0:
                return False
        # replaces underscores with correctly guessed letters & win condition
        for i in matches(guess, target):
            base[i] = guess
        if ''.join(base) == target:
            return True


# main branch for setup and driving code as well as conclusion
def main() -> None:
    # formats words into list & uses a random one for the game
    with open("words.txt") as f:
        wordlist = [i.rstrip() for i in f.readlines()]
    while True:
        target = choice(wordlist)
        # runs game
        win = game(target)
        print(f"word was: {target}")
        # handles win & loss
        if win:
            print("yay")
        else:
            print("wamp wamp")
        # checks if user would like to play again, iterates if so
        if input("go again? (y/n): ") == 'n':
            break


if __name__ == '__main__':
    main()
