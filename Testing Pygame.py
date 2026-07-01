import pygame
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def asset_path(*parts):
    return BASE_DIR.joinpath("Assets", *parts)

pygame.init()

screen = pygame.display.set_mode((1000, 800))
font = pygame.font.Font('Grand9K Pixel.ttf', 36)

player_score = 18

running = True


def card_front_img(inp):
    frames = {
        ("♠", "A"): pygame.image.load(str(asset_path("Cards", "SP_A.png"))).convert_alpha(),
        ("♠", "2"): pygame.image.load(str(asset_path("Cards", "SP_2.png"))).convert_alpha(),
        ("♠", "3"): pygame.image.load(str(asset_path("Cards", "SP_3.png"))).convert_alpha(),
        ("♠", "4"): pygame.image.load(str(asset_path("Cards", "SP_4.png"))).convert_alpha(),
        ("♠", "5"): pygame.image.load(str(asset_path("Cards", "SP_5.png"))).convert_alpha(),
        ("♠", "6"): pygame.image.load(str(asset_path("Cards", "SP_6.png"))).convert_alpha(),
        ("♠", "7"): pygame.image.load(str(asset_path("Cards", "SP_7.png"))).convert_alpha(),
        ("♠", "8"): pygame.image.load(str(asset_path("Cards", "SP_8.png"))).convert_alpha(),
        ("♠", "9"): pygame.image.load(str(asset_path("Cards", "SP_9.png"))).convert_alpha(),
        ("♠", "10"): pygame.image.load(str(asset_path("Cards", "SP_10.png"))).convert_alpha(),
        ("♠", "J"): pygame.image.load(str(asset_path("Cards", "SP_J.png"))).convert_alpha(),
        ("♠", "Q"): pygame.image.load(str(asset_path("Cards", "SP_Q.png"))).convert_alpha(),
        ("♠", "K"): pygame.image.load(str(asset_path("Cards", "SP_K.png"))).convert_alpha(),
        ('♣', 'A'): pygame.image.load(str(asset_path("Cards", "Cl_A.png"))).convert_alpha(),
        ('♣', '2'): pygame.image.load(str(asset_path("Cards", "Cl_2.png"))).convert_alpha(),
        ('♣', '3'): pygame.image.load(str(asset_path("Cards", "Cl_3.png"))).convert_alpha(),
        ('♣', '4'): pygame.image.load(str(asset_path("Cards", "Cl_4.png"))).convert_alpha(),
        ('♣', '5'): pygame.image.load(str(asset_path("Cards", "Cl_5.png"))).convert_alpha(),
        ('♣', '6'): pygame.image.load(str(asset_path("Cards", "Cl_6.png"))).convert_alpha(),
        ('♣', '7'): pygame.image.load(str(asset_path("Cards", "Cl_7.png"))).convert_alpha(),
        ('♣', '8'): pygame.image.load(str(asset_path("Cards", "Cl_8.png"))).convert_alpha(),
        ('♣', '9'): pygame.image.load(str(asset_path("Cards", "Cl_9.png"))).convert_alpha(),
        ('♣', '10'): pygame.image.load(str(asset_path("Cards", "Cl_10.png"))).convert_alpha(),
        ('♣', 'J'): pygame.image.load(str(asset_path("Cards", "Cl_J.png"))).convert_alpha(),
        ('♣', 'Q'): pygame.image.load(str(asset_path("Cards", "Cl_Q.png"))).convert_alpha(),
        ('♣', 'K'): pygame.image.load(str(asset_path("Cards", "Cl_K.png"))).convert_alpha(),
        ('♥', 'A'): pygame.image.load(str(asset_path("Cards", "He_A.png"))).convert_alpha(),
        ('♥', '2'): pygame.image.load(str(asset_path("Cards", "He_2.png"))).convert_alpha(),
        ('♥', '3'): pygame.image.load(str(asset_path("Cards", "He_3.png"))).convert_alpha(),
        ('♥', '4'): pygame.image.load(str(asset_path("Cards", "He_4.png"))).convert_alpha(),
        ('♥', '5'): pygame.image.load(str(asset_path("Cards", "He_5.png"))).convert_alpha(),
        ('♥', '6'): pygame.image.load(str(asset_path("Cards", "He_6.png"))).convert_alpha(),
        ('♥', '7'): pygame.image.load(str(asset_path("Cards", "He_7.png"))).convert_alpha(),
        ('♥', '8'): pygame.image.load(str(asset_path("Cards", "He_8.png"))).convert_alpha(),
        ('♥', '9'): pygame.image.load(str(asset_path("Cards", "He_9.png"))).convert_alpha(),
        ('♥', '10'): pygame.image.load(str(asset_path("Cards", "He_10.png"))).convert_alpha(),
        ('♥', 'J'): pygame.image.load(str(asset_path("Cards", "He_J.png"))).convert_alpha(),
        ('♥', 'Q'): pygame.image.load(str(asset_path("Cards", "He_Q.png"))).convert_alpha(),
        ('♥', 'K'): pygame.image.load(str(asset_path("Cards", "He_K.png"))).convert_alpha(),
        ('♦', 'A'): pygame.image.load(str(asset_path("Cards", "Di_A.png"))).convert_alpha(),
        ('♦', '2'): pygame.image.load(str(asset_path("Cards", "Di_2.png"))).convert_alpha(),
        ('♦', '3'): pygame.image.load(str(asset_path("Cards", "Di_3.png"))).convert_alpha(),
        ('♦', '4'): pygame.image.load(str(asset_path("Cards", "Di_4.png"))).convert_alpha(),
        ('♦', '5'): pygame.image.load(str(asset_path("Cards", "Di_5.png"))).convert_alpha(),
        ('♦', '6'): pygame.image.load(str(asset_path("Cards", "Di_6.png"))).convert_alpha(),
        ('♦', '7'): pygame.image.load(str(asset_path("Cards", "Di_7.png"))).convert_alpha(),
        ('♦', '8'): pygame.image.load(str(asset_path("Cards", "Di_8.png"))).convert_alpha(),
        ('♦', '9'): pygame.image.load(str(asset_path("Cards", "Di_9.png"))).convert_alpha(),
        ('♦', '10'): pygame.image.load(str(asset_path("Cards", "Di_10.png"))).convert_alpha(),
        ('♦', 'J'): pygame.image.load(str(asset_path("Cards", "Di_J.png"))).convert_alpha(),
        ('♦', 'Q'): pygame.image.load(str(asset_path("Cards", "Di_Q.png"))).convert_alpha(),
        ('♦', 'K'): pygame.image.load(str(asset_path("Cards", "Di_K.png"))).convert_alpha()
    }
    return frames[inp]


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    text_surface = font.render(
        f"Player Score: {player_score}",
        False,
        (0, 0, 0)
    )

    screen.blit(text_surface, (0, 0))

    screen.blit(card_front_img(('♣', '10')), (100, 100))
    pygame.display.flip()

pygame.quit()
