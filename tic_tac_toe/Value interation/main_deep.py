import numpy as np
from env import Env
from Deep_agents import agent_1
from Deep_agents import agent_2
from Deep_agents import agent_random
from Deep_agents import Human
from Deep_agents import play

################################
# Value approximation with FNN #
################################

a_O_1 = agent_1()
a_O_1.FNN()
a_O_1.set_symbol(1)


a_X_1 = agent_1()
a_X_1.FNN()
a_X_1.set_symbol(-1)


def train_FNN(a_O, a_X, e):

      state_history = []


      ####################
      # play an episode  #
      ####################
      while not e.game_over():
            a_X.play(e)
            state_history.append(e.vectorize_state())
            if not e.game_over():
                a_O.play(e)
            state_history.append(e.vectorize_state())
      ####################
      #  train FNN       #
      ####################
      rX = 0
      if e.winner == -1:
          rX = 1
      elif e.winner == 1:
          rX = -1 
      for s_x in reversed(state_history):

           V_x = a_X.alpha*rX + (1 - a_X.alpha)*a_X.fnn_model.predict(s_x)      
           a_X.fnn_model.fit(s_x, V_x, epochs = 5, verbose = False)
           rX = a_X.fnn_model.predict(s_x)

      rO = 0
      if e.winner == 1:
          rO = 1
      elif e.winner == -1:
          rO = -1
      for s_o in reversed(state_history):

           V_o = a_O.alpha*rO + (1 - a_O.alpha)*a_O.fnn_model.predict(s_o)
           a_O.fnn_model.fit(s_o, V_o, epochs = 5, verbose = False)
           rO = a_O.fnn_model.predict(s_o)


#########################
#  train 10000 episodes #
#########################

for i in range(10000):
       e = Env()
       train_FNN(a_O_1, a_X_1, e)
       if i%1000 == 0:
          print(i)




#########################
# Approximate with CNN  #
#########################

a_O_2 = agent_2()
a_O_2.CNN()
a_O_2.set_symbol(1)


a_X_2 = agent_2()
a_X_2.CNN()
a_X_2.set_symbol(-1)


def train_CNN(a_O, a_X, e):

      state_history = []


      ####################
      # play an episode  #
      ####################
      while not e.game_over():
            a_X.play(e)
            state_history.append(e.state_2D())
            if not e.game_over():
                a_O.play(e)
            state_history.append(e.state_2D())
      ####################
      #  train CNN       #
      ####################
      rX = 0
      if e.winner == -1:
          rX = 1
      elif e.winner == 1:
          rX = -1 
      for s_x in reversed(state_history):

           V_x = a_X.alpha*rX + (1 - a_X.alpha)*a_X.cnn_model.predict(s_x)      
           a_X.cnn_model.fit(s_x, V_x, epochs = 5, verbose = False)
           rX = a_X.cnn_model.predict(s_x)

      rO = 0
      if e.winner == 1:
          rO = 1
      elif e.winner == -1:
          rO = -1
      for s_o in reversed(state_history):

           V_o = a_O.alpha*rO + (1 - a_O.alpha)*a_O.cnn_model.predict(s_o)
           a_O.cnn_model.fit(s_o, V_o, epochs = 5, verbose = False)
           rO = a_O.cnn_model.predict(s_o)
      



#########################
#  train 30000 episodes #
#########################

for i in range(30000):
       e = Env()
       train_CNN(a_O_2, a_X_2, e)
       if i%1000 == 0:
          print(i)
      
                
#########################
#  play                 #
#########################
#e= Env()
#h= Human()
#play(e,h,a_X)
