"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card:str) -> int:
    if card in ('J','Q','K'):
        return 10
    if card == 'A':
        return 1
    return int(card)
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    pass


def higher_card(card_one: str, card_two: str):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    if v1 > v2:
        return card_one
    if v2 > v1:
        return card_two
    return (card_one, card_two)
    
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    pass

def _value_for_ace_logic(card: str) -> int:
    """Helper: returns standard value, Ace counted as 11 for ace-logic only."""
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 11  # only for ace evaluation
    return int(card)

def value_of_ace(card_one: str, card_two: str) -> int:
    """
    Decide whether the new Ace (A) should count as 1 or 11,
    based on the best total ≤ 21 with the current two cards.
    """
    # If there's already an Ace, the new Ace must be 1
    if card_one == 'A' or card_two == 'A':
        return 1

    current_total = _value_for_ace_logic(card_one) + _value_for_ace_logic(card_two)

    # Try Ace as 11 first
    if current_total + 11 <= 21:
        return 11
    return 1
    
    
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Return True if the two cards form a blackjack (A + 10/J/Q/K)."""
    ten_cards = {'10', 'J', 'Q', 'K'}
    return ((card_one == 'A' and card_two in ten_cards) or
            (card_two == 'A' and card_one in ten_cards))
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Return True if both cards have equal value (including any two 10-value cards)."""
    tens = {'10', 'J', 'Q', 'K'}
    if card_one in tens and card_two in tens:
        return True
    return card_one == card_two



def can_double_down(card_one: str, card_two: str) -> bool:
    """
    Return True if the two-card total is 9, 10, or 11,
    treating Ace as 1 to match exercise examples.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)

    pass
