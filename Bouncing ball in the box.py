import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Balls")

# Set up colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up rectangular box properties
box_pos=[width ,height]
box_center = [width // 2, height // 2]
box_posX=[0,width]
box_posY=[0,height]


# Set up ball properties
ball1_radius = 25
ball1_pos = [200,200]
ball1_vel = [5,5]
q1=1
q2=1


clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('green')

    # Update ball positions
    ball1_pos[0] += ball1_vel[0]
    ball1_pos[1] += ball1_vel[1]
    
   


    # Check for collision with circular box
    
    if ball1_pos[0]+70>= box_posX[1] or ball1_pos[0]+70<=140:
        ball1_vel[0]=-ball1_vel[0]
  
    if ball1_pos[1]-20< box_posY[0]+50 or ball1_pos[1]+70>box_posY[1]:
        ball1_vel[1]=-ball1_vel[1]

    # Draw rect box
    pygame.draw.rect(screen,'red',pygame.Rect(0,0,width,height),50)

    # Draw balls
    pygame.draw.circle(screen, BLUE, [int(ball1_pos[0]), int(ball1_pos[1])], ball1_radius)

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
