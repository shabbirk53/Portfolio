import random

# Define the Card class
class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return f"{self.color} {self.number}"

    def __repr__(self):
        return f"Card({self.color}, {self.number})"


class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        colors = ["red", "blue", "green", "yellow"]
        for color in colors:
            for number in range(1, 11):
                self.cards.extend([Card(color, number)] * 2)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_cards(self, count):
        drawn = []
        for _ in range(min(count, len(self.cards))):
            drawn.append(self.cards.pop())
        return drawn


class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.hand = []
        self.is_computer = is_computer

    def add_cards(self, cards):
        if len(self.hand) + len(cards) <= 20:
            self.hand.extend(cards)
            return True
        return False

    def remove_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return True
        return False


class GameManager:
    def __init__(self):
        self.deck = Deck()
        self.players = []  #'[[red 1 , red2],[blue 1 ]] '
        self.current_player = 0
        self.actions_this_turn = {"draw": False, "take_card": False}

    def reset_game(self):
        self.deck = Deck()  # Reinitialize the deck
        self.players = []
        self.current_player = 0
        self.actions_this_turn = {"draw": False, "take_card": False}

    def add_players(self, num_players, human_name):
        self.players.append(Player(human_name, False))
        for i in range(num_players - 1):
            self.players.append(Player(f"Notty Bot {i+1}", True))

    def start_game(self):
        print("started")
        self.deck.shuffle()
        for player in self.players:
            player.add_cards(self.deck.draw_cards(5))

    def print_hands(self):
        print("\nCurrent hands:")
        for player in self.players:
            print(f"{player.name}:", [str(card) for card in player.hand])

    def is_valid_group(self, collection):
        if len(collection) < 3:
            return False

        colors = {card.color for card in collection}
        numbers = sorted(card.number for card in collection)

        # Case 1: All cards have the same color and consecutive numbers
        if len(colors) == 1 and all(
            numbers[i] + 1 == numbers[i + 1] for i in range(len(numbers) - 1)
        ):
            return True

        # Case 2: All cards have the same number and different colors
        if len(set(numbers)) == 1 and len(colors) == len(collection):
            return True

        return False

    def find_valid_group(self, cards):
        if len(cards) < 3:
            return None

        colors = [card.color for card in cards]
        numbers = [card.number for card in cards]

        largest_group = []

        # Case 1: Group with the same number and different colors
        for num in sorted(set(numbers)):
            same_number_cards = [card for card in cards if card.number == num]
            if len(same_number_cards) >= 3 and len({card.color for card in same_number_cards}) == len(same_number_cards):
                if len(same_number_cards) > len(largest_group):
                    largest_group = same_number_cards

        # Case 2: Group with the same color and consecutive numbers
        for color in sorted(set(colors)):
            same_color_cards = sorted(
                (card for card in cards if card.color == color), key=lambda x: x.number
            )
            consecutive_group = []
            for i in range(len(same_color_cards)):
                if i == 0 or same_color_cards[i].number == same_color_cards[i - 1].number + 1:
                    consecutive_group.append(same_color_cards[i])
                else:
                    if len(consecutive_group) >= 3 and len(consecutive_group) > len(largest_group):
                        largest_group = consecutive_group
                    consecutive_group = [same_color_cards[i]]
            if len(consecutive_group) >= 3 and len(consecutive_group) > len(largest_group):
                largest_group = consecutive_group

        return largest_group if largest_group else None

    def find_largest_valid_group(self, cards):
        temp_cards = cards.copy()
        largest_group = []

        while True:
            valid_group = self.find_valid_group(temp_cards)
            if valid_group:
                if len(valid_group) > len(largest_group):
                    largest_group = valid_group
                for card in valid_group:
                    temp_cards.remove(card)
            else:
                break

        return largest_group if largest_group else None




    def draw_cards(self, player, count):
        drawn = self.deck.draw_cards(count)
        if player.add_cards(drawn):
            self.actions_this_turn["draw"] = True
            return True
        return False

    def take_random_card(self, from_player, to_player):
        if from_player.hand:
            card = random.choice(from_player.hand)
            if from_player.remove_card(card):
                if to_player.add_cards([card]):
                    self.actions_this_turn["take_card"] = True
                    return True
        return False

    def discard_group(self, player, cards):
        # no need of validating twicw as it is chekd during finding largest valid group
        # if self.is_valid_group(cards):
        for card in cards:
            if not player.remove_card(card):
                return False
        self.deck.cards.extend(cards)
        self.deck.shuffle()
        return True
        # return False

    def handle_computer_turn2(self, computer):
        action_message = f"{computer.name} took an action!"
        print(f"\n{computer.name}'s action:")

        # here i created a list which store 4 actions from
        # which any 1 random choices can be made by computers
        possible_actions = []

        if len(computer.hand) < 20:
            possible_actions.extend(["draw", "take"])

        # this one takes cares of the edge case as if ther
        # is no cards to discard so computer doesnt have options to play discard action
        if self.find_largest_valid_group(computer.hand):
            possible_actions.append("discard")

        # addded for skip
        possible_actions.append("skip")

        if possible_actions:
            action = random.choice(possible_actions)
            if action == "draw":
                draw_count = random.randint(1, 3)
                initial_size = len(computer.hand)
                if self.draw_cards(computer, draw_count):
                    cards_drawn = len(computer.hand) - initial_size
                    action_message = f"{computer.name} drew {cards_drawn} cards"
                    print(f"- Draws {cards_drawn} cards")
            elif action == "take":
                opponents = [p for p in self.players if p != computer]
                target = random.choice(opponents)
                if self.take_random_card(target, computer):
                    action_message = f"{computer.name} stole a card from {target.name}"
                    print(f"- Takes a random card from {target.name}")
            elif action == "discard":
                largest_group = self.find_largest_valid_group(computer.hand)
                if largest_group and self.discard_group(computer, largest_group):
                    action_message = f"{computer.name} discarded {len(largest_group)} cards as a group"
                    print(f"- Discards {len(largest_group)} cards as a group")
            elif action == "skip":
                action_message = f"{computer.name} passed their turn"
                print("- passes turn")

        else:
            print("- Passes turn")
            action_message = f"{computer.name} passed their turn"
            return action_message

        return action_message
    
    def handle_computer_turn(self, computer):
        action_message = f"{computer.name} took an action!"
        
        # Strategy 1: Try to win - check if we can discard cards
        largest_group = self.find_largest_valid_group(computer.hand)
        if largest_group:
            if self.discard_group(computer, largest_group):
                action_message = f"{computer.name} discarded {len(largest_group)} cards as a group"
                return action_message
        
        # Strategy 3: Draw cards if hand is small
        if len(computer.hand) < 12 and not self.actions_this_turn["draw"]:
            draw_count = min(3, 20 - len(computer.hand))
            initial_size = len(computer.hand)
            if self.draw_cards(computer, draw_count):
                cards_drawn = len(computer.hand) - initial_size
                action_message = f"{computer.name} drew {cards_drawn} cards"
                return action_message
            
        # Strategy 2: Steal cards strategically
        if not self.actions_this_turn["take_card"]:
            # Filter opponents with more than 2 cards
            valid_opponents = [p for p in self.players if p != computer and len(p.hand) > 2]
            if valid_opponents:
                target = random.choice(valid_opponents)
                if self.take_random_card(target, computer):
                    action_message = f"{computer.name} stole a card from {target.name}"
                    return action_message
        
        # Strategy 4: Skip turn if no other actions possible
        action_message = f"{computer.name} passed their turn"
        return action_message

    def choose_target_player(self, current_player, choice):
        opponents = [p for p in self.players if p != current_player]
        if len(opponents) == 1:
            return opponents[0]

        print("\nChoose opponent:")
        for i in range(len(opponents)):
            print(f"{i + 1} - {opponents[i].name}")

        while True:
            try:
                if 1 <= choice <= len(opponents):
                    return opponents[choice - 1]
                print("Invalid opponent number, please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def next_turn(self):
        self.current_player = (self.current_player + 1) % len(self.players)
        self.actions_this_turn = {"draw": False, "take_card": False}

    def format_card_list(self, card_objects):
        return [str(card) for card in card_objects.hand]

    def format_deck_list(self, card_objects):
        return [f"{card.color} {card.number}" for card in card_objects]

    def check_winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                return player
        return None


def show_available_actions():
    print("\nAvailable actions:")
    print("1 - Draw cards (1-3)")
    print("2 - Take random card from opponent")
    print("3 - Discard largest valid group")
    print("4 - Pass turn")
    print("5 - Play for me ")


def main():
    game = GameManager()

    while True:
        try:
            num_players = int(input("Enter number of players (2-3): "))
            if 2 <= num_players <= 3:
                break
            print("Please enter 2 or 3")
        except ValueError:
            print("Please enter a valid number")

    player_name = input("Enter your name: ").strip()
    if not player_name:
        player_name = "Human_Player"

    game.add_players(num_players, player_name)
    game.start_game()
    print("\n=== Game Start ===")
    game.print_hands()

    # game starts here after asking number of players and human player name
    while True:
        current_player = game.players[game.current_player]
        print(f"\n=== {current_player.name}'s Turn ===")

        if current_player.is_computer:
            game.handle_computer_turn(current_player)
            game.print_hands()
        else:
            show_available_actions()
            while True:
                choice = input("\nEnter your choice (1-5): ").strip()

                if choice not in ["1", "2", "3", "4", "5"]:
                    print("Invalid choice. Please enter a number between 1-5")
                    continue

                if choice == "1":
                    try:
                        count = int(input("How many cards to draw (1-3)? "))
                        if 1 <= count <= 3:
                            if game.draw_cards(current_player, count):
                                print(f"Drew {count} cards")
                                game.print_hands()
                                break
                            else:
                                print("Cannot draw cards")
                        else:
                            print("Please enter a number between 1 and 3")
                    except ValueError:
                        print("Please enter a valid number")

                # when taking 1 card form random opponent
                elif choice == "2":
                    # opponents = [p for p in game.players if p != current_player]
                    target = game.choose_target_player(current_player)
                    if game.take_random_card(target, current_player):
                        print(f"Took a random card from {target.name}")
                        game.print_hands()
                        break
                    else:
                        print("Cannot take card")

                elif choice == "3":
                    largest_group = game.find_largest_valid_group(current_player.hand)
                    if largest_group:
                        if game.discard_group(current_player, largest_group):
                            print(f"Discarded {len(largest_group)} cards")
                            game.print_hands()
                            break
                        else:
                            print("Cannot discard group")
                    else:
                        print("No valid group to discard")

                elif choice == "4":
                    print("Turn passed")
                    break

                elif choice == "5":
                    print("Playing for you...")
                    possible_actions = ["1", "2", "3", "4"]
                    random_action = random.choice(possible_actions)
                    print(f"Random action chosen: {random_action}")
                    choice = random_action  # Reassign to perform the random action
                    if choice == "1":
                        try:
                            count = random.randint(1, 3)
                            if 1 <= count <= 3:
                                if game.draw_cards(current_player, count):
                                    print(f"Drew {count} cards")
                                    game.print_hands()
                                    break
                                else:
                                    print("Cannot draw cards")
                            else:
                                print("Please enter a number between 1 and 3")
                        except ValueError:
                            print("Please enter a valid number")
                        continue  # Restart the loop to handle the chosen random action

                    # when taking 1 card form random opponent
                    elif choice == "2":
                        opponents = [p for p in game.players if p != current_player]
                        target = random.choice(opponents)
                        if game.take_random_card(target, current_player):
                            print(f"Took a random card from {target.name}")
                            game.print_hands()
                            break
                        else:
                            print("Cannot take card")

                    elif choice == "3":
                        largest_group = game.find_largest_valid_group(
                            current_player.hand
                        )
                        if largest_group:
                            if game.discard_group(current_player, largest_group):
                                print(f"Discarded {len(largest_group)} cards")
                                game.print_hands()
                                break
                            else:
                                print("Cannot discard group")
                        else:
                            print("No valid group to discard")

                    elif choice == "4":
                        print("Turn passed")
                        break

        winner = game.check_winner()
        if winner:
            print(f"\n=== Game Over ===")
            print(f"{winner.name} wins!")
            break

        game.next_turn()


if __name__ == "__main__":
    main()