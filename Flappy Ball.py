import pgzrun,random
TITLE="Flappy Ball"
WIDTH=800
HEIGHT=800
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

pgzrun.go()