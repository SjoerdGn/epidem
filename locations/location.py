import numpy as np
from scipy.stats import norm
class Location:
    """
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def generate_location_basic(self):
        """Generate a basic location.
        

        Parameters
        ----------
        width : int
            Width of frame.
        height : int
            Height of frame.

        Returns
        -------
        xloc : flaot
            x-location.
        yloc : float
            y-location.

        """
        xloc = np.random.rand(1)*self.width
        yloc = np.random.rand(1)*self.height
        self.loc = (xloc[0], yloc[0])
        return xloc[0], yloc[0]
    
    def update_location_basic(self, speed):
        """
        

        Parameters
        ----------
        speed : TYPE
            DESCRIPTION.

        Returns
        -------
        xloc : TYPE
            DESCRIPTION.
        yloc : TYPE
            DESCRIPTION.

        """
        xloc = self.loc[0]
        yloc = self.loc[1]
        xloc += norm.ppf(np.random.rand(1)[0])*speed
        yloc += norm.ppf(np.random.rand(1)[0])*speed
        if xloc >= self.width:
            xloc = self.width-0.001
        if yloc >= self.height:
            yloc = self.height-0.001
        if xloc < 0:
            xloc = 0
        if yloc < 0:
            yloc = 0
    
        
        self.loc = (xloc, yloc)
        return xloc, yloc