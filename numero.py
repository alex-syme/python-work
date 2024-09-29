import random

def guessChecker(guess, word):
    result = []
    for x in range(len(guess)):
        if guess[x] == word[x]:
            result.append("Green")
        elif guess[x] in word:
            result.append("Yellow")
        else:
            result.append("Gray")
    return result

words = ["apple", "bread", "chair", "dance", "earth", "flame", "grape", "heart", "ideal", "jolly", "kneel", "liver", "mango", "nerve", "ocean", "piano", "quill", "river", "space", "table", "uncle", "vivid", "water", "xenon", "yacht", "zebra", "angel", "beach", "cabin", "drink", "eagle", "fable", "globe", "horse", "input", "jelly", "knack", "lunar", "melon", "noble", "oasis", "petal", "quick", "royal", "snake", "tiger", "unity", "vocal", "whale", "xylem", "yield", "zesty", "amber", "blend", "climb", "dwarf", "event", "forge", "glade", "hinge", "inbox", "jolly", "karma", "laser", "magic", "niche", "olive", "pearl", "quiet", "rebel", "scale", "tulip", "ultra", "vigor", "wharf", "xenon", "yeast", "zonal", "alley", "bliss", "creep", "daisy", "elite", "frost", "grasp", "haunt", "inlet", "jazzy", "knock", "lemon", "moody", "novel", "onion", "purse", "quote", "ridge", "shear", "tough", "upset", "vixen"]
maxAttempts = 6
attempts = 0
word = random.choice(words)


print("Welcome to Alex's word guessing game! Try and guess the 5 letter word.")

for attempt in range(maxAttempts):
    guess = str(input(f"Attempt {attempt + 1}/{maxAttempts}: ")).lower()
    if len(guess) != 5:
        print("Please enter a 5 letter word.")
    continue

    feedback = guessChecker(guess, word)
    print("Result: ", feedback)

    if guess == word:
        print("Congrats, you got the word correct.")
        break
else:
    print(f"Sorry, you've used all attempts. The word was: {word}")

    