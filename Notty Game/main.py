import pygame
import sys
import time
from backend import GameManager
import random


def start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    # Margins and colors
    margin = 40
    container_color = (35, 64, 41, 120)
    text_color = "#ffffff"
    font_path = pygame.font.match_font("arial")  # Default font

    # Fonts
    title_font = pygame.font.Font(font_path, 38)
    button_font = pygame.font.Font(font_path, 20)

    # Main container dimensions
    rect_x = margin
    rect_y = margin
    rect_width = SCREEN_WIDTH - 2 * margin
    rect_height = SCREEN_HEIGHT - 2 * margin

    # Transparent container
    container_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    container_surface.fill(container_color)
    screen.blit(container_surface, (rect_x, rect_y))

    # Title
    title_text = "Notty Game"
    title_surface = title_font.render(title_text, True, text_color)
    title_x = rect_x + (rect_width - title_surface.get_width()) // 2
    title_y = rect_y + 50
    screen.blit(title_surface, (title_x, title_y))

    # Buttons
    button_width = rect_width // 2
    button_height = 60
    button_x = rect_x + (rect_width - button_width) // 2
    button_gap = 40
    start_y = title_y + 100  # Space below the title

    button_texts = ["Play", "Game rules", "Credits", "Exit"]
    button_colors = ["#000000", "#000000", "#000000", "#bc4749"]
    global button_rects  # Store button rects for click detection
    button_rects = []
    for i, text in enumerate(button_texts):
        button_y = start_y + i * (button_height + button_gap)
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_colors[i], button_rect, border_radius=10)
        button_rects.append(button_rect)  # Save rect for click detection

        # Button text
        button_surface = button_font.render(text, True, text_color)
        text_x = button_x + (button_width - button_surface.get_width()) // 2
        text_y = button_y + (button_height - button_surface.get_height()) // 2
        screen.blit(button_surface, (text_x, text_y))


