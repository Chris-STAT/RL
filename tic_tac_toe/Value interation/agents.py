import numpy as np
import matplotlib.pyplot as plt
##################################
#     agent (value iteration)    #
##################################
class agent:

       def __init__(self, eps = 0.1, alpha = 0.5):

             self.eps = eps
             self.alpha = alpha 
             

       def  setV(self):

              self.V = np.zeros((3**(3*3)))
         

       
       def  set_symbol(self, symbol):

              self.symbol = symbol 

       #########################
       #     epsilon-greedy    #	   
       #########################
                                 
       def  get_action(self, env):

               feasible_actions = env.feasible_actions()
               feasible_actions_nbr = len(feasible_actions)

               p = np.random.uniform(0,1)

               if p < self.eps:

                    idx = np.random.randint(feasible_actions_nbr)
                    action = feasible_actions[idx]

               else:

                    best_V = np.NINF

                    for act in feasible_actions:
                                
                        env.board[act[0],act[1]] = self.symbol
                        V_tmp = self.V[env.get_state()] + env.reward(self.symbol)
                                  
                        env.board[act[0],act[1]] = 0

                        if best_V < V_tmp:
                            best_V = V_tmp
                            action = act                

               return(action)     

                               
       def play(self,env):

                old_state = env.get_state() 
                act = self.get_action(env)
                env.board[act[0], act[1]] = self.symbol


#######################################
#           random agent              #
#######################################

class agent_random:

       def set_symbol(self, symbol):

                self.symbol = symbol

       def play(self, env):
               
                feasible_actions = env.feasible_actions()
                feasible_actions_nbr = len(feasible_actions)

                idx = np.random.randint(feasible_actions_nbr)
                action = feasible_actions[idx]
                env.board[action[0], action[1]] = self.symbol


#######################################
#              Human                  #
#######################################

class Human:

    def __init__(self):
        pass

    def usr_play(self,env):

        action = [int(x) for x in input().split()]

        while action not in env.feasible_actions():
            print("This is not a legitimate action! Please input a another action.")
            action = [int(x) for x in input().split()]
        
        env.board[action[0], action[1]] = 1


#############
#  Play!    #
#############

def play(Env, H, agent):

      print("Do you want to play? Yes/No")
      ans = input ()
      while ans.lower() == 'yes':
         while not Env.game_over():
           agent.play(Env)
           Env.draw_board()
           if not Env.game_over():
             print("Please take an action!")
             H.usr_play(Env)
             Env.draw_board()
         if Env.winner == -1:
            print('Game over! The winner is {0}'.format('X'))
         elif Env.winner == 1:
            print('Game over! The winner is {0}'.format('O'))
         else:
            print('Game over! It is a draw!')
         Env.reset_env()
         print("Do you want to play again? Yes/No")
         ans = input()

      print("Session ended!")
