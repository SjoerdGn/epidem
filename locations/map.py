import numpy as np

class BasicMap:
    
    
    def __init__(self, city, disp_width, disp_height, blocks = (4,3)):
        
        self.city = city
        self.disp_width = disp_width
        self.disp_height = disp_height
        self.blocks = blocks
        self.limits = (np.linspace(0,disp_width,blocks[0]+1), 
                       np.linspace(0,disp_height,blocks[1]+1))
        self.xsys_formed = False
        self.allocated_city = [[[] for i in range(self.blocks[1])] for j in range(self.blocks[0])]
        
        
    def xsys(self):
        city = self.city
        xs = np.zeros(len(city))
        ys = np.zeros(len(city))
        for i in range(len(city)):
            xs[i], ys[i] = city[i].location.loc
        self.xs = xs
        self.ys = ys
        self.xsys_formed = True
    
    def allocate(self):
        
        
        if self.xsys_formed:
            indsx = np.digitize(self.xs, self.limits[0])
            indsy = np.digitize(self.ys, self.limits[1])
            self.indsx = indsx-1
            self.indsy = indsy-1
            
            
        
        else:
            raise ValueError("xsys not formed yet!")
        
        for i in range(len(self.city)):
            self.allocated_city[self.indsx[i]][self.indsy[i]].append(self.city[i])
        
    