def play_screen(
    screen, SCREEN_WIDTH, SCREEN_HEIGHT, total_players=None, error_message=None
):
    """Render the main game screen with Game Settings."""
    # Margins and colors
    container_color = (35, 64, 41, 120)
    text_color = "#ffffff"
    error_box_color = "#bf3234"  # Slightly transparent red
    font_path = pygame.font.match_font("arial")  # Default font
    title_font = pygame.font.Font(font_path, 32)
    paragraph_font = pygame.font.Font(font_path, 18)
    button_font = pygame.font.Font(font_path, 18)
    error_font = pygame.font.Font(font_path, 16)

    # Load and scale the background image
    main_bg_image = pygame.image.load("main-bg.jpg")
    main_bg_image = pygame.transform.scale(main_bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Render background image
    screen.blit(main_bg_image, (0, 0))

    # Game Settings Container Dimensions
    container_width = SCREEN_WIDTH // 2
    container_height = SCREEN_HEIGHT
    container_x = (SCREEN_WIDTH - container_width) // 2
    container_y = (SCREEN_HEIGHT - container_height) // 2

    # Transparent container for settings
    container_surface = pygame.Surface(
        (container_width, container_height), pygame.SRCALPHA
    )
    container_surface.fill(container_color)
    screen.blit(container_surface, (container_x, container_y))

    # Title: Game Settings
    title_text = "Game Settings"
    title_surface = title_font.render(title_text, True, text_color)
    title_x = container_x + (container_width - title_surface.get_width()) // 2
    title_y = container_y + 44
    screen.blit(title_surface, (title_x, title_y))

    # Body
    para_text = "Select how many players you want to play with"
    para_surface = paragraph_font.render(para_text, True, text_color)
    para_x = container_x + (container_width - para_surface.get_width()) // 2
    para_y = title_y + 84
    screen.blit(para_surface, (para_x, para_y))

    # Options and Start Game Button
    option_width = container_width // 2
    option_height = 50
    option_gap = 20
    option_x = container_x + (container_width - option_width) // 2
    option_y_start = para_y + 100

    global option_1_rect, option_2_rect, start_button_rect, home_button_rect

    # Option 1: 1 Computer Player
    option_1_color = "#1e6091" if total_players == 2 else "#000000"
    option_1_rect = pygame.Rect(option_x, option_y_start, option_width, option_height)
    pygame.draw.rect(screen, option_1_color, option_1_rect, border_radius=10)
    option_1_text = button_font.render("1 Bot", True, text_color)
    screen.blit(
        option_1_text,
        (
            option_x + (option_width - option_1_text.get_width()) // 2,
            option_y_start + (option_height - option_1_text.get_height()) // 2,
        ),
    )

    # Option 2: 2 Computer Players
    option_2_color = "#1e6091" if total_players == 3 else "#000000"
    option_2_rect = pygame.Rect(
        option_x,
        option_y_start + option_height + option_gap,
        option_width,
        option_height,
    )
    pygame.draw.rect(screen, option_2_color, option_2_rect, border_radius=10)
    option_2_text = button_font.render("2 Bots", True, text_color)
    screen.blit(
        option_2_text,
        (
            option_x + (option_width - option_2_text.get_width()) // 2,
            option_y_start
            + option_height
            + option_gap
            + (option_height - option_2_text.get_height()) // 2,
        ),
    )

    # Start Game Button
    start_button_y = option_y_start + 2 * (option_height + option_gap)
    start_button_rect = pygame.Rect(
        option_x, start_button_y, option_width, option_height
    )
    pygame.draw.rect(screen, "#6A994E", start_button_rect, border_radius=10)
    start_button_text = button_font.render("Start Game", True, text_color)
    screen.blit(
        start_button_text,
        (
            option_x + (option_width - start_button_text.get_width()) // 2,
            start_button_y + (option_height - start_button_text.get_height()) // 2,
        ),
    )

    # Back to Home Button
    home_button_y = SCREEN_HEIGHT - 100
    home_button_rect = pygame.Rect(option_x, home_button_y, option_width, option_height)
    pygame.draw.rect(screen, "#bc4749", home_button_rect, border_radius=10)
    home_button_text = button_font.render("Back to Home", True, text_color)
    screen.blit(
        home_button_text,
        (
            option_x + (option_width - home_button_text.get_width()) // 2,
            home_button_y + (option_height - home_button_text.get_height()) // 2,
        ),
    )

    # Error message box
    if error_message:
        error_box_width = container_width
        error_box_height = 40
        error_box_x = container_x
        error_box_y = start_button_y + option_height + 40

        error_surface = pygame.Surface(
            (error_box_width, error_box_height), pygame.SRCALPHA
        )
        error_surface.fill(error_box_color)
        screen.blit(error_surface, (error_box_x, error_box_y))

        error_text_surface = error_font.render(error_message, True, text_color)
        error_text_x = (
            error_box_x + (error_box_width - error_text_surface.get_width()) // 2
        )
        error_text_y = (
            error_box_y + (error_box_height - error_text_surface.get_height()) // 2
        )
        screen.blit(error_text_surface, (error_text_x, error_text_y))


def main_board_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, total_players=0):
    "Main Game Screen"
    font_path = pygame.font.match_font("arial")
    title_font = pygame.font.Font(font_path, 24)
    subtitle_font = pygame.font.Font(font_path, 24)
    card_font = pygame.font.Font(font_path, 24)
    card_number_font = pygame.font.Font(font_path, 18)
    button_font = pygame.font.Font(font_path, 18)
    small_font = pygame.font.Font(font_path, 16)

    card_colors = {
        "red": "#d62828",
        "green": "#8ac926",
        "blue": "#03045e",
        "yellow": "#ffd500",
    }

    deck_colors = {
        "red": "#000000",
        "green": "#e5e5e5",
        "blue": "#000000",
        "yellow": "#e5e5e5",
    }

    # Load and scale the background image
    main_bg_image = pygame.image.load("start-game-bg.jpg")
    main_bg_image = pygame.transform.scale(main_bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Render background image
    screen.blit(main_bg_image, (0, 0))

    # Back to Home Button
    back_button_width = 120
    back_button_height = 50
    back_button_x = 55
    back_button_y = 20
    global back_to_home_rect  # Store rectangle for click handling
    back_to_home_rect = pygame.Rect(
        back_button_x, back_button_y, back_button_width, back_button_height
    )

    # Draw the Back to Home button
    pygame.draw.rect(screen, "#BC4749", back_to_home_rect, border_radius=10)
    back_button_text = small_font.render("Back to home", True, (255, 255, 255))
    back_text_x = (
        back_button_x + (back_button_width - back_button_text.get_width()) // 2
    )
    back_text_y = (
        back_button_y + (back_button_height - back_button_text.get_height()) // 2
    )
    screen.blit(back_button_text, (back_text_x, back_text_y))

    title_text = "Deck"
    title_surface = title_font.render(title_text, True, (255, 255, 255))
    title_x = (SCREEN_WIDTH - title_surface.get_width()) // 2
    title_y = 20
    screen.blit(title_surface, (title_x, title_y))

    # Current Turn Box
    current_player = game_manager.players[game_manager.current_player]
    turn_text = f"Turn: {current_player.name}"
    turn_surface = button_font.render(turn_text, True, (255, 255, 255))

    # Transparent box dimensions
    box_width = 200
    box_height = 50
    box_x = SCREEN_WIDTH - box_width - 40  # Positioned at the top-right
    box_y = 20

    # Draw the transparent box
    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    box_surface.fill((0, 0, 0, 160))  # Black with some transparency
    screen.blit(box_surface, (box_x, box_y))

    # Render the turn text
    text_x = box_x + (box_width - turn_surface.get_width()) // 2
    text_y = box_y + (box_height - turn_surface.get_height()) // 2
    screen.blit(turn_surface, (text_x, text_y))

    # Deck showing top 5 for now
    deck_obj = game_manager.deck.cards
    deck = game_manager.format_deck_list(deck_obj)
    top_deck_cards = deck[-4:]

    # Deck position and dimensions
    deck_width = 120
    deck_height = 160
    deck_x = SCREEN_WIDTH // 2 - deck_width // 2
    deck_y = SCREEN_HEIGHT // 6

    for i, card in enumerate(top_deck_cards):
        color_name, number = card.split()
        card_color = pygame.Color(deck_colors[color_name])

        card_rect = pygame.Rect(deck_x, deck_y - i * 15, deck_width, deck_height)
        pygame.draw.rect(screen, card_color, card_rect, border_radius=10)

        # Render number
        number_color = "black" if color_name in ["yellow", "green"] else "white"
        number_surface = small_font.render("Face Down", True, number_color)
        number_x = card_rect.x + (deck_width - number_surface.get_width()) // 2
        number_y = card_rect.y + (deck_height - number_surface.get_height()) // 2
        screen.blit(number_surface, (number_x, number_y))

    # Remaining cards box
    remaining_cards_text = f"Cards left: {len(deck)}"
    remaining_cards_surface = button_font.render(
        remaining_cards_text, True, (255, 255, 255)
    )

    box_width = deck_width + 20
    box_height = 40
    box_x = deck_x - 10
    box_y = deck_y + deck_height + 20  # Below deck

    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
    box_surface.fill((0, 0, 0, 160))  # Black with some transparency
    screen.blit(box_surface, (box_x, box_y))

    text_x = box_x + (box_width - remaining_cards_surface.get_width()) // 2
    text_y = box_y + (box_height - remaining_cards_surface.get_height()) // 2
    screen.blit(remaining_cards_surface, (text_x, text_y))

    # Action Buttons
    button_width = 150
    button_height = 50
    button_gap = 20
    buttons = ["Draw", "Steal Card", "Discard", "Pass", "Play for me"]
    global human_button_rects  # Store button rectangles for interaction
    human_button_rects = []

    for i, button_text in enumerate(buttons):
        button_x = (
            SCREEN_WIDTH // 2
            - 2 * button_width
            - button_gap
            + i * (button_width + button_gap)
        ) - 95
        button_y = SCREEN_HEIGHT - 350  # Positioned above the human player's cards
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        human_button_rects.append(button_rect)
        if button_rect.collidepoint(mouse_pos):
            button_color = "#6A994E"  # Hover color (green)
        else:
            button_color = "black"  # Default color
        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)

        # Render button text
        text_surface = button_font.render(button_text, True, (255, 255, 255))
        text_x = button_x + (button_width - text_surface.get_width()) // 2
        text_y = button_y + (button_height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

    card_width = 80
    card_height = 100
    card_gap = 10
    card_gap_col = 14

    human_cards_obj = game_manager.players[0]
    human_cards = game_manager.format_card_list(human_cards_obj)

    #    Maximum cards per row
    max_cards_per_row = 10

    #    Calculate the number of rows needed
    num_cards = len(human_cards)
    num_rows = (
        num_cards + max_cards_per_row - 1
    ) // max_cards_per_row  # Ceiling division
    human_start_y = SCREEN_HEIGHT - 250  # Y Pos 1st row

    for row in range(num_rows):
        # Determine the cards for the current row
        row_start_idx = row * max_cards_per_row
        row_end_idx = min((row + 1) * max_cards_per_row, num_cards)
        cards_in_row = human_cards[row_start_idx:row_end_idx]

        # X pos ceneter
        total_card_width = (
            len(cards_in_row) * card_width + (len(cards_in_row) - 1) * card_gap
        )
        human_start_x = (SCREEN_WIDTH - total_card_width) // 2

        for col, card in enumerate(cards_in_row):
            color_name, number = card.split()
            card_color = pygame.Color(card_colors[color_name])

            card_x = human_start_x + col * (card_width + card_gap)
            card_y = human_start_y + row * (card_height + card_gap)
            card_rect = pygame.Rect(card_x, card_y, card_width, card_height)
            pygame.draw.rect(screen, card_color, card_rect, border_radius=10)

            # Render the card number
            number_color = "black" if color_name in ["yellow", "green"] else "white"
            number_surface = card_font.render(number, True, number_color)
            number_x = card_rect.x + (card_width - number_surface.get_width()) // 2
            number_y = card_rect.y + (card_height - number_surface.get_height()) // 2
            screen.blit(number_surface, (number_x, number_y))

    # Computer Player 1 (Left, stacked into two columns)
    player1_cards_obj = game_manager.players[1]
    player1_cards = game_manager.format_card_list(player1_cards_obj)
    player1_title = subtitle_font.render("Notty Bot 1", True, (255, 255, 255))
    player1_title_x = 55
    player1_title_y = SCREEN_HEIGHT // 4 - 60
    screen.blit(player1_title, (player1_title_x, player1_title_y))

    player1_start_x = 50
    player1_start_y = SCREEN_HEIGHT // 4

    for i, card in enumerate(player1_cards):
        col = i // 10
        row = i % 10

        color_name, number = card.split()
        card_color = pygame.Color(card_colors[color_name])

        card_x = player1_start_x + col * (card_width + card_gap_col)
        card_y = player1_start_y + row * 40
        card_rect = pygame.Rect(card_x, card_y, card_width, card_height)
        pygame.draw.rect(screen, card_color, card_rect, border_radius=10)

        number_color = "black" if color_name in ["yellow", "green"] else "white"
        number_surface = card_number_font.render(number, True, number_color)
        number_x = card_rect.x + card_width - number_surface.get_width() - 5
        number_y = card_rect.y + 5
        screen.blit(number_surface, (number_x, number_y))

    # Show Player 2 cards only if total_players == 3
    if total_players == 3:
        player2_cards_obj = game_manager.players[2]
        player2_cards = game_manager.format_card_list(player2_cards_obj)
        player2_title = subtitle_font.render("Notty Bot 2", True, (255, 255, 255))
        player2_title_x = SCREEN_WIDTH - 110 - player2_title.get_width()
        player2_title_y = SCREEN_HEIGHT // 4 - 60
        screen.blit(player2_title, (player2_title_x, player2_title_y))

        player2_start_x = SCREEN_WIDTH - 50 - (2 * (card_width + card_gap))
        player2_start_y = SCREEN_HEIGHT // 4

        for i, card in enumerate(player2_cards):
            col = i // 10
            row = i % 10

            color_name, number = card.split()
            card_color = pygame.Color(card_colors[color_name])

            card_x = player2_start_x + col * (card_width + card_gap_col)
            card_y = player2_start_y + row * 40
            card_rect = pygame.Rect(card_x, card_y, card_width, card_height)
            pygame.draw.rect(screen, card_color, card_rect, border_radius=10)

            number_color = "black" if color_name in ["yellow", "green"] else "white"
            number_surface = card_number_font.render(number, True, number_color)
            number_x = card_rect.x + card_width - number_surface.get_width() - 5
            number_y = card_rect.y + 5
            screen.blit(number_surface, (number_x, number_y))


def game_rules_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """Render the Game Rules Screen."""
    # Background color and text settings
    container_color = (35, 64, 41, 120)
    text_color = "#ffffff"
    font_path = pygame.font.match_font("arial")  # Default font

    # Updated font sizes
    title_font = pygame.font.Font(font_path, 32)
    body_font = pygame.font.Font(font_path, 18)

    # Main container dimensions
    rect_width = SCREEN_WIDTH // 2
    rect_height = SCREEN_HEIGHT
    rect_x = (SCREEN_WIDTH - rect_width) // 2
    rect_y = (SCREEN_HEIGHT - rect_height) // 2

    # Transparent container
    container_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    container_surface.fill(container_color)
    screen.blit(container_surface, (rect_x, rect_y))

    # Title
    title_text = "Game Rules"
    title_surface = title_font.render(title_text, True, text_color)
    title_x = rect_x + (rect_width - title_surface.get_width()) // 2
    title_y = rect_y + 20
    screen.blit(title_surface, (title_x, title_y))

    # Body Text (Updated Game Rules)
    rules_text = [
        "",
        "",
        "*Setup*",
        "   Five cards will be given face up to each player from a shuffled deck.",
        "   Remaining deck stays face down.",
        "",
        "*Gameplay (on your turn)*",
        "  1. Draw up to 3 cards (once per turn).",
        "  2. Take 1 random card from another player.",
        "  3. Discard valid groups:",
        "      Sequence: Same color, consecutive numbers.",
        "      Set: Same number, different colors (no repeats).",
        "  4. Pass (do nothing).",
        "",
        "*Additional Rules*",
        "You cannot hold more than 20 cards in your hand.",
        "Every time cards are discarded, they are returned to the deck, and the deck is reshuffled.",
        "",
        "*Goal: Empty your hand first to win!*",
        "",
        "*Enjoy playing Notty!*",
    ]

    # Render rules text (Center-aligned within the container)
    line_height = body_font.get_linesize()
    start_y = title_y + 70  # Adjusted spacing for larger title

    for line in rules_text:
        body_surface = body_font.render(line, True, text_color)
        line_width = body_surface.get_width()
        text_x = rect_x + (rect_width - line_width) // 2  # Center horizontally
        screen.blit(body_surface, (text_x, start_y))
        start_y += line_height + 6

    # Back Button
    global home_button_rect  # Reuse the home button rect
    button_width = 200
    button_height = 50
    button_x = rect_x + (rect_width - button_width) // 2
    button_y = rect_y + rect_height - button_height - 20
    home_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, "#bc4749", home_button_rect, border_radius=10)

    button_text = body_font.render("Back to Home", True, text_color)
    text_x = button_x + (button_width - button_text.get_width()) // 2
    text_y = button_y + (button_height - button_text.get_height()) // 2
    screen.blit(button_text, (text_x, text_y))


