import pgzrun,random
TITLE="Flappy Ball"
WIDTH=800
HEIGHT=600
R=random.randint(0,255)
G=random.randint(0,255)
B=random.randint(0,255)
CLR=R,G,B 
GRAVITY=2000 #Pixels per second
#Class is a blueprint of an object
#Object is an instance of class
class Ball:
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
        self.vx=200 #Velocity on x-axis
        self.vy=0 #Velocity on y-axis
        self.radius=10
    def draw(self):
        pos=((self.x,self.y))
        screen.draw.filled_circle(pos,self.radius,CLR)
ball= Ball(100,0)
def draw():
    screen.clear()
    ball.draw()
def update(dt):
    u=ball.vy
    #Constant acceleration formula
    ball.vy+=GRAVITY*dt
    ball.y+=(u+ball.vy)*0.5*dt
    if ball.y > HEIGHT - ball.radius:
        ball.y= HEIGHT - ball.radius
        ball.vy= -ball.vy*0.9 #inelastic collision
    ball.x+=ball.vx*dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx= -ball.vx
def on_key_down(key):
    if key==keys.SPACE:
        ball.vy= -500




pgzrun.go()
