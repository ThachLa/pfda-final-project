import pygame
import sys
import random

def main():
    #Constants
    WIDTH, HEIGHT = 400, 600
    WHITE = (255, 255, 255)
    GROUND_COLOR = (0, 128, 0)
    pipe_width = 80
    MIN_PIPE_GAP = 100
    MAX_PIPE_GAP = 200
    bird_x = 100
    bird_y = 300
    bird_width = 30
    bird_height = 30
    bird_speed = 0
    bird_jump = 5
    bird_gravity = 0.3
    pipe_height1 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
    pipe_height2 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
    pipe_x = WIDTH
    pipe_speed = 3
    score = 0
    font = pygame.font.Font(None, 36)
    game_over = False
    pipe_passed = False
    
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    clock = pygame.time.Clock()

    initial_delay = 1000 #1sec
    pygame.time.delay(initial_delay)
def draw_bird(screen, x, y, width, height):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
def draw_pipe(screen, x, height1, height2, width, screen_height):
    pygame.draw.rect(screen, (0, 128, 0), (x, 0, width, height1))
    pygame.draw.rect(screen, (0, 128, 0), (x,height2 + 150, width, screen_height - height2 - 150))

    
    