def credits_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
    """Render the Credits Screen."""
    # Background color and text settings
    container_color = (35, 64, 41, 120)
    text_color = "#ffffff"
    font_path = pygame.font.match_font("arial")  # Default font
    title_font = pygame.font.Font(font_path, 32)
    body_font = pygame.font.Font(font_path, 22)  # Larger font for better visibility

    # Main container dimensions
    rect_width = SCREEN_WIDTH // 2
    rect_height = SCREEN_HEIGHT
    rect_x = (SCREEN_WIDTH - rect_width) // 2
    rect_y = (SCREEN_HEIGHT - rect_height) // 2

    # Transparent container
    container_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    container_surface.fill(container_color)
    screen.blit(container_surface, (rect_x, rect_y))

    # Title
    title_text = "Credits"
    title_surface = title_font.render(title_text, True, text_color)
    title_x = rect_x + (rect_width - title_surface.get_width()) // 2
    title_y = rect_y + 20
    screen.blit(title_surface, (title_x, title_y))

    # Credits Text
    credits_text = [
        "",
        "",
        "",
        "",
        "",
        "*Muneeb Amer*",
        "",
        "*Abu Qais*",
        "",
        "*Harsh Moradiya*",
        "",
        "*Shabbir Kutbuddin*",
        "",
        "*Ali Tahir*",
        "",
        "",
        "Thank you for playing Notty!",
    ]

    # Render credits text, center-aligned within the container
    line_height = body_font.get_linesize()
    start_y = title_y + 80  # Spacing below the title
    for line in credits_text:
        line_surface = body_font.render(line, True, text_color)
        line_width = line_surface.get_width()
        text_x = rect_x + (rect_width - line_width) // 2  # Center align
        screen.blit(line_surface, (text_x, start_y))
        start_y += line_height

    # Back Button
    global home_button_rect  # Reuse the home button rect
    button_width = 200
    button_height = 50
    button_x = rect_x + (rect_width - button_width) // 2
    button_y = rect_y + rect_height - button_height - 20
    home_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, "#bc4749", home_button_rect, border_radius=10)

    button_text = body_font.render("Back to Home", True, text_color)
    text_x = button_x + (button_width - button_text.get_width()) // 2
    text_y = button_y + (button_height - button_text.get_height()) // 2
    screen.blit(button_text, (text_x, text_y))


