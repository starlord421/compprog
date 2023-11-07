import random

with open('sowpods.txt','r') as f:
    lines = f.readlines()
    words= [word for line in lines for word in line.split()]
    random_word = random.choice(words)
    print("your daily random word is", random_word)