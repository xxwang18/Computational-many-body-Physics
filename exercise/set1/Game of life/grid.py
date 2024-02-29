#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pygame
import numpy as np
import random

class Grid:
    def __init__(self,width,height,scale,offset):
        self.scale = scale  # the size of a single square in grid
        self.columns = int(height/scale) # height/scale = 800/40 = 20
        self.rows = int(width/scale) # width/scale = 800/40 = 20
        self.size = (self.rows,self.columns)
        self.grid_array = np.zeros(shape=(self.size)) #establish the nparray with the size 20*20
        self.offset = offset
        self.question_c_count =[0] # the list for cell number for generations
        self.generation = 0 # the current generation
        
    def random2d_array(self): # not necessary in assignment
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)
                
    def set_array(self,x,y):  # create a living cell at position (x,y)
        self.grid_array[x][y] = 1
        
    def question_a_1(self): # pattern 1 in question a
        self.set_array(5,5)
        self.set_array(6,5)
        self.set_array(5,6)
        self.set_array(6,6)
    
    def question_a_2(self):# pattern 2 in question a
        self.set_array(15,6)
        self.set_array(15,4)
        self.set_array(14,5)
        self.set_array(16,5)
    
    def question_a_3(self):# pattern 3 in question a
        self.set_array(5,15)
        self.set_array(4,15)
        self.set_array(6,15)
        
    def question_a_4(self):# pattern 4 in question a
        self.set_array(15,15)
        self.set_array(15,16)
        self.set_array(16,15)
        self.set_array(16,16)
        self.set_array(17,16)
        self.set_array(14,15)
    def question_b(self): # the pattern in question b
        self.set_array(12,11)
        self.set_array(13,12)
        self.set_array(13,13)
        self.set_array(12,13)
        self.set_array(11,13)
     
    def diehard(self):# 'diehard' pattern
        self.set_array(8,10)
        self.set_array(7,10)
        self.set_array(8,11)
        
        self.set_array(12,11)
        self.set_array(13,11)
        self.set_array(14,11)
        self.set_array(13,9)
    
    def Conway(self, off_color, on_color, surface): # on_color is black here ,off_color is white
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos = x*self.scale
                y_pos = y*self.scale
                
                if self.grid_array[x][y] == 1:
                    self.question_c_count[self.generation]+=1
                    pygame.draw.rect(surface,on_color,[x_pos,y_pos,self.scale-self.offset,self.scale-self.offset])
                else:
                    pygame.draw.rect(surface,off_color,[x_pos,y_pos,self.scale-self.offset,self.scale-self.offset])
        next = np.ndarray(shape=(self.size))
        self.generation+=1
        self.question_c_count.append(0)
        
        for x in range(self.rows):  # the rule of Conway game of life
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x,y)
                if state == 0 and neighbours == 3: # if the cell is dead and the number of neighbours are 3, the cell will alive
                    next[x][y] = 1
                elif state == 1 and (neighbours<2 or neighbours >3):# if the cell is living and is underpopulation or overpopulation, turn to dead
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next
    def get_neighbours(self,x,y): # get the number of neighbours in period boundary contion
        total = 0
        for n in range(-1,2):
            for m in range(-1,2):
                x_edge = (x+n+self.rows)%self.rows 
                y_edge = (y+m+self.columns)%self.columns
                total += self.grid_array[x_edge,y_edge]
        
        total -= self.grid_array[x][y]
        return total


# In[ ]:




