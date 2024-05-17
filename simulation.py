

import pygame
import sys
import random
import joblib
from utils import *

pygame.init()

key_fra_model = joblib.load('RandomFOrest.joblib')
relay_attack_model = joblib.load('RelayAttack.joblib')

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30
FONT = pygame.font.Font(None, 36)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vehicle Cyber Attack Simulation")
clock = pygame.time.Clock()

# Variables to store prediction results
key_fra_result = None
relay_attack_result = None
def draw_button(text, x, y, w, h, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, button_rect)
    draw_text(text, FONT, BLACK if color == WHITE else WHITE, screen, x + 10, y + 5)

    if button_rect.collidepoint(mouse[0], mouse[1]) and click[0] == 1:
        pygame.time.wait(200)
        if action:
            action()
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_slider(label, x, y, val, min_val, max_val, step, width=200):
    slider_rect = pygame.Rect(x, y + 20, width, 10)
    handle_rect = pygame.Rect(x + (val - min_val) / (max_val - min_val) * width - 5, y + 10, 10, 30)
    
    pygame.draw.rect(screen, GREY, slider_rect)
    pygame.draw.rect(screen, BLUE, handle_rect)
    draw_text(f"{label}: {round(val)}", FONT, WHITE, screen, x, y - 30)
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if click[0] == 1 and handle_rect.collidepoint(mouse[0], mouse[1]):
        rel_x = mouse[0] - x
        new_val = min_val + (rel_x / width) * (max_val - min_val)
        val = round(new_val / step) * step
        val = max(min_val, min(val, max_val))
    return val

def main():
    global key_fra_result, relay_attack_result
    frequency = 20.0
    distance = 5.0
    timedelta = 1.0
    signal_strength = 50.0
    running = True

    while running:
        screen.fill(BLACK)
        draw_text("Vehicle Cyber Attack Simulation", FONT, WHITE, screen, 50, 20)

        frequency = draw_slider("Frequency", 50, 100, frequency, 10, 100, 1)
        distance = draw_slider("Distance", 50, 200, distance, 1, 20, 1)
        timedelta = draw_slider("Time Delay", 50, 300, timedelta, 0, 10, 1)
        signal_strength = draw_slider("Signal Strength", 50, 400, signal_strength, 0, 100, 1)

        draw_button("Launch Key FRA Attack", 50, 500, 220, 40, RED, lambda: update_attack_result('key_fra'))
        draw_button("Launch Relay Attack", 300, 500, 220, 40, GREEN, lambda: update_attack_result('relay_attack'))

        # Display the results if available
        if key_fra_result is not None:
            draw_text(f"Key FRA Attack Prediction: {'Detected' if key_fra_result == 1 else 'Failure'}", FONT, RED, screen, 400, 200)
        if relay_attack_result is not None:
            draw_text(f"Relay Attack Prediction: {'Detected' if relay_attack_result == 1 else 'Failure'}", FONT, GREEN, screen, 400, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

def update_attack_result(attack_type):
    global key_fra_result, relay_attack_result
    if attack_type == 'key_fra':
        key_fra_result = launch_key_fra_attack()
    elif attack_type == 'relay_attack':
        relay_attack_result = launch_relay_attack()

if __name__ == "__main__":
    main()