def show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, duration):
    print("Message: ", message)
    overlay_width = 400
    overlay_height = 100
    overlay_x = (SCREEN_WIDTH - overlay_width) // 2
    overlay_y = (SCREEN_HEIGHT - overlay_height) // 2

    overlay_surface = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
    overlay_surface.fill((0, 0, 0, 150))
    screen.blit(overlay_surface, (overlay_x, overlay_y))

    font_path = pygame.font.match_font("arial")
    message_font = pygame.font.Font(font_path, 16)
    message_surface = message_font.render(message, True, (255, 255, 255))
    message_x = overlay_x + (overlay_width - message_surface.get_width()) // 2
    message_y = overlay_y + (overlay_height - message_surface.get_height()) // 2
    screen.blit(message_surface, (message_x, message_y))

    pygame.display.flip()

    # Pause for 1 second
    time.sleep(duration)


def show_winner_screen(screen, winner_name, SCREEN_WIDTH, SCREEN_HEIGHT):
    overlay_width = 600
    overlay_height = 200
    overlay_x = (SCREEN_WIDTH - overlay_width) // 2
    overlay_y = (SCREEN_HEIGHT - overlay_height) // 2

    overlay_surface = pygame.Surface((overlay_width, overlay_height), pygame.SRCALPHA)
    overlay_surface.fill((0, 0, 0, 150))  # Black with transparency
    screen.blit(overlay_surface, (overlay_x, overlay_y))

    font_path = pygame.font.match_font("arial")
    title_font = pygame.font.Font(font_path, 28)
    button_font = pygame.font.Font(font_path, 18)

    winner_text = f"{winner_name} Wins!"
    winner_surface = title_font.render(winner_text, True, (255, 255, 255))  # White text
    winner_x = overlay_x + (overlay_width - winner_surface.get_width()) // 2
    winner_y = overlay_y + 40
    screen.blit(winner_surface, (winner_x, winner_y))

    button_width = 200
    button_height = 50
    button_x = overlay_x + (overlay_width - button_width) // 2
    button_y = overlay_y + overlay_height - 80

    global home_button_rect
    home_button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    pygame.draw.rect(screen, "#6A994E", home_button_rect, border_radius=10)
    home_text = button_font.render("Home", True, (255, 255, 255))
    home_text_x = button_x + (button_width - home_text.get_width()) // 2
    home_text_y = button_y + (button_height - home_text.get_height()) // 2
    screen.blit(home_text, (home_text_x, home_text_y))

    pygame.display.flip()


