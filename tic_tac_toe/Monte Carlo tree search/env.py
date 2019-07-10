import numpy as np

class Env:
    def __init__(self):
         self.board = np.zeros((3,3))
         self.winner = None
         self.ended = False
         self.O = 1
         self.X = -1
         self.state_size = 3**(3*3)



    def reward(self,symbol):
         if not self.game_over():
           return(0)
         if self.winner == symbol:
           return(1)
         elif self.winner == None:
           return(0)
         else:
           return(-1)


    def vectorize_state(self):

         state_vec = [] 
         for i in range(3):
            for j in range(3):
              state_vec.append(self.board[i,j])
         state_vec = np.array([state_vec])

         state_vec = state_vec.reshape((1,9))
         
         return(state_vec)


    def state_2D(self):

         state_2D = np.array(self.board)
         state_2D = state_2D.reshape((1,3,3,1))

         return(state_2D)
	
	def get_state(self):
         #####################
         # Use 3-base number #
         #####################
         state = 0
         for i in range(3):
            for j in range(3):
                if self.board[i,j] == 0:
                    u = 0
                elif self.board[i,j] == self.O:
                    u = 1
                else:
                    u = 2
                state +=  3**(3*i + j)*u
         return (state)

    def game_over(self):      
        
         for i in range(3):
                if np.sum(self.board[i,:]) == self.O*3:
                   self.winner = 1
                   self.ended = True
                   return(True)
                elif np.sum(self.board[i,:]) == self.X*3:
                   self.winner = -1
                   self.ended = True
                   return(True)
         for j in range(3):
                if np.sum(self.board[:,j]) == self.O*3:
                   self.winner = 1
                   self.ended = True
                   return(True)
                elif np.sum(self.board[:,j]) == self.X*3:
                   self.winner = -1
                   return(True)
         diag_1 = 0
         diag_2 = 0
         for i in range(3):
                diag_1 = self.board[i,i] + diag_1
                diag_2 = self.board[i,(2-i)] + diag_2

         if diag_1 == self.O*3 or diag_2 == self.O*3:
                self.winner = 1
                self.ended = True
                return(True)
         elif diag_1 == self.X*3 or diag_2 == self.X*3:
                self.winner = -1
                self.ended = True
                return(True)
                
         ##################
         # check if draw  #   
         ##################
         if np.all((self.board == 0) == False):
             self.winner = None
             self.ended = True
             return(True)

         self.winner = None
         self.ended = False 
         return(False)
	
    def is_empty(self, i ,j):
         return self.board[i][j] == 0



    def feasible_actions(self):

              feasible_actions = []

              for j in range(3):
                  for i in range(3):
                    if self.is_empty(i,j):
                       feasible_actions.append([i,j])       
              return(feasible_actions) 


    def draw_board(self):
        for i in range(3):
            print('-------------')
            for j in range(3):
              print('  ', end='')
              if self.board[i,j] == self.O:
                  print('O ', end='')
              elif self.board[i,j] == self.X:
                  print('X ', end='')
              else:
                  print('  ', end='')
            print('')
        print('-------------')

    def reset_env(self):
         self.board = np.zeros((3,3))
         self.winner = None
         self.ended = False
