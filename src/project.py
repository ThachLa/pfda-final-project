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
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    game_over = False
    pipe_passed = False
    
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    clock = pygame.time.Clock()

    initial_delay = 1000 #1sec
    pygame.time.delay(initial_delay)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_speed = -bird_jump
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        bird_x = 100
                        bird_y = 300
                        bird_speed = 0 
                        pipe_x = WIDTH
                        pipe_height1 =  random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        pipe_height2 =  random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        score = 0
                        game_over = False
        if not game_over:
            screen.fill(WHITE)
            bird_speed += bird_gravity
            bird_y += bird_speed
            pipe_x -= pipe_speed
            draw_pipe(screen, pipe_x, pipe_height1, pipe_height2, pipe_width, HEIGHT)
            draw_bird(screen, bird_x, bird_y,bird_width, bird_height)
            if pipe_x <= -pipe_width:
                pipe_x = WIDTH
                pipe_height1 =  random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                pipe_height2 =  random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                pipe_passed = False
            if bird_y + bird_height >= HEIGHT or bird_y <=0:
                game_over = True
            if bird_x +bird_y > pipe_x and bird_x < pipe_x + pipe_width:
                if bird_y < pipe_height1 or bird_y + bird_height > pipe_height1 + 150:
                    game_over = True
                if bird_y < pipe_height2 or bird_y + bird_height > pipe_height2 + 150:
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
                        pipe_height1 =  random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        pipe_height2 =  random.randint(MIN_PIPE_GAP, MAX_PIPE_GAP)
                        score = 0
                        game_over = False
        show_score(screen, font, score)
        pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - 50, WIDTH, 50))
        pygame.display.update()
        clock.tick(30)                
def draw_bird(screen, x, y, width, height):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
def draw_pipe(screen, x, height1, height2, width, screen_height):
    pygame.draw.rect(screen, (0, 128, 0), (x, 0, width, height1))
    pygame.draw.rect(screen, (0, 128, 0), (x,height2 + 150, width, screen_height - height2 - 150))
def show_score(screen, font, score):
    text = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(text, (10,10))
def game_over_screen(screen, width, height):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(text, (width // 2-80, height // 2-30))
    text = font.render("Press R to restart", True, (255, 255, 255))
    screen.blit(text, (width //2-120, height // 2+30))

if __name__ == "__main__":
    main()