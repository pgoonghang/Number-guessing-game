import random
import os
import time
import platform

# Maximum number to include in guessing game
# Default is set to include numbers from 1 to 1,000
#
# To use numbers from 1 to 1,000,000 for example, change to: max_num = 1_000_000
#
OK_GREEN = '\033[92m'
FAIL_RED = '\033[91m'
ENDC = '\033[0m'

max_num = 1_000
current_platform = platform.system()

# Scratch file location for tracking winning streak
scratch_file = "./tally.scratch"

correct_responses = ["あたり", "正しい", "よくできました", "すごいね", "正解", "御名答"]
incorrect_responses = ["おしい", "残念", "違う", "不正解", "間違い", "誤り", "違います"]

guess, tally = None, 0

def say(str):
    if (current_platform == 'Darwin'):
        str = "say -v kyoko " + str
    # TODO: And command for window/linux users https://wiki.freepascal.org/espeak
    # else:
    #     str = "espeak"
    os.system(str)
    return

if os.path.isfile(scratch_file):
    with open(scratch_file, "r") as f:
        tally = f.read()
    tally = int(tally)    

os.system("clear")

input("""This program will help you improve your listening comprehension with Japanese numbers.
You will hear a number spoken in Japanese, and then be asked to type in the number.
Type your answer using the traditional western numbers (0-9). Type 'q' to quit.

Make sure your sound is turned on and press ENTER  to begin: """)
print()

while True:
    num = random.randint(1, max_num)
    say(str(num))
    guess = input("Type your answer or 'q' to quit: ")
    if guess == "q":
        with open(scratch_file, "w") as f:
            f.write(str(tally))
        break
    elif int(guess) == num:
        say(random.choice(correct_responses))
        tally += 1
        print(f"{OK_GREEN}correct number: {num} your guess: {guess}{ENDC}\n")
    else:
        say(random.choice(incorrect_responses))
        tally = 0
        print(f"{FAIL_RED}correct number: {num} your guess: {guess}{ENDC}\n")

    print(f"Streak: {tally}\n")
    time.sleep(1)
