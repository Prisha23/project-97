Number guessing game
Guess a number (between 1 to 9):
 Enter your guess:- 3
 Your guess was too low: Guess a number higher than 3
 Enter your guess:- 4
 Your guess33 was too low: Guess a number higher than 4
 Enter your guess:- 7
 Your guess was too low: Guess a number higher than 7
 Enter your guess:- 9
 while chances < 5:
     if guess == number:
         print("Congratulations YOU WON!!!")
         break
     if not chances < 5:
        print("YOU LOSE!!! the number is", number)