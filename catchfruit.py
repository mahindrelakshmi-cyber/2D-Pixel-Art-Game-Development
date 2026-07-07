import pygame, random

# 1. Initialize Pygame
pygame.init()

# 2. Create game window
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Catch the Fruit")

# 3. Load images
basket_img = pygame.image.load("basket.png")
basket_img = pygame.transform.scale(basket_img, (100, 20))
basket = basket_img.get_rect()
basket.x, basket.y = 250, 350

apple_img = pygame.image.load("apple.png")
banana_img = pygame.image.load("banana.png")
orange_img = pygame.image.load("orange.png")

apple_img = pygame.transform.scale(apple_img, (40, 40))
banana_img = pygame.transform.scale(banana_img, (40, 40))
orange_img = pygame.transform.scale(orange_img, (40, 40))

background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, (600, 400))

start_img = pygame.image.load("start.png")
start_img = pygame.transform.scale(start_img, (600, 400))

gameover_img = pygame.image.load("gameover.png")
gameover_img = pygame.transform.scale(gameover_img, (600, 400))

# 4. Fruits setup
def create_fruits():
    return [
        {"rect": pygame.Rect(random.randint(0, 560), 0, 40, 40), "image": apple_img},
        {"rect": pygame.Rect(random.randint(0, 560), -100, 40, 40), "image": banana_img},
        {"rect": pygame.Rect(random.randint(0, 560), -200, 40, 40), "image": orange_img}
    ]

fruits = create_fruits()

# 5. Clock and score
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

# 6. Start screen loop
start_screen = True
running = False
while start_screen:
    screen.blit(start_img, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_screen = False
            running = True

# 7. Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.x > 0:
        basket.x -= 5
    if keys[pygame.K_RIGHT] and basket.x < 500:
        basket.x += 5

    for fruit in fruits:
        fruit["rect"].y += 5
        if fruit["rect"].y > 400:
            fruit["rect"].y = 0
            fruit["rect"].x = random.randint(0, 560)

    for fruit in fruits:
        if basket.colliderect(fruit["rect"]):
            score += 1
            fruit["rect"].y = 0
            fruit["rect"].x = random.randint(0, 560)

    # Drawing everything
    screen.blit(background_img, (0, 0))
    screen.blit(basket_img, basket)
    for fruit in fruits:
        screen.blit(fruit["image"], fruit["rect"])
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(30)

# 8. Game Over screen
game_over = True
while game_over:
    screen.blit(gameover_img, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Reset game
            score = 0
            fruits = create_fruits()
            basket.x, basket.y = 250, 350
            game_over = False
            running = True

            # Restart game loop
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT] and basket.x > 0:
                    basket.x -= 5
                if keys[pygame.K_RIGHT] and basket.x < 500:
                    basket.x += 5

                for fruit in fruits:
                    fruit["rect"].y += 5
                    if fruit["rect"].y > 400:
                        fruit["rect"].y = 0
                        fruit["rect"].x = random.randint(0, 560)

                for fruit in fruits:
                    if basket.colliderect(fruit["rect"]):
                        score += 1
                        fruit["rect"].y = 0
                        fruit["rect"].x = random.randint(0, 560)

                screen.blit(background_img, (0, 0))
                screen.blit(basket_img, basket)
                for fruit in fruits:
                    screen.blit(fruit["image"], fruit["rect"])
                text = font.render(f"Score: {score}", True, (0, 0, 0))
                screen.blit(text, (10, 10))
                pygame.display.flip()
                clock.tick(30)

pygame.quit()
