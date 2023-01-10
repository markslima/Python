import random
from art import logo

def cls():
    print("\n" * 20)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    ''' Take a LIST of cards and return the score calculated from SUM of cards
    '''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😭"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, computer has BlackJack 😭"
    elif user_score == 0:
        return "BlackJack! You win! 😎"
    elif user_score > 21:
        return "You went over 21. You lose! 😫"
    elif computer_score > 21:
        return "Computer went over 21. You win! 😃"
    elif user_score > computer_score:
        return "You win! 😎"
    elif computer_score > user_score:
        return "You bet your family's savings, and now you have lost everything. 😖"

def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, or type 'n' to hold: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score is {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? 'y' or 'n' :") == 'y':
    cls()
    play_game()

