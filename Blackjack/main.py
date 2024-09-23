import random

def deal_card():
    # Returns a random card from deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # Check for a blackjack (a hand with only 2 cards that sums to 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents a blackjack

    # Adjust for ace if the hand is over 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Dealer has blackjack. You lose."
    elif user_score == 0:
        return "You have blackjack! You win!"
    elif user_score > 21:
        return "You went over. You lose."
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins!"

# Game setup
user_cards = []
dealer_cards = []
is_game_over = False

# Deal 2 cards to each player
for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print("Your cards:", user_cards, "Current score:", user_score)
    print("Dealer's first card:", dealer_cards[0])

    # Check for blackjack or bust
    if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        # Ask the user if they want to take another card
        should_continue = input("Do you want to draw another card? Type 'y' or 'n': ")
        if should_continue == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

# Dealer's turn: dealer keeps drawing until score is at least 17
while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

print("Your final hand:", user_cards, "Final score:", user_score)
print("Dealer's final hand:", dealer_cards, "Final score:", dealer_score)
print(compare(user_score, dealer_score))
