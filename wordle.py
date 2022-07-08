import random
from words import word_list

letters_not = []
display = []
CORRECT_ANSWER = False
random_word = random.choice(word_list[0])

for position in random_word:
    display += '-'


def check_letter(word_guess):
    for n in range(len(random_word)):
        for letter in word_guess:
            if word_guess[n] == random_word[n]:
                display[n] = guess[n]
            elif letter in random_word and word_guess[n] != random_word[n]:
                letters_not.append(letter)
    return True


amount_of_guesses = 6
while amount_of_guesses != 0:
    guess = input("Enter a word: ")

    if guess == random_word:
        print(f"Congrats, you won, the word was {random_word}")
        CORRECT_ANSWER = True
        break

    elif len(guess) != 5:
        print("Please enter a 5 letter word.")

    else:
        amount_of_guesses -= 1
        new_letters = []
        check_letter(guess)

        # check if letter is in word but not in right spot.
        for i in letters_not:
            if i not in new_letters:
                new_letters.append(i)

            if i in display and new_letters:
                new_letters.remove(i)
        # if new_letters list is NOT empty - display the letters.
        if new_letters != []:
            print(f"You have these letters correct, but not in the right spot: {new_letters}")
        print(''.join(display))

try:
    with open('wordle_stats.txt', 'r') as stats:
        for line in stats:
            data = line.split()
            try:
                played = int(data[1])
                current_streak = int(data[9])
                max_streak = int(data[13])
            except IndexError:
                pass
            if CORRECT_ANSWER:
                played += 1
                current_streak += 1
                win_percent = round((current_streak / played) * 100)
                max_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak

            else:
                played += 1
                current_streak = 0
                win_percent = round((current_streak / played) * 100)
                max_streak = max_streak

            with open("wordle_stats.txt", "w") as statistics:
                statistics.write(f"Played: {played} | Win Percentage: {win_percent}% | Current Streak: {current_streak} |"
                                 f" Max Streak: {max_streak}")


#this is only if they are running program for the very first time and wordle_stats does not exist.
except NameError:
    if CORRECT_ANSWER:
        with open("wordle_stats.txt", "w") as stats:
            played = 1
            current_streak = 1
            win_percent = 100
            max_streak = current_streak
            stats.write(f"Played: {played} | Win Percentage: {win_percent}% | Current Streak: {current_streak} |"
                                 f" Max Streak: {max_streak}")

    else:
        with open("wordle_stats.txt", "w") as stats:
            played = 1
            current_streak = 0
            win_percent = 0
            max_streak = 0
            stats.write(f"Played: {played} | Win Percentage: {win_percent}% | Current Streak: {current_streak} |"
                        f" Max Streak: {max_streak}")

if CORRECT_ANSWER == False:
    print(f"The word was {random_word}")
