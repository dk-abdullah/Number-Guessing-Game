import random
correct = random.randint(1,100)
guess = int(input("Guess a number: "))
counter = 1
while guess != correct:
    if guess > correct:
        print("Guess Lower")
    else:
        print("Guess Higher")
    
    guess = int(input("Guess Again: "))
    counter +=1
print("Correct guess")
print("You took", counter ,"attempts")