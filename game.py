#!/usr/bin/env python3
import pygame
import random

# Initialize pygame
pygame.init()

# Set screen size and title
screen_width = 2000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Pygame")

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Define tile size
tile_size = 20

# Define map size
map_width = 100
map_height = 50

# Define player size and position
player_size = 40
player_pos = [screen_width / 2, screen_height / 2]

# Define enemy size and position
enemy_size = 20
enemy_pos = [random.randint(0, map_width) * tile_size, random.randint(0, map_height) * tile_size]
enemies = [enemy_pos]
for i in range(9):
    enemy_x = random.randint(0, map_width) * tile_size
    enemy_y = random.randint(0, map_height) * tile_size
    enemy_pos = [enemy_x, enemy_y]
    enemies.append(enemy_pos)

# Define enemy movement
enemy_movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# Define game loop
game_over = False

clock = pygame.time.Clock()

# Define life counter
lives = 3

# Define font
font = pygame.font.SysFont("Arial", 25)

# Define function to draw text
def draw_text(text, color, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_obj, text_rect)

# Define function for collision detection
def collision_detection(player_rect, enemy_list):
    global lives
    for enemy_pos in enemy_list:
        enemy_rect = pygame.Rect(enemy_pos[0] - enemy_size, enemy_pos[1] - enemy_size, enemy_size * 2, enemy_size * 2)
        if player_rect.colliderect(enemy_rect):
            lives -= 1

# Game loop
while True: 

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= tile_size
    elif keys[pygame.K_RIGHT] and player_pos[0] < screen_width - player_size:
        player_pos[0] += tile_size
    elif keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= tile_size
    elif keys[pygame.K_DOWN] and player_pos[1] < screen_height - player_size:
        player_pos[1] += tile_size

    # Move enemies
    for enemy in enemies:
        enemy_direction = random.choice(enemy_movement)
        enemy[0] += enemy_direction[0] * tile_size * 5
        enemy[1] += enemy_direction[1] * tile_size * 5

        # Bounce from bounding box
        if enemy[0] < 0 or enemy[0] > screen_width:
            enemy_direction[0] *= -1
        if enemy[1] < 0 or enemy[1] > screen_height:
            enemy_direction[1] *= -1

    # Fill screen with white
    screen.fill(white)

    # Draw map
    for row in range(map_height):
        for column in range(map_width):
            rect = pygame.Rect(column * tile_size, row * tile_size, tile_size, tile_size)
            pygame.draw.rect(screen, white, rect)

    # Draw player
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    pygame.draw.rect(screen, red, player_rect)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.circle(screen, blue, (enemy[0], enemy[1]), enemy_size)

    # Check for collisions
    collision_detection(player_rect, enemies)

    # Draw life counter
    draw_text(f"Lives: {lives}", green, screen_width - 100, 20)

    # Check for game over
    if lives == 0:
        game_over = True
        screen.fill(white)
        draw_text("Game Over", red, screen_width / 2 - 50, screen_height / 2 - 50)
        draw_text("Press R to Restart", red, screen_width / 2 - 100, screen_height / 2)

    # Update screen
    pygame.display.update()

    # Set FPS
    clock.tick(30)

    # Check for game over restart
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        game_over = False
        lives = 3
        player_pos = [screen_width / 2, screen_height / 2]
        enemies = [enemy_pos]
        for i in range(9):
            enemy_x = random.randint(0, map_width) * tile_size
            enemy_y = random.randint(0, map_height) * tile_size
            enemy_pos = [enemy_x, enemy_y]
            enemies.append(enemy_pos)
    if keys[pygame.K_q]:
        # Quit pygame
        pygame.quit()
