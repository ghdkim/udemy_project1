import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


# Create a deal_card() function that uses the List below to *return* a random card.
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Create a function called calculate_score() that takes a List of cards as input and returns the score
def calculate_score(cards):
    """Take a list of cards and return the score"""
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "Bust. You lose!"
    if comp_score == user_score:
        return "Draw!"
    elif comp_score == 0:
        return "Computer got a blackjack! You lose!"
    elif user_score == 0:
        return "You got a blackjack! You win!"
    elif user_score > 21:
        return "Bust. You lose!"
    elif comp_score > 21:
        return "Computer went over. You win!"
    elif user_score > comp_score:
        return "You win!"
    else:
        return "You lose!"

def play_blackjack():
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        print(logo)
        """The score will need to be rechecked with every new card drawn"""
        # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        print (f"   Your cards: {user_cards}, current score: {user_score}")
        print (f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True

        # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            draw_another = input("Type 'yes' if you would like to draw another card. Type 'no' if not: ").lower()
            if draw_another == 'yes':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f"    Your final hand is {user_cards}, final score: {user_score}")
    print(f"    Computer final hand is {computer_cards}, final score: {comp_score}")
    result = compare(user_score,comp_score)
    print(result)

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while True:
    play_blackjack()

    again = input("Do you want to restart the game? Type 'yes' to restart, type 'no' to exit ").lower()
    if again != "yes":
        break