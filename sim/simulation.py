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
                 blocks = (4,3), anderhalfmeter = 15, speed = 10, dotwidth = 6):
        self.initial_city = initial_city
        self.disp_width = disp_width
        self.disp_height = disp_height
        self.gameDisplay = pg.display.set_mode((self.disp_width,self.disp_height))
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.blue = [0, 0, 255]
        self.blocks = blocks
        self.anderhalfmeter = anderhalfmeter
        self.speed = speed
        self.dotwidth = dotwidth

    def run_sim(self):
    
        pg.init()
        
        crashed = False
                
        pg.display.set_caption('Epidemic simulation')
        
        clock = pg.time.Clock()
        
        
        
        cmap = BasicMap(self.initial_city, self.disp_width, self.disp_height,
                            blocks = self.blocks)
        
        while not crashed:
            self.gameDisplay.fill(self.black)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    crashed = True
                    pg.quit()
                    exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        self.speed += 1
                        print(f"Speed up to {self.speed}")
                    if event.key == pg.K_DOWN:
                        self.speed = self.speed -1
                        print(f"Speed down to {self.speed}")
                    
                if self.speed < 0:
                    self.speed = 0
                    
                print(event)
                
            cmap.xsys()
            cmap.allocate()
            for i in range(cmap.blocks[0]):
                for j in range(cmap.blocks[1]):
                    for person in cmap.allocated_city[i][j]:
                        self.plot_dot(person)
                        person.location.update_location_basic(self.speed)
                        if person.infected:
                            for person2 in cmap.allocated_city[i][j]:
                                dist = self.distance(person, person2) 
                                if dist < self.anderhalfmeter and dist > 0:
                                    person2.infected = True
                    
            # for person in cmap.city:
            #     self.plot_dot(person)
            #     person.location.update_location_basic(speed)
                
            
            pg.display.update()
            clock.tick(10)
            
    def plot_dot(self, person):
        #gameDisplay.blit()
        if person.infected:
            color = self.blue
        else:
            color = self.white
        pg.draw.circle(self.gameDisplay, color,
                       [int(person.location.loc[0]), int(person.location.loc[1])], self.dotwidth)
        
    def distance(self, person1, person2):
        
        xdist = person1.location.loc[0] - person2.location.loc[0]
        ydist = person1.location.loc[1] - person2.location.loc[1]
        
        return xdist**2 + ydist**2
