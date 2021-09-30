'''
Create a program to help the user type faster. Give him a word and ask him to write it five times.
Check how many seconds it took him to type the word at each round.

In the end, tell the user how many mistakes were made and show a chart with the
typing speed evolution during the 5 rounds.
'''
import time as t
import matplotlib.pyplot as plt
word = "Polymorphism"
i = 1
times = []
mistakes = 0
print("This program will help you to type faster. You will have to type the word 'Polymorphism' as fast as you can for five times")
input("Press enter for continue...")
while i<=5:
    startTime = t.time()
    userInput = input("Write a "+ word + ": ")
    end = t.time()
    time_elapsed = end - startTime
    times.append(time_elapsed)
    if(userInput.lower() != "polymorphism"):
        mistakes += 1
    i += 1

print(f"you made {mistakes} mistakes")
print("Now let's see your evolution")
t.sleep(3)
x = [1,2,3,4,5]
y = times
legend = ['1','2','3','4','5']
plt.xticks(x,legend)
plt.xlabel("Attempts")
plt.ylabel("Times in Seconds")
plt.title("Your Typing Evolution")
plt.plot(x,y)
plt.show()