def handle_button_click(mouse_pos):
    """Handle button clicks and return the action."""
    if button_rects[0].collidepoint(mouse_pos):  # Play button
        game_manager.reset_game()
        return "play"
    elif button_rects[1].collidepoint(mouse_pos):  # Game Rules
        return "Game Rules"
    elif button_rects[2].collidepoint(mouse_pos):  # Credit
        return "Credits"
    elif button_rects[3].collidepoint(mouse_pos):  # Exit button
        return "exit"
    return None


def handle_play_screen_click(mouse_pos, total_players):
    if option_1_rect.collidepoint(mouse_pos):
        return ("option", 2)
    elif option_2_rect.collidepoint(mouse_pos):
        return ("option", 3)
    elif start_button_rect.collidepoint(mouse_pos):
        if total_players > 1:
            playSound('./sounds/game-start.mp3',0)
            return "board"
        else:
            return "error"  # Return error state if no valid selection is made
    elif home_button_rect.collidepoint(mouse_pos):
        return "start"


def handle_win_screen_click(mouse_pos):
    if home_button_rect.collidepoint(mouse_pos):
        return "start"


def update_game_state(game_manager, total_players):
    """Fetch the updated game state from the backend and update frontend variables."""
    global human_cards, player1_cards, player2_cards, deck_count, current_turn

    # Fetch cards for each player
    human_cards = game_manager.format_card_list(game_manager.players[0])
    player1_cards = game_manager.format_card_list(game_manager.players[1])
    if total_players == 3:
        player2_cards = game_manager.format_card_list(game_manager.players[2])
    else:
        player2_cards = []

    # Fetch deck count
    deck_count = len(game_manager.deck.cards)

    # Update the current player
    current_turn = game_manager.players[game_manager.current_player]


