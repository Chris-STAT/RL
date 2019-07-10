import numpy as np
from env import Env
from Node import Node 
class MCTS:

       def __init__(self, C, symbol):

            self.C = C 
            self.symbol = symbol
            
            
            
       
       def traversal(self, current_node):

              while len(current_node.get_children()) > 0:

                UCB1 = [node.V_i + self.C*np.sqrt(np.log(current_node.n_i)/node.n_i) for node in current_node.get_children()]
                next_node = np.argmax(UCB1)
                current_node = current_node.get_children()[next_node]

              return(current_node) 
        

       def random_play(self, state):

            e = Env()
            e.board = state.copy()
            count_O = (np.array(state) == 1).sum()
            count_X = (np.array(state) == -1).sum()

            if count_O < count_X:

                 sym = 1  

            else:

                 sym = -1
        
            while not e.game_over():

                feasible_actions = e.feasible_actions()
                feasible_actions_nbr = len(feasible_actions)

                idx = np.random.randint(feasible_actions_nbr)
                action = feasible_actions[idx]

                e.board[action[0], action[1]] = sym

                sym = sym*(-1)

            return(e.reward(self.symbol))                 


          

       def rollout(self, current_node):
        
              current_node = current_node
              
              e_temp = Env()
               
              e_temp.board = current_node.state.copy()

              if current_node.n_i == 0 or e_temp.game_over():
                  
                  V = self.random_play(current_node.state)
                  current_node.V_i = (current_node.V_i*current_node.n_i + V)/(current_node.n_i + 1)
                  current_node.n_i = current_node.n_i + 1 
              
                  return(current_node)

              else:

                  e = Env()
                  e.board = current_node.state.copy()
                  count_O = (np.array(e.board) == 1).sum()
                  count_X = (np.array(e.board) == -1).sum()

                  if count_O < count_X:

                      sym = 1  

                  else:

                      sym = -1

                  feasible_actions = e.feasible_actions()

                  for act in feasible_actions:

                      e.board[act[0], act[1]] = sym
                      new_node = Node()
                      new_node.parent = current_node
                      new_node.state = e.board.copy()
                      e.board[act[0], act[1]] = 0
                      current_node.children.append(new_node)
                  
                  child_node = current_node.children[0]

                  V = self.random_play(child_node.state)

                  child_node.V_i = (child_node.V_i*child_node.n_i + V)/(child_node.n_i + 1)
                  child_node.n_i = child_node.n_i +1 
                  
                
              return(child_node)
            
            


       def backpropagation(self, current_node):

                   while current_node.parent is not None:
                       current_node.parent.V_i = (current_node.parent.V_i*current_node.parent.n_i + current_node.V_i)/(current_node.parent.n_i + 1)
                       current_node.parent.n_i = current_node.parent.n_i + 1
                       current_node = current_node.parent
