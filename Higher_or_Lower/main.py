from game_data import data
import random

def format_data(account):
    """Formats the data."""
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_des}, from {account_country}"

def check(user_guess, ceb1_followers, ceb2_followers):
    """Checks if the user's guess is correct."""
    if ceb1_followers > ceb2_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"
    
score = 0
should_game_continue = True
ceb2 = random.choice(data)

while should_game_continue:
    # randomly selecting two people from data
    ceb1 = ceb2
    ceb2 = random.choice(data)
    
    # checking ig ceb1 and ceb2 are not same
    while ceb1 == ceb2:
        ceb2 = random.choice(data)
        
    print(f"Compare A: {format_data(ceb1)}")
    print("Vs")
    print(f"Against B: {format_data(ceb2)}")  

    # User input
    choice = input("Which one has more followers? Type 'A' or 'B': ").upper()
    
    #user input
    while choice not in ['A', 'B']:
        print("Invalid choice! Please choose 'A' or 'B'.")
        choice = input("Which one has more followers? Type 'A' or 'B': ").upper()
    
    # Comparing follower counts
    ceb1_followers = ceb1["follower_count"]
    ceb2_followers = ceb2["follower_count"]

    correct = check(choice, ceb1_followers, ceb2_followers)

    if correct:
        score += 1
        print(f"You are right! Your score is {score}")
    else:
        print(f"You are wrong! {format_data(ceb1)} has {ceb1_followers} followers, and {format_data(ceb2)} has {ceb2_followers} followers.")
        print(f"Your final score is {score}")
        should_game_continue = False