def handle_human_player_action(game_manager, current_turn, action, total_players):
    if action == "Play for me":
        possible_actions = ["Draw Cards", "Steal Card", "Discard Group", "Pass Turn"]
        while True:
            random_action = random.choice(possible_actions)
            # If selected action is Discard Group, check if valid groups exist
            if random_action == "Discard Group":
                largest_group = game_manager.find_largest_valid_group(current_turn.hand)
                if not largest_group:
                    # Remove Discard Group from possible actions and try again
                    possible_actions.remove("Discard Group")
                    continue
            return handle_human_player_action(
                game_manager, current_turn, random_action, total_players
            )

    if action == "Draw Cards":
        option_selected = draw_cards_dialog()
        if option_selected:
            if len(current_turn.hand) + option_selected <= 20:
                game_manager.draw_cards(current_turn, option_selected)
                message = f"{option_selected} cards added to your deck"
                show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5)
                return True
            else:
                message = f"you have {len(current_turn.hand)} cards in deck...cant draw"
                show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5)
                return False
                # return handle_human_player_action(game_manager, current_turn, action, total_players)

    ##improve here
    elif action == "Steal Card":
        if len(current_turn.hand) != 20:

            if total_players > 2:
                choice = steal_card_dialog(total_players)
                if choice:
                    target_player = game_manager.choose_target_player(
                        current_turn, choice
                    )
                    if len(current_turn.hand) != 20:
                        game_manager.take_random_card(target_player, current_turn)
                        message = f"You stole a card from {target_player.name}"
                        show_action_screen(
                            screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5
                        )
                        return True

            else:
                target_player = game_manager.choose_target_player(current_turn, 2)
                game_manager.take_random_card(target_player, current_turn)
                message = f"You stole a card from {target_player.name}"
                show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5)
                return True
        else:
            message = f"You already have 20 cards!"
            show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5)
            return False

    elif action == "Discard Group":
        largest_group = game_manager.find_largest_valid_group(current_turn.hand)
        if largest_group:
            game_manager.discard_group(current_turn, largest_group)
            message = f"You discarded a valid group of {len(largest_group)} cards. Deck reshuffled"
            show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5)            
            return True
        else:
            message = "No valid group to discard. Choose another action"
            show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5)
            return False
    elif action == "Pass Turn":
        message = "You passed your turn."
        show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.5)
        pass
    return True


