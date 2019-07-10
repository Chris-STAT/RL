import numpy as np

class Env:
    def __init__(self):
         self.grid = np.zeros((6,7))
         self.winner = None
         self.ended = False
         self.red = 1
         self.black = -1
         self.state_size = 3**(6*7)

    def is_empty(self, i ,j):
         return self.grid[i][j] == 0


    def reward(self,color):
         if not self.game_over():
           return(0)
         if self.winner == color:
           return(1)
         elif self.winner == None:
           return(0)
         else:
           return(-1)

    def get_state(self):
         #####################
         # Use 3-base number #
         #####################
         state = 0
         for i in range(6):
            for j in range(7):
                if self.grid[i,j] == 0:
                    u = 0
                elif self.grid[i,j] == self.red:
                    u = 1
                else:
                    u = 2
                state +=  3**(3*i + j)*u
         return (state)

    def game_over(self):      
        
         for i in range(6):
            for l in range(5):
                if np.sum(self.grid[i,l:(l+3)]) == self.red*3:
                   self.winner = 1
                   self.ended = True
                   return(True)
                elif np.sum(self.grid[i,l:(l+3)]) == self.black*3:
                   self.winner = -1
                   self.ended = True
                   return(True)
         for j in range(7):
            for m in range(4):
                if np.sum(self.grid[m:(m+3),j]) == self.red*3:
                   self.winner = 1
                   self.ended = True
                   return(True)
                elif np.sum(self.grid[m:(m+3),j]) == self.black*3:
                   self.winner = -1
                   return(True)
         for i in range(6):
            for j in range(7):
                diag_sum = 0
                s,t = i,j
                while(s<=3 and s<=i+2 and t<=3 and t<=j+2):
                      diag_sum += self.grid[s,t]
                      s += 1
                      t += 1
                if diag_sum == self.red*3:
                   self.winner =  1
                   self.eneded = True 
                   return(True)
                elif diag_sum == self.black*3:
                   self.winner = -1
                   self.ended = True 
                   return(True)

                ss, tt = i,j  
                diag_sum = 0
                while (ss<=3 and ss<=i+2 and tt>=0 and tt>=j-2):
                       diag_sum += self.grid[ss,tt]
                       ss +=1
                       tt -=1
                if diag_sum == self.red*3:
                   self.winner = 1
                   self.ended = True
                   return(True)
                elif diag_sum == self.black*3:
                   self.winner = -1
                   self.ended = True
                   return(True)
                   
                
         ##################
         # check if draw  #   
         ##################
         if np.all((self.grid == 0) == False):
             self.winner = None
             self.ended = True
             return(True)


         self.winner = None
         self.ended = False 
         return(False)



    def feasible_actions(self):

              feasible_actions = []

              for j in range(7):
                  for i in list(range(6))[::-1]:
                    if self.is_empty(i,j):
                       feasible_actions.append([i,j])
                       break       
                    
              return(feasible_actions) 


    def draw_grid(self):
        for i in range(6):
            print('----------------')
            for j in range(7):
              print('  ', end='')
              if self.grid[i,j] == self.red:
                  print('R ', end='')
              elif self.grid[i,j] == self.black:
                  print('B ', end='')
              else:
                  print('  ', end='')
            print('')
        print('----------------')

    def reset_env(self):
         self.grid = np.zeros((6,7))
         self.winner = None
         self.ended = False

