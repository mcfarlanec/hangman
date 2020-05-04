import random
import json

# Simple Hangman Game
# Created by Colin McFarlane
# May 4th, 2020
# Built with english-words json from https://github.com/dwyl/english-words

words_json = 'words_dictionary.json'

# Gets a random word from the json, breaks the word into all its letters
# Player tries to guess the letters in the given word
# If the player gets all the letters before running out of lives they win, otherwise it is game over
def main():
    words = read_dictionary()
    selected_word = random.choice(list(words))
    selected_letters = list(selected_word)
    guessed_letters = []
    player_lives = 6

    print("Welcome to Hangman!")
    print("You have to guess all the letters in the given word.")
    print("You have 6 lives, every incorrect letter will take 1 life away. Good luck!")
    print("\t")

    while set(guessed_letters) != set(selected_letters):
        if player_lives == 0:
            print("You have run out of lives!")
            print("The word was:", selected_word)
            print("Game Over.")
            break
        else:

            print("Current lives:", player_lives)

            out_word = []
            for letter in selected_letters:
                if letter in guessed_letters:
                    out_word.append(letter)
                else:
                    out_word.append("_")
            print(*out_word)

            while 1:

                guess = input("Guess a letter: ")
                print("\t")

                if len(guess) > 1:
                    print("Guess not a letter try again.")

                elif guess in guessed_letters:
                    print("Already guessed that letter. Try again.")

                elif guess in selected_letters:
                    print("Valid letter.")
                    guessed_letters.append(guess)
                    print("\t")
                    break

                else:
                    print("Letter not in word.")
                    player_lives = player_lives - 1
                    guessed_letters.append(guess)
                    print("\t")
                    break

    if player_lives > 0:
        print(*selected_letters)
        print("\t")
        print("Congratulations! You correctly guessed the word!")

    print("You have", player_lives, "lives left. Play again?")
    play_again = input("y/n : ")
    if play_again == "y":
        main()


# Reads the json and returns all the words in a dictionary
def read_dictionary():
    with open(words_json) as json_file:
        words = json.load(json_file)
    return words


if __name__ == '__main__':
    main()
