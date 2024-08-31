import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw(hand):
    hand.append(random.choice(cards))


def calculate_score(hand):
    """Calculate the score of a given hand."""
    score = sum(hand)

    # Adjust for Ace (11) if the score exceeds 21
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score


def blackjack():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print("\n" * 20)

    if play == 'y':
        print(art.logo)

        player_hand = []
        cpu_hand = []

        draw(player_hand)
        draw(player_hand)
        draw(cpu_hand)

        game_over = False

        while not game_over:
            player_score = calculate_score(player_hand)
            cpu_score = calculate_score(cpu_hand)

            print(f"Your cards: {player_hand}, current score: {player_score}\n"
                  f"Computer's first card: {cpu_hand[0]}")

            if player_score == 21:
                print("Blackjack! You win!")
                game_over = True
            elif player_score > 21:
                print("You went over 21. You lose!")
                game_over = True
            else:
                redraw = input("Type 'y' to get another card, type 'n' to pass: ")
                if redraw == "y":
                    draw(player_hand)
                else:
                    while cpu_score < 17:
                        draw(cpu_hand)
                        cpu_score = calculate_score(cpu_hand)

                    print(f"Your final hand: {player_hand}, final score: {player_score}\n"
                          f"Computer's final hand: {cpu_hand}, final score: {cpu_score}")

                    if cpu_score > 21 or player_score > cpu_score:
                        print("You win!")
                    elif player_score == cpu_score:
                        print("Draw")
                    else:
                        print("You lose")

                    game_over = True

        blackjack()
    else:
        print("Thanks for playing! Goodbye!")


blackjack()