def draw_cards_dialog():
    dialog_width = 400
    dialog_height = 200
    dialog_x = (SCREEN_WIDTH - dialog_width) // 2
    dialog_y = (SCREEN_HEIGHT - dialog_height) // 2

    font_path = pygame.font.match_font("arial")
    title_font = pygame.font.Font(font_path, 20)
    option_font = pygame.font.Font(font_path, 18)
    options = [1, 2, 3]
    option_rects = []

    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))  # Black with transparency
    screen.blit(overlay, (0, 0))

    pygame.draw.rect(
        screen,
        (35, 64, 41),
        (dialog_x, dialog_y, dialog_width, dialog_height),
        border_radius=10,
    )

    title_text = "Select how many cards to draw"
    title_surface = title_font.render(title_text, True, (255, 255, 255))
    title_x = dialog_x + (dialog_width - title_surface.get_width()) // 2
    title_y = dialog_y + 26
    screen.blit(title_surface, (title_x, title_y))

    for i, option in enumerate(options):
        option_width = 80
        option_height = 40
        option_x = (
            (dialog_x - 20)
            + (dialog_width - len(options) * option_width) // 2
            + i * (option_width + 20)
        )
        option_y = dialog_y + dialog_height - 80

        option_rect = pygame.Rect(option_x, option_y, option_width, option_height)
        option_rects.append(option_rect)

        pygame.draw.rect(screen, "#6A994E", option_rect, border_radius=10)
        option_surface = option_font.render(str(option), True, (255, 255, 255))
        option_text_x = option_x + (option_width - option_surface.get_width()) // 2
        option_text_y = option_y + (option_height - option_surface.get_height()) // 2
        screen.blit(option_surface, (option_text_x, option_text_y))

    pygame.display.flip()

    # Wait for user to select an option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(mouse_pos):
                        return options[i]  # Return the selected option


def steal_card_dialog(total_players):
    dialog_width = 400
    dialog_height = 200
    dialog_x = (SCREEN_WIDTH - dialog_width) // 2
    dialog_y = (SCREEN_HEIGHT - dialog_height) // 2

    font_path = pygame.font.match_font("arial")
    title_font = pygame.font.Font(font_path, 20)
    option_font = pygame.font.Font(font_path, 16)

    # Define the options based on total_players
    options = ["Notty Bot 1"]
    if total_players == 3:
        options.append("Notty Bot 2")
    option_rects = []

    # Create a semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))  # Black with transparency
    screen.blit(overlay, (0, 0))

    # Draw the dialog box
    pygame.draw.rect(
        screen,
        (35, 64, 41),
        (dialog_x, dialog_y, dialog_width, dialog_height),
        border_radius=10,
    )

    # Draw the title
    title_text = "Select a player to steal card from"
    title_surface = title_font.render(title_text, True, (255, 255, 255))
    title_x = dialog_x + (dialog_width - title_surface.get_width()) // 2
    title_y = dialog_y + 26
    screen.blit(title_surface, (title_x, title_y))

    # Render options (Player 1, Player 2)
    for i, option in enumerate(options):
        option_width = 150
        option_height = 50
        option_x = (
            (dialog_x - 10)
            + (dialog_width - len(options) * option_width) // 2
            + i * (option_width + 20)
        )
        option_y = dialog_y + dialog_height - 80

        option_rect = pygame.Rect(option_x, option_y, option_width, option_height)
        option_rects.append(option_rect)

        pygame.draw.rect(screen, "#6A994E", option_rect, border_radius=10)
        option_surface = option_font.render(option, True, (255, 255, 255))
        option_text_x = option_x + (option_width - option_surface.get_width()) // 2
        option_text_y = option_y + (option_height - option_surface.get_height()) // 2
        screen.blit(option_surface, (option_text_x, option_text_y))

    pygame.display.flip()

    # Wait for user to select an option
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(mouse_pos):
                        return i + 1  # Return the player number (1 or 2)


def handle_computer_turn(game_manager, current_turn):
    """Handle the computer player's turn."""
    action_message = game_manager.handle_computer_turn(current_turn)
    return action_message


def switch_turn(game_manager):
    game_manager.next_turn()

def playSound(filePath, duration):
    pygame.init()
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play()
    time.sleep(duration)
    


def render_game_state(screen, game_manager, total_players, SCREEN_WIDTH, SCREEN_HEIGHT):
    update_game_state(game_manager, total_players)
    main_board_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, total_players)


def handle_main_board_screen_click(mouse_pos):
    if back_to_home_rect.collidepoint(mouse_pos):
        return "start"


def handle_human_buttons(mouse_pos):
    if human_button_rects[0].collidepoint(mouse_pos):
        return "Draw Cards"
    elif human_button_rects[1].collidepoint(mouse_pos):
        return "Steal Card"
    elif human_button_rects[2].collidepoint(mouse_pos):
        return "Discard Group"
    elif human_button_rects[3].collidepoint(mouse_pos):
        return "Pass Turn"
    elif human_button_rects[4].collidepoint(mouse_pos):
        return "Play for me"


