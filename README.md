Number Guessing Game Project Report
Overview

For this project, I created a single-player number guessing game that runs in the terminal using Python. The main idea is that the computer randomly generates a number, and the user has to guess it based on feedback after each attempt. Even though the concept is pretty simple, it actually uses a lot of the core ideas we’ve been learning in class, like loops, conditionals, functions, and input handling. This project was a good way to practice putting everything together into one working program instead of just small pieces.

Program Structure and Flow

I organized the program into functions to keep things cleaner and easier to follow. There is a main function that controls the overall flow of the game, and another function that runs a single round. This way, the code isn’t all in one place, and it’s easier to understand what each part is doing. It also makes it easier to add features like replaying the game without rewriting everything.

When the program starts, the user is asked to choose a difficulty level: easy, medium, or hard. Each difficulty changes both the range of numbers and the number of attempts the user gets. For example, easy mode uses a smaller range and gives more attempts, while hard mode increases the range and gives fewer attempts. I added this because it makes the game more interesting and gives the user some control over how challenging it is.

After the user selects a difficulty, the program generates a random number using random.randint(). Then the game loop starts, where the user keeps entering guesses until they either guess correctly or run out of attempts.

Feedback and User Interaction

One of the most important parts of the game is the feedback after each guess. After the user enters a guess, the program compares it to the correct number and responds accordingly. If the guess is too high, it tells the user to guess lower. If it’s too low, it tells them to guess higher. If the guess is correct, it prints a congratulations message and ends the round.

This feedback is what makes the game actually playable, because it guides the user toward the correct answer instead of just guessing randomly. It also makes the game feel more interactive instead of just input/output.

Input Validation

I also made sure to include input validation so the program doesn’t crash if the user enters something invalid. Before converting the input to an integer, the program checks if the input is a number. If the user types something like letters or symbols, the program prints a message asking them to enter a valid number and then continues the loop. This was important because without it, the program would throw an error and stop running.

Attempt Tracking and Limits

Another key feature is tracking the number of attempts. Every time the user makes a guess, the program increases a counter. It also shows how many attempts are left after each guess, which helps the user keep track of their progress. If the user guesses the number correctly, the program shows how many attempts it took. If they run out of attempts, the game ends and reveals the correct number.

Adding a limit on attempts makes the game more challenging and gives it more of a goal. Without a limit, the user could just keep guessing forever, which wouldn’t be as interesting.

Extra Features and Improvements

To go beyond the basic requirements, I added a few extra features. The main ones are difficulty levels, limited attempts, and a replay option. The replay option lets the user play multiple rounds without restarting the program, which makes it more convenient and feel more like a complete game.

These features weren’t too complicated to add, but they made a big difference in how the game feels. It made the project more interactive and less like a basic assignment.

Challenges and What I Learned

One of the main challenges was getting the loop structure right so the game runs correctly in all situations. I had to make sure the loop continues when it should and stops at the right time, like when the user guesses correctly or runs out of attempts. Another challenge was handling invalid input without breaking the program.

Working through these issues helped me understand how control flow works in Python, especially how loops and conditionals interact. I also got more comfortable organizing code into functions and writing code that is easier to read and follow.

Conclusion

Overall, this project was a good way to apply what I’ve learned so far in Python. Even though the game itself is simple, it uses a lot of important programming concepts all at once. Adding features like difficulty levels and replay made it more engaging and showed how small improvements can make a program feel more complete. This project definitely helped me feel more confident in writing and structuring programs, and it gave me a better understanding of how everything fits together.h the idea is simple, it covers a lot of important skills like loops, conditionals, and user input. Adding extra features like difficulty levels and replay also made it more fun and interactive.
