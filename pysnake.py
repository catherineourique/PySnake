import pygame
import random

pygame.init()

screen_width=800
screen_height=800

screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()

fps=30

is_running=True

ng_x=10
ng_y=10

npx_x=screen_width/ng_x
npx_y=screen_height/ng_y

def StartGame(ng_x, ng_y):
    snake=[[int(ng_x/2), int(ng_y/2)], [int(ng_x/2)+1, int(ng_y/2)], [int(ng_x/2)+1, int(ng_y/2)+1],
            [int(ng_x/2)+2, int(ng_y/2)+1], [int(ng_x/2)+2, int(ng_y/2)+2]]

    apple=[int(random.random()*ng_x), int(random.random()*ng_y)]
    direction=[1,0]
    return snake,apple, direction
    
snake,apple,direction=StartGame(ng_x,ng_y)


frames_to_move=15
snake_frame=0

should_reset=False

while is_running:
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    snake_frame+=1
    
    keys=pygame.key.get_pressed()
    dx=keys[pygame.K_d]-keys[pygame.K_a]
    dy=keys[pygame.K_s]-keys[pygame.K_w]
    if (dx or dy) and not (abs(dx) > 0.5 and abs(dy) > 0.5) and not (direction[0]==-dx) and not (direction[1]==-dy):
        direction[0]=dx
        direction[1]=dy


    if snake_frame > frames_to_move:
        snake_frame=0
        head=[snake[-1][0]+direction[0], snake[-1][1]+direction[1]]
        if not head==apple:
            snake.pop(0)
        else:
            apple=[int(random.random()*ng_x), int(random.random()*ng_y)]

        for body in snake:
            if body==head:
                should_reset=True
                
        if head[0] >= ng_x or head[0] < 0 or head[1] >= ng_y or head[1] < 0:
            should_reset=True
            
        snake.append(head)
        
    should_reset+=keys[pygame.K_r]
        
    if should_reset:
        snake,apple,direction=StartGame(ng_x,ng_y)
        should_reset=False
        
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen,(255,0,0),(apple[0]*npx_x,apple[1]*npx_y,npx_x,npx_y))
    
    for body in snake:
        pygame.draw.rect(screen,(0,200,0),(body[0]*npx_x,body[1]*npx_y,npx_x,npx_y))
    pygame.display.flip()
    
pygame.quit()
