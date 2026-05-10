import random
word_list = ["instagram", "telegram", "youtube", "snapchart", "whatsapp","facebook"]

word_to_guess = random.choice(word_list)
word_length = len(word_to_guess)

display = ["_"] * word_length
incorrect_guesses = 0
max_incorrect = 6
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(display))  

while incorrect_guesses < max_incorrect and "_" in display:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(f"Good job! '{guess}' is in the word.")
        
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                display[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Sorry, '{guess}' is not in the word. Incorrect guesses: {incorrect_guesses}/{max_incorrect}")

    
    print(" ".join(display))

if "_" not in display:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game over! The word was:", word_to_guess)
