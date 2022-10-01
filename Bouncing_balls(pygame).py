import random, pygame,sys
from pygame.locals import *
(width, height) = (900, 900)
screen = pygame.display.set_mode((width, height))
keep_going=True
timer=pygame.time.Clock()
Q=100

colors = ['red','yellow','blue','cyan','brown','purple','light blue',\
          'black','navy','violet']
colors1=[0]*Q
for i in range(Q):
    colors1[i]=random.choice(colors)
dx,dy,r,x,y=[],[],[],[],[]

for m in range(Q):
    x.append(100)
    y.append(100)
    r.append(random.randint(10, 30))
    dx.append(random.randint(-10,10))
    dy.append(random.randint(-10,10))
    if dx[m]==0 or dy[m] == 0:
        dx[m] = random.randint(-8, 8)
        dy[m] = random.randint(-8, 8)

keep_going=True
while keep_going: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('green')
    for i in range(Q):
        (x[i], y[i]) = (x[i] + dx[i], y[i] + dy[i])
        if x[i] - r[i] < 0 or x[i] + r[i] > width: 
            dx[i] = -dx[i]
        if y[i] - r[i] < 0 or y[i] + r[i] > height: 
            dy[i] = -dy[i]
           
        pygame.draw.circle(screen, colors1[i],(x[i],y[i]), r[i])                  
    pygame.display.update()
    timer.tick(35)


    
