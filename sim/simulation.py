# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:14:15 2020

@author: sgnodde
"""

import pygame as pg
from sys import exit
from epidem.locations.map import BasicMap
from epidem.time.clock import Clock
import datetime as dt

class Sim:
    
    def __init__(self, initial_city, clock = Clock(start_date_time=dt.datetime(2020,1,1)), 
                 disp_width = 800, disp_height = 600,
                 blocks = (4,3), anderhalfmeter = 15, speed = 10, dotwidth = 6,
                 ill_time = dt.timedelta(days = 5),
                 infectious_time = dt.timedelta(days = 5),
                 time_increment = dt.timedelta(days = 1),
                 col_nothing = (255, 255, 255),
                 col_infected = [0, 0, 255],
                 col_background = [0,0,0],
                 col_ill = [0,255,0],
                 col_infectious = [200,100,100]):
        self.initial_city = initial_city
        self.disp_width = disp_width
        self.disp_height = disp_height
        self.gameDisplay = pg.display.set_mode((self.disp_width,self.disp_height))
        self.col_nothing = col_nothing
        self.col_background = col_background
        self.col_infected = col_infected
        self.col_infectious = col_infectious
        self.col_ill = col_ill
        self.blocks = blocks
        self.anderhalfmeter = anderhalfmeter
        self.speed = speed
        self.dotwidth = dotwidth
        self.clock = clock
        self.time_increment = time_increment
        self.ill_time = ill_time
        self.infectious_time = infectious_time
        

    def run_sim(self):
    
        pg.init()
        
        crashed = False
                
        pg.display.set_caption('Epidemic simulation')
        
        gameclock = pg.time.Clock()
        
        
        
        cmap = BasicMap(self.initial_city, self.disp_width, self.disp_height,
                            blocks = self.blocks)
        
        while not crashed:
            self.gameDisplay.fill(self.col_background)
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
                        person.check_ill(ill_time = self.ill_time)
                        person.check_infectious(infectious_time = self.infectious_time)
                        self.plot_dot(person)
                        person.location.update_location_basic(self.speed)
                        if person.infectious:
                            for person2 in cmap.allocated_city[i][j]:
                                dist = self.distance(person, person2) 
                                if dist < self.anderhalfmeter and dist > 0:
                                    person2.touch()
                    
            # for person in cmap.city:
            #     self.plot_dot(person)
            #     person.location.update_location_basic(speed)
                
            
            pg.display.update()
            gameclock.tick(10)
            self.clock.add_time(self.time_increment)
            
    def plot_dot(self, person):
        #gameDisplay.blit()
        if person.ill:
            color = self.col_ill
        elif person.infectious:
            color = self.col_infectious
        elif person.infected:
            color = self.col_infected
        else:
            color = self.col_nothing
        pg.draw.circle(self.gameDisplay, color,
                       [int(person.location.loc[0]), int(person.location.loc[1])], self.dotwidth)
        
    def distance(self, person1, person2):
        
        xdist = person1.location.loc[0] - person2.location.loc[0]
        ydist = person1.location.loc[1] - person2.location.loc[1]
        
        return xdist**2 + ydist**2
