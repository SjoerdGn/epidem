# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:56:44 2020

@author: sgnodde
"""

import datetime as dt


class Clock:
    
    
    def __init__(self, start_date_time = dt.datetime(2020,1,1)):
        self.date_time = start_date_time

    def add_time(self, timediff = dt.timedelta(days = 1)):
        """Adds time to clock.
        

        Parameters
        ----------
        timediff : datetime.timedelta, optional
            Time added to clock. The default is dt.timedelta(days = 1).

        Returns
        -------
        datetime.datetime
            Time right now.

        """
        self.date_time = self.date_time + timediff
        return self.date_time
    