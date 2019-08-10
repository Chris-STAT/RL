import numpy as np
import matplotlib.pyplot as plt

from env import Env
from agents import agent
from agents import agent_random
from agents import Human
from agents import play


e = Env()

a_O = agent()
a_O.setV()
a_O.set_symbol(1)


a_X = agent()
a_X.setV()
a_X.set_symbol(-1)


def train(a_O, a_X, e):

      state_history = []


      ####################
      # play an episode  #
      ####################
      while not e.game_over():
            a_X.play(e)
            state_history.append(e.get_state())
            if not e.game_over():
                a_O.play(e)
            state_history.append(e.get_state())
      ####################
      #  value iteration #
      ####################
      rX = 0
      if e.winner == -1:
          rX = 1
      elif e.winner == 1:
          rX = -1 
      for s_x in reversed(state_history):
          V_rX = a_X.alpha*rX + (1 - a_X.alpha)*a_X.V[s_x]
          a_X.V[s_x] = V_rX
          rX = a_X.V[s_x]

      rO = 0
      if e.winner == 1:
          rO = 1
      elif e.winner == -1:
          rO = -1
      for s_o in reversed(state_history):
          V_rO = a_O.alpha*rO + (1 - a_O.alpha)*a_O.V[s_o]
          a_O.V[s_o] = V_rO
          rO = a_O.V[s_o]
      



#########################
#  train 50000 episodes #
#########################

winning_rate = []
a_rand = agent_random()
a_rand.set_symbol(1)

for i in range(10):
   for j in range(1000):

       e = Env()
       train(a_O, a_X, e)

   X_win = []    
   for k in range(50000):
       e_p = Env()
       while not e_p.game_over():
            a_X.play(e_p)
            if not e_p.game_over():
                 a_rand.play(e_p)
       if e_p.winner == 1:
            X_win.append(0)
       else:
            X_win.append(1)
   winning_rate.append(sum(X_win)/50000.0)
   print(i)
      
                
#########################
#  play                 #
#########################
#e= Env()
#h= Human()
#play(e,h,a_X)
