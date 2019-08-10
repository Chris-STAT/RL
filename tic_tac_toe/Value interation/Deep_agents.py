import numpy as np
import keras
import keras.layers as L
from keras import models

##############################
#        Deep agents         #
##############################

class agent_1:

        def __init__(self, eps = 0.15, alpha = 0.5):

               self.eps = eps
               self.alpha = alpha

        def set_symbol(self,symbol):

              self.symbol = symbol


        def FNN(self):

            self.fnn_model = models.Sequential()
            self.fnn_model.add(L.Dense(16, activation = 'relu', input_dim = 9))
            self.fnn_model.add(L.Dense(32, activation = 'relu'))
            self.fnn_model.add(L.Dense(16, activation = 'relu'))
            self.fnn_model.add(L.Dense(1, activation = 'linear'))
            self.fnn_model.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])

              
        #########################
        #    epsilon-greedy     #
        #########################
        
        def get_action(self, env):

            feasible_actions = env.feasible_actions()
            feasible_actions_nbr = len(feasible_actions)

            action = None

            #####################################
            #  If the agent can win, then win!  #
            #####################################
            
            
            for act_0 in feasible_actions:
 
                    env.board[act_0[0], act_0[1]] = self.symbol
                    if env.game_over():
                        action = act_0
                    env.board[act_0[0], act_0[1]] = 0
                    env.game_over()

            if action == None:                           

                p = np.random.uniform(0,1)

                if p < self.eps:

                   idx = np.random.randint(feasible_actions_nbr)
                   action = feasible_actions[idx]

                else:

                   best_V = np.NINF

                   for act in feasible_actions:

                       env.board[act[0], act[1]] = self.symbol
                       V_pred = self.fnn_model.predict(env.vectorize_state())
                       env.board[act[0], act[1]] = 0
                       if best_V < V_pred:
                           best_V = V_pred
                           action = act
            return(action)
        
        #def get_action(self, env):
        #
        #    feasible_actions = env.feasible_actions()
        #    feasible_actions_nbr = len(feasible_actions)

        #   action = None

        #    p = np.random.uniform(0,1)

        #    if p < self.eps:

        #       idx = np.random.randint(feasible_actions_nbr)
        #       action = feasible_actions[idx]

        #   else:

        #       best_V = np.NINF

        #       for act in feasible_actions:

        #         env.board[act[0], act[1]] = self.symbol
        #          V_pred = self.fnn_model.predict(env.vectorize_state())
        #          env.board[act[0], act[1]] = 0
        #          if best_V < V_pred:
        #            best_V = V_pred
                    action = act
        #    return(action)

        def play(self, env):

           act = self.get_action(env)
           env.board[act[0], act[1]] = self.symbol


class agent_2:

        def __init__(self, eps = 0.15, alpha = 0.5):

               self.eps = eps
               self.alpha = alpha

        def set_symbol(self,symbol):

              self.symbol = symbol


        def CNN(self):

              self.cnn_model = models.Sequential()
              self.cnn_model.add(L.InputLayer((3,3,1)))
              self.cnn_model.add(L.Conv2D(16,(2,2), padding = 'same', activation = 'relu'))
              self.cnn_model.add(L.MaxPooling2D((2,2)))
              self.cnn_model.add(L.Flatten())
              self.cnn_model.add(L.Dense(32, activation = 'relu'))
              self.cnn_model.add(L.Dense(1, activation = 'linear'))
              self.cnn_model.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])

                                 
              
        #########################
        #    epsilon-greedy     #
        #########################
        
        def get_action(self, env):

            feasible_actions = env.feasible_actions()
            feasible_actions_nbr = len(feasible_actions)

            action = None

            #####################################
            #  If the agent can win, then win!  #
            #####################################
            
            
            for act_0 in feasible_actions:
 
                    env.board[act_0[0], act_0[1]] = self.symbol
                    if env.game_over():
                        action = act_0
                    env.board[act_0[0], act_0[1]] = 0
                    env.game_over()

            if action == None:                           

                p = np.random.uniform(0,1)

                if p < self.eps:

                   idx = np.random.randint(feasible_actions_nbr)
                   action = feasible_actions[idx]

                else:

                   best_V = np.NINF

                   for act in feasible_actions:

                       env.board[act[0], act[1]] = self.symbol
                       V_pred = self.cnn_model.predict(env.state_2D())
                       env.board[act[0], act[1]] = 0
                       if best_V < V_pred:
                           best_V = V_pred
                           action = act
            return(action)


        def play(self, env):

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
