# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:14:15 2020

@author: sgnodde
"""

import pygame as pg
from sys import exit
from epidem.locations.map import BasicMap


class Sim:
    
    def __init__(self, initial_city, disp_width = 800, disp_height = 600,
                 blocks = (4,3)):
        self.city = initial_city
        self.disp_width = disp_width
        self.disp_height = disp_height
        self.gameDisplay = pg.display.set_mode((self.disp_width,self.disp_height))
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = [0, 0, 255]
        self.blocks = blocks

    def run_sim(self):
    
        pg.init()
        
        crashed = False
                
        pg.display.set_caption('Epidemic simulation')
        
        clock = pg.time.Clock()
        
        speed = 20
        
        while not crashed:
            self.gameDisplay.fill(self.black)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    crashed = True
                    pg.quit()
                    exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        speed += 1
                        print(f"Speed up to {speed}")
                    if event.key == pg.K_DOWN:
                        speed = speed -1
                        print(f"Speed down to {speed}")
                    
                if speed < 0:
                    speed = 0
                    
                print(event)
                
            cmap = BasicMap(self.city, self.disp_width, self.disp_height,
                            blocks = self.blocks)
                
            for person in self.city:
                self.plot_dot(int(person.location.loc[0]), int(person.location.loc[1]))
                person.location.update_location_basic(speed)
                
            
            pg.display.update()
            clock.tick(10)
            
    def plot_dot(self, x,y):
        #gameDisplay.blit()
        pg.draw.circle(self.gameDisplay, self.white, [x, y], 2)
