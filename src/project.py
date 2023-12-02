import pygame
import sys
import random

def main():
    # Constants
    WIDTH, HEIGHT = 400, 600
    WHITE = (255, 255, 255)
    GROUND_COLOR = (0, 128, 0)
    pipe_width = 80
    MIN_PIPE_GAP = 200
    MAX_PIPE_GAP = 300
    bird_x = 100
    bird_y = 300
    bird_size = 30
    bird_speed = 0
    bird_jump = 5
    bird_gravity = 0.3
    pipe_height1 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
    pipe_height2 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
    pipe_x = WIDTH
    pipe_speed = 3
    score = 0
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    game_over = False
    pipe_passed = False
    wings_flap_counter = 0
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    clock = pygame.time.Clock()

    initial_delay = 1000  # 1 sec
    pygame.time.delay(initial_delay)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_speed = -bird_jump
                        wings_flap_counter = 15 
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        bird_x = 100
                        bird_y = 300
                        bird_speed = 0
                        pipe_x = WIDTH
                        pipe_height1 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        pipe_height2 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        score = 0
                        game_over = False
        if not game_over:
            screen.fill(WHITE)
            bird_speed += bird_gravity
            bird_y += bird_speed
            pipe_x -= pipe_speed
            draw_pipe(screen, pipe_x, pipe_height1, pipe_height2, pipe_width, HEIGHT)
            draw_bird(screen, bird_x, bird_y, bird_size, wing_flap_counter)
            if pipe_x <= -pipe_width:
                pipe_x = WIDTH
                pipe_height1 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                pipe_height2 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                pipe_passed = False
            if bird_y + bird_size >= HEIGHT or bird_y <= 0:
                game_over = True
            if bird_x + bird_size > pipe_x and bird_x < pipe_x + pipe_width:
                if bird_y < pipe_height1 or bird_y + bird_size > pipe_height1 + 150:
                    game_over = True
                if bird_y < pipe_height2 or bird_y + bird_size > pipe_height2 + 150:
                    game_over = True
            if pipe_x + pipe_width < bird_x and not pipe_passed:
                score += 1
                pipe_passed = True
        if game_over:
            game_over_screen(screen, WIDTH, HEIGHT)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        bird_x = 100
                        bird_y = 300
                        bird_speed = 0
                        pipe_x = WIDTH
                        pipe_height1 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        pipe_height2 = random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        score = 0
                        game_over = False
        show_score(screen, font, score)
        pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - 50, WIDTH, 50))
        pygame.display.update()
        clock.tick(30)
        wings_flap_counter = max(0, wings_flap_counter - 1)

def draw_bird(screen, x, y, size, wing_flap_counter):
    body_color = (255, 255, 0)  # Yellow color for the body
    wing_color = (255, 0, 0)   # Red color for the wings
    beak_color = (255, 165, 0)  # Orange color for the beak
    #Body
    pygame.draw.circle(screen, body_color, (x + size // 2, y + size // 2), size // 2)
    #WingFlap
    wing_offset = size // 4
    wing_up_y = y + 2 *size // 3 - wing_flap_counter
    #Wing
    pygame.draw.polygon(screen, wing_color, [(x + size // 2, wing_up_y), (x + size // 4, wing_up_y - size // 4), (x + 3 * size // 4, wing_up_y - size // 4)])
    #Beak
    beak_size = size // 6
    beak_x = x + size
    beak_y = y + size // 2 - beak_size // 2
    pygame.draw.polygon(screen, beak_color, [(beak_x, beak_y), (beak_x + beak_size, beak_y + beak_size // 2), (beak_x, beak_y + beak_size)])
def draw_pipe(screen, x, height1, height2, width, screen_height):
    pygame.draw.rect(screen, (0, 128, 0), (x, 0, width, height1))
    pygame.draw.rect(screen, (0, 128, 0), (x, height2 + 150, width, screen_height - height2 - 150))

def show_score(screen, font, score):
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

def game_over_screen(screen, width, height):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, (width // 2 - 80, height // 2 - 30))
    text = font.render("Press R to restart", True, (255, 255, 255))
    screen.blit(text, (width // 2 - 120, height // 2 + 30))

if __name__ == "__main__":
    main()