import sys
import pygame
import numpy as np
import matplotlib.pyplot as plt

class Cell:
    def __init__(self):
        self.position = [0,0] #this is RELATIVE to the center of the Bloom.
        self.image = pygame.image.load("intro_ball.gif")
        self.rect = self.image.get_rect()

class Bloom:
    def __init__(self,position):
        self.center = position
        self.stemimage = pygame.image.load("BW_ball.gif")
        self.stemrect = self.stemimage.get_rect()
        self.cells = []
        
    def draw(self,surface):
        # draw the stem cell
        surface.blit(self.stemimage, self.stemrect)
        # draw all daughter cells (RELATIVE to self.center)
        for cell in self.cells:
            surface.blit(cell.image,cell.rect)
        
    def update(self,dt):
        #this just updates the position of all the components relative to center.
        self.stemrect.center = self.center
        for cell in self.cells:
            cell.rect.center = [cell.position[0]+self.center[0] , cell.position[1]+self.center[1]]
            
    def add_cell(self,position):
        new_cell = Cell()
        new_cell.position = position
        self.cells.append(new_cell)
        
    # TO DO: add a method for dividing in a direction, at the edge of the stem cell.
    
    