import pygame, sys, random


#Balls function
def ball_properties():
    global ball_s_x, ball_s_y, p1_score, p2_score

    ball.x += ball_s_x
    ball.y += ball_s_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_s_y *= -1
    
    if ball.left <= 0: 
        ball_restart()
        p1_score += 1

    if ball.right >= screen_width:
        ball_restart()
        p2_score += 1
   

    if ball.colliderect(p1):
        ball_s_x *= -1
        p1_score += 1
    if ball.colliderect(p2):
        p2_score += 1
        ball_s_x *= -1

#P1
def p1_anim():
    p1.y += p1_speed

    if p1.top <= 0:
        p1.top = 0
    if p1.bottom >= screen_height:
        p1.bottom = screen_height
    
#P2
def p2_anim():
    p2.y += p2_speed

    if p2.top <= 0:
        p2.top = 0
    if p2.bottom >= screen_height:
        p2.bottom = screen_height

def ball_restart():
    global ball_s_x, ball_s_y
    ball.center = (screen_width/2, screen_height/2)
    ball_s_y *= random.choice((1, -1))
    ball_s_x *= random.choice((1, -1))



#Window
pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')



ball = pygame.Rect(screen_width/2 - 13, screen_height/2 - 13, 26, 26)
p1 = pygame.Rect(screen_width - 40, screen_height/2 - 60, 10, 120) 
p2 = pygame.Rect(30, screen_height/2 - 60, 10, 120)

p_col = (0, 255, 0)
bg_col = (0, 0, 0)

rand_col = 0

ball_s_x = 7 * random.choice((1, -1))
ball_s_y = 7 * random.choice((1, -1))
p1_speed = 0
p2_speed = 0

p1_score = 0
p2_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 32)

game_over_font = pygame.font.Font('freesansbold.ttf', 32)




#Main Loop 
while True:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                p1_speed += 7
            
            if event.key == pygame.K_r:
                p1_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_n:
                p1_speed -= 7
            
            if event.key == pygame.K_r:
                p1_speed += 7

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                p2_speed += 7
            
            if event.key == pygame.K_COMMA:
                p2_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_o:
                p2_speed -= 7
            
            if event.key == pygame.K_COMMA:
                p2_speed += 7
            
    #Controls and properties
    ball_properties()

    p1_anim()

    p2_anim()
    
    

    screen.fill(bg_col)

    pygame.draw.rect(screen, p_col, p1)
    pygame.draw.rect(screen, p_col, p2)
    pygame.draw.ellipse(screen, p_col, ball)
    pygame.draw.aaline(screen, p_col, (screen_width/2,0), (screen_width/2, screen_height))

    p1_text = game_font.render(f"{p1_score}", False, p_col)
    screen.blit(p1_text,(440, 300))

    p2_text = game_font.render(f"{p2_score}", False, p_col)
    screen.blit(p2_text,(340, 300))

    pygame.display.flip()

    clock.tick(60)





