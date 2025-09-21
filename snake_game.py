import pygame
import random

pygame.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Creating Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

#Background Image
bgimg = pygame.image.load("snake_background.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game by Ahad")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text , color, x, y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color , [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome to the Snake Game by AHAD", black, 100 , 250)
        text_screen("Press Space Bar To Play", black, 200 , 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)      
                                                            
# Game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 60
    velocity_x = 4
    velocity_y = 4
    score = 0
    init_velocity = 3
    food_x = random.randint(20, screen_width) 
    food_y = random.randint(20, screen_height)
    snk_list=[]
    snk_length= 1
    with open("High_Score.txt","r") as f:
        high_score = f.read()

    while not exit_game:
        if game_over:
            with open("High_Score.txt", "w") as f:
                f.write(str(high_score))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity 
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
            
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs(snake_x- food_x)<6 and abs(snake_y-food_y)<6:
                score +=1
                print("Score:", score)
                food_x = random.randint(20, screen_width) 
                food_y = random.randint(20, screen_height)
                snk_length +=5
                if score>int(high_score):
                    high_score = score
            
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score:"+ str(score) + "  High_Score:  "+str(high_score) ,red,5,5)
            pygame.draw.rect(gameWindow, red , [food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            
            if head in snk_list[:-1]:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()