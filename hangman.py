print("welcome to hangman")
word="nerd"
guessed_letters=[]
guesses=1
def desplay_clue(word, guessed_letters):
    clue=""
    for letter in word:
        if letter.lower() in guessed_letters or letter.upper() in guessed_letters:
            clue += letter
            print(clue)
        else: 
            print("____ ")
               
while True:
    desplay_clue(word,guessed_letters)
    guess=input("what is your guessed letter ").upper()
    if guess in guessed_letters:
        print("you've guessed that already")
        #continue   
    guessed_letters.append(guess)
    if all (letter.lower() in guessed_letters or letter.upper() in guessed_letters for letter in word):
        print("if you got this far, you are one")
        break