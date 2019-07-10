import numpy as np
class Node:

       def __init__(self):

               self.parent = None
               self.children = []
               self.n_i = 0
               self.V_i = 0
               self.state = np.zeros((3,3)) 

       def get_children(self):
               return(self.children)
