import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1000, 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Driving Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Car properties
car_width = 73
car_height = 82

# Obstacle properties
obstacle_width = 80
obstacle_height = 80

# Load car image
car_img = pygame.image.load("img/car.png")
obstacle_img = pygame.image.load("img/obstacle.png")
road_img = pygame.image.load("img/road.png")

# Function to display the car on the screen
def car(x, y):
    display.blit(car_img, (x, y))
    
def obstacle(x, y):
    display.blit(obstacle_img, (x, y))

# Function to display text on the screen
def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

# Function to display a message on the screen
def message_display(text):
    large_text = pygame.font.Font("freesansbold.ttf", 60)
    text_surface, text_rect = text_objects(text, large_text)
    text_rect.center = (width / 2, height / 2)
    display.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Display the message for 2 seconds
    game_loop()

# Game loop
def game_loop():
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0
    y_change = 0

    obstacle_width = 50
    obstacle_height = 50
    obstacle_x = random.randint(1, width - obstacle_width)
    obstacle_y = -600
    obstacle_speed = 0.40
    car_speed = 0.50

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Handling key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_speed
               	elif event.key == pygame.K_RIGHT:
                    x_change = car_speed
                elif event.key == pygame.K_UP:
                    y_change = -car_speed
                elif event.key == pygame.K_DOWN:
                    y_change = car_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        display.blit(road_img, (0,0))

        # Move and draw the obstacle
        obstacle_y += obstacle_speed
        display.blit(obstacle_img, (obstacle_x, obstacle_y))

        # Draw the car
        car(x, y)

        # Check for collision
        if y < obstacle_y + obstacle_height:
            if x < obstacle_x + obstacle_width and x + car_width > obstacle_x:
                if y + car_height < obstacle_y:
                    # Car is above the obstacle, no collision
                    pass
                else:
                    message_display("Game Over")
	# Check if the obstacle has reached the bottom of the screen
        if obstacle_y > height:
            obstacle_y = 0 - obstacle_height
            obstacle_x = random.randint(0, width - obstacle_width)
        pygame.display.update()

# Start the game
game_loop()