def handle_game_rules_screen_click(mouse_pos):
    if home_button_rect.collidepoint(mouse_pos):
        return "start"


def handle_credits_rules_screen_click(mouse_pos):
    if home_button_rect.collidepoint(mouse_pos):
        return "start"


def handle_turn(
    screen, game_manager, total_players, SCREEN_WIDTH, SCREEN_HEIGHT, event
):
    global current_turn
    current_turn = game_manager.players[game_manager.current_player]

    if current_turn.is_computer:
        # backend computer actions
        message = handle_computer_turn(game_manager, current_turn)
        show_action_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT, message, 1.8)
        switch_turn(game_manager)
    else:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            action = handle_human_buttons(mouse_pos)
            if action:
                res = handle_human_player_action(
                    game_manager, current_turn, action, total_players
                )
                # If the action is valid, proceed to the next turn
                if res:
                    switch_turn(game_manager)

    # Render the updated game state
    render_game_state(screen, game_manager, total_players, SCREEN_WIDTH, SCREEN_HEIGHT)


def main():
    # Pygame setup
    pygame.init()
    global screen
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    screen = pygame.display.set_mode((1500, 800))
    clock = pygame.time.Clock()
    running = True
    total_players = 0
    SCREEN_WIDTH = screen.get_width()
    SCREEN_HEIGHT = screen.get_height()
    global mouse_pos

    # Initialize the game manager
    global game_manager
    game_manager = GameManager()

    # Load and scale the background image
    background_image = pygame.image.load("main-bg.jpg")
    background_image = pygame.transform.scale(
        background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    current_screen = "start"
    winner = None
    error_message = None
    next_turn_delay = 1000
    next_turn_time = None

    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if current_screen == "start":
                    action = handle_button_click(mouse_pos)
                    if action == "play":
                        current_screen = "play"
                    elif action == "Game Rules":
                        current_screen = "Game Rules"
                    elif action == "Credits":
                        current_screen = "Credits"
                    elif action == "exit":
                        running = False
                elif current_screen == "Game Rules":
                    action = handle_game_rules_screen_click(mouse_pos)
                    if action == "start":
                        current_screen = "start"
                elif current_screen == "Credits":
                    action = handle_credits_rules_screen_click(mouse_pos)
                    if action == "start":
                        current_screen = "start"
                elif current_screen == "play":
                    action = handle_play_screen_click(mouse_pos, total_players)
                    if action == "start":
                        current_screen = "start"
                    elif action == "error":
                        error_message = (
                            "Please select an option before starting the game!"
                        )
                    elif action == "board" and total_players > 1:
                        # Game Start
                        game_manager.add_players(total_players, "Batman")
                        game_manager.start_game()
                        next_turn_time = current_time + next_turn_delay
                        current_screen = "board"
                    elif isinstance(action, tuple):
                        total_players = action[1]
                elif current_screen == "board":
                    back_home_action = handle_main_board_screen_click(mouse_pos)
                    if back_home_action == "start":
                        current_screen = "start"
                    # Action Humaan
                    if not game_manager.players[
                        game_manager.current_player
                    ].is_computer:
                        handle_turn(
                            screen,
                            game_manager,
                            total_players,
                            SCREEN_WIDTH,
                            SCREEN_HEIGHT,
                            event,
                        )
                        if game_manager.players[
                            game_manager.current_player
                        ].is_computer:
                            next_turn_time = current_time + next_turn_delay
                elif current_screen == "winner":
                    # Handle clicks on the winner screen
                    action = handle_win_screen_click(mouse_pos)
                    if action == "start":
                        current_screen = "start"
        if (
            current_screen == "board"
            and next_turn_time is not None
            and current_time >= next_turn_time
        ):
            # computer check
            if game_manager.players[game_manager.current_player].is_computer:
                handle_turn(
                    screen,
                    game_manager,
                    total_players,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT,
                    None,
                )
                if not game_manager.players[game_manager.current_player].is_computer:
                    next_turn_time = None  # human action waitss

        # Winner condition check
        if current_screen == "board":
            winner = game_manager.check_winner()
            if winner:
                current_screen = "winner"

        # Render current screen
        screen.blit(background_image, (0, 0))
        if current_screen == "start":
            start_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif current_screen == "Game Rules":
            game_rules_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif current_screen == "Credits":
            credits_screen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
        elif current_screen == "play":
            play_screen(
                screen, SCREEN_WIDTH, SCREEN_HEIGHT, total_players, error_message
            )
        elif current_screen == "board":
            render_game_state(
                screen, game_manager, total_players, SCREEN_WIDTH, SCREEN_HEIGHT
            )
        elif current_screen == "winner":
            # Render the winner screen
            show_winner_screen(screen, winner.name, SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
