import sys, pygame, math, random, pygame.gfxdraw, pygame.transform
class Ball:
    image = pygame.image.load("simple_seed.png")
    image_original = image
    bouncemod = 0.9
    size = 1
    def __init__(self,x,y,dx,dy):
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect = self.rect.move([x,y])
        self.dx = dx
        self.dy = dy
        self.image_width = self.rect.width
        self.angle = 0
        
    def __str__(self):
        return f"({self.rect.x},{self.rect.y})"

    def set_image(self,filepath):
        self.image = pygame.image.load(filepath)
        self.image_original = self.image
        center = self.get_center()
        self.rect = self.image.get_rect()
        self.set_center(center[0],center[1])
    
    def clone(self):
        newball = Ball(self.rect.x,self.rect.y,self.dx,self.dy)
        newball.size = self.size
        return newball
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_x_center(self):
        return self.x + self.rect.width/2
        #return self.rect.centerx #THIS IS VERY WRONG
    
    def get_y_center(self):
        return self.y + self.rect.height/2
        #return self.rect.centery #THIS IS VERY WRONG
    
    def get_center(self):
        return (self.get_x_center(),self.get_y_center())
    
    def get_radius_inner(self):
        return self.get_x_center()-self.get_x()

    def set_radius_inner(self,radius):
        factor = (radius)/self.image_width
        self.resize(factor)
    
    def set_x(self,x):
        self.x = x
        self.rect.x = x
        
    def set_y(self,y):
        self.y = y
        self.rect.y = y
        
    def set_center(self,x,y):
        #each coordinate is a radius less
        radius = self.get_radius_inner()
        self.set_x(x-radius)
        self.set_y(y-radius)

    def move(self,dt):
        self.x += self.dx * dt
        self.rect.x = self.x
        self.y += self.dy * dt
        self.rect.y = self.y
        
    def collide(self,xmin,xmax,ymin,ymax):
        if self.get_x() <= xmin:
            self.set_x(0)
            self.dx = abs(self.dx*self.bouncemod)
        if self.get_x() >= xmax-self.rect.width:
            self.set_x(xmax-self.rect.width)
            self.dx = -abs(self.dx*self.bouncemod)
        if self.get_y() <= ymin:
            self.set_y(0)
            self.dy = abs(self.dy*self.bouncemod)
        if self.get_y() >= ymax-self.rect.height:
            self.set_y(ymax-self.rect.height)
            self.dy = -abs(self.dy*self.bouncemod)
            
    def resize(self,factor):
        #Sets The Size of the rect and the image RELATIVE to a factor of it's ORIGINAL SIZE. Keeps the center of the object the same. 
        angle = self.angle
        self.size = factor
        center = self.get_center()
        self.image = pygame.transform.scale_by(self.image_original,self.size) #the image needs to be a scaled version of its original. #PROBLEM??
        self.rect = self.image.get_rect()
        self.set_center(center[0],center[1])
        self.rotate_point(center,angle)
        
    def vector(self):#TODO: NORMALIZE THIS? or not. 
        return [self.dx,self.dy]

    def rotate_point(self,point,angle):
        self.angle = angle
        center = self.get_center()
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.set_center(center[0],center[1])