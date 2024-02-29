#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import numpy as np
import os
import grid

os.environ['SDL_VIDEO_CENTERED'] = '1'

width, height = 800,800 #your screen size
size = (width,height)

pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 200

black = (0,0,0)
blue = (0,14,71)
white = (255,255,255 )

scaler = 40
offset = 1

Grid = grid.Grid(width,height,scaler,offset)
Grid.random2d_array()

run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Grid.Conway(off_color = white, on_color = blue, surface = screen)
    
    pygame.display.update()

pygame.quit()


# In[ ]:





# In[ ]:





# In[ ]:




