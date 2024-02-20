from advent.day04 import shared


def main():
    cards = [CardType(card_description) for card_description in shared.parse_input()]
    deck = Deck(cards)
    print("total number of cards is: ", deck.score())


class CardType:
    def __init__(self, card_description):
        self.id = card_description[0]
        self.amount = 1
        self.winning_numbers = card_description[1]
        self.extracted_numbers = card_description[2]

    def add_copies(self, amount):
        self.amount += amount

    def score(self):
        cards_acquired = []
        matches = shared.count_matches(
            (None, self.winning_numbers, self.extracted_numbers)
        )
        for id in range(self.id + 1, self.id + matches + 1):
            cards_acquired.append((id, self.amount))
        return cards_acquired


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def __get_card(self, id):
        return self.cards[id - 1]

    def score(self):
        total_score = 0
        for card in self.cards:
            total_score += card.amount
            cards_acquired = card.score()
            for card_id, amount in cards_acquired:
                self.__get_card(card_id).add_copies(amount)
        return total_score
