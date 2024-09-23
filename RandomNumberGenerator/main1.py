import random

print('''
   _____ _    _ ______  _____ _____   _______ _    _       _______   _   _ _    _ __  __ ____  ______ _____  _ 
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |   /\|__   __| | \ | | |  | |  \/  |  _ \|  ____|  __ \| |
 | |  __| |  | | |__  | (___| (___      | |  | |__| |  /  \  | |    |  \| | |  | | \  / | |_) | |__  | |__) | |
 | |  |_| |  | |  __|   \___ \\___ \     | |  |  __  | / /\ \ | |    | . ` | |  | | |\/| |  _ <|  __| |  _  /| |
 | |__| | |__| | |____ ____) |___) |    | |  | |  | |/ ____ \| |    | |\  | |__| | |  | | |_) | |____| | \ \|_|
  \_____|\____/|______|_____/_____/     |_|  |_|  |_/_/    \_\_|    |_| \_|\____/|_|  |_|____/|______|_|  \_(_)
                                                                                                               
                                                                                                               
''')


given_num=random.randint(0,100)
chances=0
print("Welcome to 'GUESS THAT NUMBER'")
ans=input("Choose Difficulty 'easy' or 'hard'")
if ans=="easy":
    chances=10
elif ans=="hard":
    chances=5
else:
    print("Invalid Choice")
    
while chances > 0:
    choice = int(input(f"Guess the number (Chances left: {chances}): "))
    
    if choice == given_num:
        print("Correct Answer! You win!")
        break
    elif choice > given_num: 
        print("Too high")
    else:
        print("Too low")
    chances -= 1

    if chances == 0:
        print(f"You lost, try again. The correct answer was {given_num}")
    